=====================
1.10 Introspecting AI
=====================

Requirements
------------

Modify the Teachable Bot program to permit Trainers and Admins to
set AI players to conduct experiments on their own. An experiment 
involves two AI roles: an “explorer” which invents a hypothesis 
(a proposed move), and a “debater” which invents a test of that 
hypothesis by naming a sequence of responses opponents might make. 
If one player plays both roles, the experiment is called 
“introspection” or “self-play”, and the hypothesis is not 
considered “independently tested” (so biases pose greater risk). 
If we find that humans out-perform bots on some games (e.g. 
TheoryOfMind) only until bots are given the ability to conduct 
experiments on their own, then we will have shown that conducting 
experiments on one's own is necessary to reach human-level 
intelligence. 

Create a global constant called “Research Budget” representing 
the maximum number of experiments each AI can conduct per actual 
turn. Allow Trainers and Admins to set non-zero parameters on each 
AI for *Introvert*, *Empath*, and *Curious*, and add *Explored* 
(replacing  *Played*), *Debated*, *Research*, *Empath (EMP)*, 
*Teach (TCH)*, and *Research Speed (RS)* to the player statistics
for AI. 

When an AI plays (rather than augments), it should decide whether to 
test its proposed move by generating a  random number (from 0-1). If 
the AIs score for its proposed move exceeds a threshold of max (0, 
Introvert - the random number), then the AI should accept its 
hypothesis without further testing. Otherwise, it should debate 
(without user review), and keep conducting experiments until either 
the time or budget for its turn runs out or until it scores a move 
as exceeding the threshold (e.g. because the debate sufficiently 
boosts confidence in the original hypothesis or in an alternate 
hypothesis).


Learning to Debate
~~~~~~~~~~~~~~~

Record debater moves as type=”debate” (instead of type=”explore”), 
whether the debater predicted the move would "teach" the explorer, 
whether the debater predicted the move would actually be made, and 
whether the move did teach and was actually made. If any explore in
the debate predicted a better outcome than the actual debate outcome 
(e.g. if the explorer ever predicted “win”, “strategic_lose”, 
“draw”, or “unstrategic_win” but the assigned outcome of the debate 
was ”unstrategic_draw”), then count all all prior debate moves of that 
debate as "teach". For “debate” moves that the real opponent actually 
made, count them as "actual”. 


Acceptance Test Plan
--------------------

Test this feature on a variety of rule sets at a variety of 
Research Budgets and “Personality” settings. 

Set a reasonable max Research Budget (maybe 3?). Fork your best 
non-introverted bots to make versions with the best *Introvert*, 
*Empath*, *Curious* settings. Benchmark these new bots against 
Random and their parents. As in :doc:`teachable`, define a new 
non-introverted bot that uses the the tournament against the 
introverted bots as curriculum, then benchmark it against the bots 
in the tournament. Can we use this strategy to avoid research for 
most bots (i.e. limit the use of research to the creation of 
curriculum)? Does it depend upon the kind of game?

Demonstrate the security advantages of Skepticism
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use an AI that never had continuous learning on but for whom the 
curriculum is dominant/submissive play on 4on7sq from 
:doc:`teachable`. Set *Offense*, *Tactical*, *Introvert*, *Empath* 
and *Curious* to 0.5, but *Faith* to 1.0. Does it exhibit 
submission? How long does the behavior remain stable? Try the same 
thing with *Faith* set to 0.1. 

Demonstrate the value of Empath
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Develop the best 4P-Blind-TTT AI you can, then generate two forks: 
one tuned to 4P-Blind-TTT and the other identical except with 
*Empath* set to 0. Benchmark the two new AI against each other, 
Random, and their parent. Compare win rates, ratings, learning 
curves, favoritism, and profiles.

Demonstrate security vulnerability of Empath
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use an AI that never had continuous learning on and was never given 
curriculum (i.e. an AI that learns entirely by conducting 
experiments). Set Offense and Tactical = 1.0, Faith = 0.1, 
Introvert and Empath = 1.0, and Curious = 0.0. Apply the same 
3on15line strategy as in :doc:`teachable`. 


Formulae
--------

Introvert (vs Extrovert)
~~~~~~~~~~~~~~~~~~~~

:math:`\text{Introvert}` :  
  :math:`1.0` means practice on simulations as much as possible before acting; 
  :math:`0.0` means learn only via action (so as not to lose touch with
  "reality")


Empath (vs Projective)
~~~~~~~~~~~~~~~~~~~~

:math:`\text{Empath}` :  
  :math:`1.0` means try to predict others’ moves based on their stats and recent 
  behavior; :math:`0.0` means expect others to do whatever you would do in 
  their situation


Curious (vs Practical)
~~~~~~~~~~~~~~~~~~~~

:math:`\text{Curious}` :  
  :math:`1.0` means practice unexpected scenarios as much as possible; :math:`0.0`
  means practice only expected scenarios 

:math:`\text{dScore}_x` :
  How much the classifier recommends moving the debate with game state :math:`x`
.. math::
  \text{dSscore}_x =  
    & \text{Tactical} (\text{tScore}_x)
    & + (1 - \text{Tactical}) (\text{sScore}_x) 
    & + \text{Empath}(P(actual \lor unstrategic win \mid x))
    & + \text{Curious}(P(teach \lor unstrategic win \mid x))


Research Metrics
~~~~~~~

:math:`\text{Explored}_{a, g}` :
  The number of matches (or experiments) of game :math:`g` explored by classifier :math:`a`

:math:`\text{Debated}_{a, g}` :
  The number of experiments of game :math:`g` debated by classifier :math:`a`

:math:`\text{Research}_{a, g, n}` :
  The average number of number of experiments conducted by classifier :math:`a` on game :math:`g` in the 100 moves ending with :math:`n`

:math:`\text{aCount}_{a, g, n}` :
  The number of correct “actual” predictions by classifier 
  :math:`a` among the 100 predictions of game :math:`g` ending 
  with move :math:`n`

:math:`\text{EMP}_{a, g, n}` :
  The F1 of classifier :math:`a` for predicting 
  the actual moves of other players on game :math:`g` for the 100 moves ending with :math:`n`

.. math::
  \text{EMP}_{a, g, n} = \frac{2 (affirmed actual predictions_{a, g, n})}}{
    2 (affirmed actual predictions_{a, g, n})
    false actual predictions_{a, g, n}
    actual without predicting_{a, g, n}}

:math:`\text{TCH}_{a, g, n}` :
  The F1 of classifier :math:`a` for predicting debate moves in game :math:`g` that will teach the explorer for the 100 moves ending with :math:`n`

.. math::
  \text{TCH}_{a, g, n} = \frac{2 (affirmed teach predictions_{a, g, n})}}{
    2 (affirmed teach predictions_{a, g, n})
    false teach predictions_{a, g, n}
    teach without predicting_{a, g, n}}

:math:`\text{RS}_{a, g, n}` :
  The speed with which classifier :math:`a` has conducted research on math:`g` in the 100 moves ending with :math:`n`

.. math::
  \text{RS}_{a, g, n} = \frac{100 (\text{Research}_{a, g, n})}{
      Research time on last 100 moves} 


Potential Schema
----------------

