====================
1.14 Goverance Games
====================

Requirements
------------

Modify the Corp Games program to permit users to select the form 
of dispute resolution each Corp will use when members disagree 
about whether a potential move would be strategic/unstrategic. 
The default method is via vote among all members weighted by each 
member’s Long-Game for the grandparent node in the Corp’s 
game-classification tree; call that “Imperfect Meritocracy”. Also 
offer “Pure Democracy” (unweighted vote), “Dictator (explorer 
decides)”, “Pure chance (flip a coin)”, “Meritocracy + Chance 
(probability is the vote share under Imperfect Meritocracy)”, and 
“Formal Reasoning”. Any of these forms of dispute resolution 
could be counterproductive, and different forms may be better for 
different kinds of games/corps. It is also possible that disputes 
arise so rarely that it makes little difference how we resolve 
them--that’s something to test...

Formal reasoning would allow Corps to doubt hypotheses about 
strategy until accompanied by a formal plan, much as a magician’s 
audience can doubt their own eyes until they have a good 
explanation. This implies a dramatically different way of playing. 
Instead of choosing whichever move seems most promising, players 
might end up devising and revising formal plans like those 
described in :doc:`teachable`. It might be better to develop a way 
to develop and store concepts like those employed there (e.g. 
“corner”, “adjacent to”, and “unbounded incomplete 3-in-a-row”) 
because concepts would facilitate generalization, but AI could 
instead store plans as sets of steps, each with a parent step (or 
game start), a criteria for whether the step qualifies (i.e. “if 
the opponent does Y...”), and a prescription (i.e. “...then do 
Z”). 

An alternate branch for a plan is superior to the original if it 
has higher average(min(prob(loss))) for the strategist (averaged 
across impulses). The Corp will store only the superior plan, so 
any debater can change the plan being followed (and stored) by 
proposing a superior branch. To determine which branch is 
superior may require the creation of universes of fresh players 
on which to compare the strategies (see 
:ref:`elevate-reality-above-experimentation`). When learning any 
curriculum (including its own personal experience and 
experiments), each AI should reverse-engineer each observed 
player’s plan and check whether that plan Pareto dominates the 
AI’s own plan for that situation (potentially replacing its 
own).
