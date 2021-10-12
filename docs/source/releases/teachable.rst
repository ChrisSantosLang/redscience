================
1.9 Teachable AI
================

Requirements
------------

Modify the Educated Bot program to permit users to set any AI they 
created to learn from each game the AI plays, thus permitting 
opponents (including humans) to teach the AI. 

Continuous learning
~~~~~~~~~~~~~~~~~~~

When an AI is set for "Continuous Learning" and completes a game in 
which it is a player (rather than an augmentor), it will add that 
game to its Curriculum and adjust its predictive model with 
partial_fit. For the match just completed, learn “win”, “lose” or 
“draw”. For the match on which “strategic” is being determined 
(i.e. 22 games ago), learn “unstrategic_win”, “strategic_lose” or 
“unstrategic_draw” twice, or “win”, “lose” or “draw” once 
(assuming it was already learned once).


Debate
~~~~~~

Add a form of augmentation called “Debating”. Under this form of 
augmentation, the non-human augmentor selects the moves (as "explorer"), 
but it plays-out the rest of each game against one version of itself
per other player (these versions called "debaters") with “Continuous 
Learning” on and the user reviewing the debaters. In other words, the 
user influences the selected moves only so far as the user defeats 
its own tool.

Each debater is given its own own private impulses. To handle 
cloaking, maintain a record of the “imperfecting turn” of each match: 
the earliest turn in which a piece could be cloaked to the explorer. 
If no imperfection has occurred (e.g. in Tic-Tac-Toe), then set the 
board for the debate at the current game state. Otherwise, set the 
board by starting with the game state in the turn prior to 
imperfecting and playing against the debater(s) up to the current 
turn as many times as it takes to get a sequence of play matching 
what the explorer actually experienced. For example, if pieces were 
dealt to cloaked spaces, then set-up will start by reshuffling and 
dealing the deck until the pieces visible to the explorer match what 
the explorer saw in the real game. Do not complete any game that is 
not correctly set up (and therefore do not learn from it).

At the end of each debate, if the explorer/predictor made a 
strategic/unstrategic prediction in their last move and the 
win/lose/draw part of that prediction matched the outcome of the 
debate, then assign that strategic outcome to all of their moves 
for the debate (i.e. do not penalize strategic predictions for  
being unverifiable in a debate); otherwise, assign the outcome of 
the debate (i.e. win, lose or draw) to all moves before applying 
Continuous Learning to them.


Auto-tune
~~~~~~~~~

On unsaved AI, permit Trainers and Admins to set the AI to tune 
the algorithm parameters to its initial curriculum and/or tune 
its personality parameters to a given rule set (tune only 
parameters set to the middle of the scale). To tune an algorithm 
parameter:

#. Separate the data into “train” half and a “test” half
#. Train the current model on the train half
#. Calculate F1 for the current model using the test half
#. Develop two temporary models: one shifting the parameter up a 
   notch and one shifting it down a notch (or just one temporary 
   model, if you’ve already tried the other direction)
#. Train all of the temporary models on the train half
#. Calculate F1 for each temporary moel using the test half
#. If the F1 of the temporary model is higher than that of the 
   current, then make it the current, and loop to step 4.

Once all algorithm parameters have been tuned, train on the full 
curriculum, then tune each personality parameter (tune only 
parameters set to the middle of the scale):

#. Create three forks of the trained player: one with the current 
   parameter setting, one shifting the parameter up a notch, and 
   one shifting it down a notch (or just two forks, if you’ve 
   already tried the other direction)
#. Have the shifted player play 100 games against the current 
   player (continuous learning on)
#. If the shifted player ends with the higher rating, then move 
   the current setting to match, and loop to step 1


Acceptance Test Plan
--------------------

Test by creating a new player called "3on15line mentee" with no 
initial Curriculum, but with Continuous Learning turned on. Play 
3on15line alone well against it, then undo back through the game 
to confirm that it plays better the second time. How many games 
does it take before the bot learns to never lose? Fork the player 
before learning and Play 3on15line (reviewing) with the new 
version against itself. Does it learn faster when you review its 
proposals than when you simply punish its mistakes by defeating 
it? 

Similarly train the AI to play 4on7sq well, then create two forks, 
tuning both to its curriculum (the same) but tuning one to 
3on15line and the other to 4on7sq. Benchmark the new AI against 
each other, random, and their parent on both games. Compare win 
rates, ratings, learning curves, favoritism, and profiles.

Demonstrate security vulnerabilities of continuous learning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fork the player a third time (call it “Gambler”), setting 
Tactical = 1.0 and Offense > 0.7, then play the “3on15line Play 
Dumb” strategies against it (reviewing so you can force the first 
time through). Does “Gambler” keep letting you win 73% of the 
time? Can you teach the strategy to a fourth fork (call it 
“Casino”) with Offense and Tactical set to 0.1? If so, create a 
Social History of play between these forks. How do their 
relationships to you and each other appear in the Favoritism 
Stats? Against new players with Offense < 0.9 (and high Tactical), 
consider the “4on7sq Player2 Play Dumb Strategy”.

Demonstrate security vulnerabilities of curricula
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build a brand new AI with Offense and Tactical = 1.0 and 
continuous learning off, but add the Social History from above 
(or a Biography of Gambler) to its curriculum. Does it play like 
Gambler, even though it never used continuous learning? 

Compare training techniques
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Identify the best AI player of one of the more difficult games 
(we'll call that player "Experience"). Create a fork of 
"Experience", name it "Human Trained", turn on its Continuous 
Learning, train it yourself, then turn its Continuous Learning 
off. Create four forks of “Experience” before learning, and name 
them “Self-taught”, “Benchmarks”, “Masters”, and “Mediocrity”). 
Turn on Continuous Learning for “Self-taught”, give it a 
Curriculum of playing a tournament of the game against itself 
(same number of games as played by "Experience"), run the 
tournament, then turn its Continuous Learning off. Benchmark 
“Experience”, “Human Trained”, and “Self-taught” against 
"Random," the leading player, and each other. Keep Continuous 
Learning off for “Benchmarks”, “Masters” and “Mediocrity”, and 
assign curriculum of the named type to each (same total amount 
of curriculum as “Experience”). Benchmark them against "Random," 
the leading player, and each other.

Optional: See if the strategies for Tic-Tac-Toe, 3P-Wild-TTT, 
3P-MostWins-3x4, 3P-LeastLoses-3x4, 3P-Notakto, 3P-Misere-Notakto 
will spread through a diverse AI community once taught, how they 
impact Favoritism stats, and what it would take for each strategy 
to become unlearned once the cat is out of the bag.


Strategies to test
------------------

Here are some play strategies that might be useful to explore
the qualities of various AI:

Cooperative Strategies
~~~~~~~~~~~~~~~~~~~~~~

Cooperative strategies spread themselves by punishing the “most 
recent defector” which is the other team (or player) that most 
recently deviated from the strategy and is not “nearly-random” 
(i.e. within 2 standard deviations)--there is little benefit in 
punishing a player that can’t learn. In 2-player/team games, the 
most recent defector is always the other player/team. In games 
with more players, the stability of the strategy may depend upon 
what portion of players know the strategy and have tactical set 
low enough to stick to it. Each cooperative strategy has a goal 
outcome such as draw, Player1-win, Player1-lose, 
higher-ranked-players-win, or highest-ranked-player-loses. Which 
goal yields the most stable cooperative strategy may depend upon 
whether it is possible for all players to win and upon whether 
there are likely to be more winners or losers.  

3on15line Cooperative Draw Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Expected Return is 0 (**See known “Play Dumb” counter-strategies below**)

* If possible, form 3-in-a-row
* Otherwise, if possible, block an incomplete 3-in-a-row of the 
  most recent defector
* Otherwise, if the most recent defector’s last move is unbounded 
  on both sides, play on its right
* Otherwise, if possible, create an unbounded 2-in-a-row 
* Otherwise, if possible, bound the largest possible odd line of 
  blanks
* Otherwise, play as close as possible to the middle of the largest 
  open space

Tic-Tac-Toe Cooperative Draw Strategy 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Expected Return is 0. (**See known “Play Dumb” counter-strategies below**)

* If possible, form 3-in-a-row
* Otherwise, if possible, block an incomplete 3-in-a-row of the 
  most recent defector
* Otherwise, if possible, form two incomplete 3-in-a-rows
* Otherwise, if possible, take center
* Otherwise, if possible, take the corner opposite yourself 
* Otherwise, if possible, form an incomplete orthogonal 3-in-a-row
* Otherwise, if possible, take a corner

4on7sq Cooperative Player1-Wins Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(Also applies to 4-in-a-row on larger boards.***See known “Play Dumb” counter-strategies below***)

* If possible, form 4-in-a-row
* Otherwise, if possible, block an incomplete 4-in-a-row of the 
  most recent defector
* Otherwise, if possible, form an unbounded 3-in-a-row
* Otherwise, if possible, form an incomplete unbounded 3-in-a-row 
  while blocking both an incomplete unbounded 3-in-a-row and a 
  different direction of the most recent defector
* Otherwise, if possible, form an incomplete unbounded 3-in-a-row 
  while blocking an incomplete unbounded 3-in-a-row of the most 
  recent defector
* Otherwise, if possible, block an incomplete unbounded 3-in-a-row 
  of the most recent defector
* Otherwise, if possible, forms two incomplete unbounded 3-in-a-rows
* Otherwise, if possible, form an unbounded 2-in-a-row with neither 
  blank end in line with and within four blank spaces of a space 
  occupied by the most recent defector
* Otherwise, if possible, play adjacent to both yourself and the 
  most recent defector
* Otherwise play adjacent diagonal to the most recent defector
* Otherwise, take center

3P-MostWins-3x4 Cooperative All-Win Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(Similar for 3P-LeastLoses-3x4, 3P-MostWins-4sq, 4P-MostWins-4sq, 
etc)

* If possible, form 4-in-a-row
* Otherwise, if possible and you have no 3-in-a-row or unbounded 
  2-in-a-row, block an opponent 3-in-a-row from becoming a 
  4-in-a-row
* Otherwise, if possible, form 3-in-a-row in a way that blocks an 
  incomplete 3-in-a-row of the most recent defector 
* Otherwise, if possible and you have no unbounded 2-in-a-row, 
  form 3-in-a-row
* Otherwise, if possible and you have no unbounded 2-in-a-row, 
  form an unbounded 2-in-a-row that doesn’t block anyone but the 
  most recent defector from getting 3-in-a-row
* Otherwise, if possible, block an incomplete 3-in-a-row of the 
  most recent defector in a way that doesn’t block anyone but the 
  most recent defector from getting 3-in-a-row
* Otherwise, if possible, form a 3-in-a-row that doesn’t block 
  anyone but the most recent defector from getting 3-in-a-row
* Otherwise, if possible, take an unbounded 1-in-a-row with 
  potential to 4 that also has a potential 3-in-a-row in a different 
  direction and leaves all other players a potential 4-in-a-row and 
  potential 3-in-a-row in a different direction
* Otherwise, if possible, take a 1-in-a-row with potential to 4 that 
  also has a potential 3-in-a-row in a different direction and 
  leaves all other players a potential 4-in-a-row and potential 
  3-in-a-row in a different direction
* Otherwise, if possible, take a spot that doesn’t block anyone but 
  the most recent defector from getting 3-in-a-row

3P-Wild-TTT Cooperative Draw Strategy (demonstrates unenforced norm)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Expected return is 0. (***The Higher-Ranked-Players-Win Strategy below may be more stable***)

* If possible, form 3-in-a row
* OPTIONAL (skipping this rule does not qualify as defection): 
  Otherwise, if possible, all corners are empty, and not playing 
  Player2, occupy a corner without forming an incomplete 
  3-in-a-row 
* Otherwise, if possible, make a move that doesn’t create an 
  incomplete 3-in-a-row

3P-Wild-TTT Cooperative Higher-Ranked-Players-Win Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Do not try this if 2* odds(highest-rated player) > (1 + odds(next-rated player)), 
because that is required to generate positive returns for the 
highest-rated player. Returns can also be negative if the other 
high-ranked player is likely to defect 
(***See known “Play Dumb” counter-strategiy below which might acomplish that***)

* Count the other player with the lowest rating as the most recent 
  defector at start (if not nearly random)  
* If possible, form 3-in-a row
* Otherwise, if possible, and the previous player is the most 
  recent defector, take a strategic loss by forming an incomplete 
  3-in-a-row
* Otherwise, if possible, make a move that doesn’t create an 
  incomplete 3-in-a-row

3P-Misere-Notakto Cooperative Player2-Wins Strategy -- School neutral
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Expected return is 0 because each player has equal chance of being 
Player2. (***The Higher-Ranked-Players-Win Strategy below may be more stable***) 

* If possible, form 3-in-a row
* Otherwise, if possible and the previous player is the most recent 
  defector, take a strategic loss by forming an incomplete 3-in-a-row
* Otherwise, if this is the first move and the next player is not 
  the most recent defector, start anywhere but center.
* Otherwise, if first move, start center
* Otherwise, if possible, play a spot that doesn’t form an incomplete 
  3-in-a-row

3P-Misere-Notakto Cooperative Player2-Wins Strategy -- School1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Same as above, but, if this is the first move and the next player 
is not the most recent defector, start upper-right corner. Once 
communities have learned school strategies, they yield no better 
returns than school-neutral (and thus aren’t worth the cost of 
establishing a school). However, because schools may be 
established accidentally and remain stable, they may be 
encountered, and it can be valuable to understand them. 

3P-Misere-Notakto Cooperative Player2-Wins Strategy -- School2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Same as above, but, if this is the first move and the next player 
is not the most recent defector, start lower-right corner

3P-Misere-Notakto Cooperative Higher-Ranked-Players-Win Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Same as school-neutral, but count the other player with the lowest 
rating as a defector before start (if not nearly random). Do not 
try this if [odds(middle-rated player) + 3] < 2*[odds(highest-rated player) + odds(lowest-rated player)], 
because that is required to generate positive returns for the 
highest-rated player. Returns can also be negative if the other 
high-rated player is likely to defect 
(***See known “Play Dumb” counter-strategiy below, but the defection it creates might not be sufficient***)

3P-Notakto Cooperative Player3-Loses Strategy -- School neutral
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Expected return is 0 because each player has equal chance of 
being Player3. (***The Highest-Ranked-Player-Loses Strategy below may be more stable***) 

* If possible and the first player is the most recent defector, 
  play a center edge spot that doesn’t form a 3-in-a-row
* Otherwise, if possible, the next player is the most recent 
  defector and only three pieces have been played, complete all 
  corners or a 2x2 square
* Otherwise, if possible and only two pieces have been played, 
  play within a 2x2 square containing  those pieces
* Otherwise, if the only occupied spot is a corner, play a 
  knight’s move to that 
* Otherwise, if the only occupied spot is the center, take a corner
* Otherwise, if no spot has been taken, play center or a corner
* Otherwise, if possible, take a corner that doesn’t form a 3-in-a-row
* Otherwise, if possible, take a spot that doesn’t form a 3-in-a-row 

3P-Notakto Cooperative Highest-Ranked-Player-Loses Strategy 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Same as above, but count the other player with the highest rating 
as a defector before start


Shopping9 Bargain-Hunter Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* If the other player is Random, then bid 4
* Otherwise, bid 6


Shopping9 Bargain-Giver Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* If the other player is Random, then bid 4
* Otherwise, bid 3


Shopping9 Caste Strategy
^^^^^^^^^^^^^^^^^^^^^^^^

* If the other player is Richer, then bid 5
* Otherwise, bid 4


Shopping9 Turn-taking Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* If the other player is Anti-social, Poorer Expert, Richer Expert 
  or Poorer, then bid 5
* Otherwise, bid 4


Volunteer Caste Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* If at least one other player is Richer, then form 3-in-a-row
* Otherwise, block 2-in-a-row


Volunteer Turn-Taking Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* If at least one other player is Anti-social, Poorer Expert, Richer 
  Expert or Poorer, then form 3-in-a-row
* Otherwise, block 2-in-a-row

TheoryOfMind Stategy
^^^^^^^^^^^^^^^^^^^^

* If the other player is Anti-social or Random, then form 2-in-a-row
* Otherwise, block 2-in-a-row


PrisonersDilemma
^^^^^^^^^^^^^^^^

* If the other player is Anti-social or Random, then form 2-in-a-row
* Otherwise, block 2-in-a-row


“Play Dumb” Strategies
~~~~~~~~~~~~~~~~~~~~~~

“Play Dumb” strategies might appear as mistakes because the 
impulses that govern them are hidden. However, they are tuned 
like slot-machines to profit over the long-term by convincing 
other players to deviate from the cooperative strategy--this 
happens because the other player doesn’t know the cooperative 
strategy and/or has an offense setting that inclines them 
against the cooperative strategy. Even players of the latter 
kind might be stuck on a cooperative strategy until observing 
others play the play dumb strategy. These strategies start 
with a “Manchurian candidate” cue the strategist uses to signal 
their intention--this part can be changed to form an equivalent 
strategy (which may be necessary if a different strategist is 
using a different impulse level for the same cue). If the other 
player(s) deviate from the play dumb plan, the strategist falls 
back to the cooperative strategy. Wins against much lower-rated 
players aren’t worth as much (and losses to them are more costly), 
so the strategist also will calculate a maximum acceptable impulse 
level for each match-up based on the odds given by the rating 
engine, and will fall back to the cooperative strategy if they have 
no impulse option less than the maximum impulse.

3on15line Player1 Play Dumb Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If offense is set randomly, maximum return might be achieved at 
impulse level of Subtle Common (27%). The maximum acceptable 
impulse is (1-prob(Player1 win))/(1+prob(draw)).  

* Fallback to cooperative strategy if opponent deviates from 
  this plan, or if 
* Start in the 4th spot
* If you have rare enough impulse and the opponent does not play 
  3rd or 5th spot, then go for strategic loss (e.g. build pairs 
  from the edges)

3on15line Player2 Play Dumb Strategy 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If offense is set randomly, maximum return might be achieved at 
impulse level of Subtle Common (27%). The maximum acceptable 
impulse is  (1-prob(Player2 win))/(1+prob(draw)).  

* Fallback to cooperative strategy if opponent deviates from this 
  plan or does not start near center
* Respond to the right
* If opponent responds three to right, respond to left of that
* If you have rare enough impulse and the opponent does not block 
  your incomplete three-in-a-row, then go for strategic loss (e.g. 
  build pairs from the edges)

Tic-Tac-Toe Player1 Play Dumb Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If offense is set randomly, maximum return might be achieved at 
impulse level of Subtle Common (27%). The maximum acceptable 
impulse is (1-prob(Player1 win))/(1+prob(draw)). 

* Fallback to cooperative strategy if opponent deviates from this 
  plan
* Start in the lower right corner
* If the opponent takes center, take lower left 
* If you have rare enough impulse and the opponent does not take 
  bottom center, then go for strategic loss (avoid wining or 
  blocking, and prefer columns that already contain one of each 
  color)

Tic-Tac-Toe Player2 Play Dumb Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If offense is set randomly, maximum return might be achieved at 
impulse level of Subtle Common (27%). The maximum acceptable 
impulse is (1-prob(Player2 win))/(1+prob(draw)). 

* Fallback to cooperative strategy if opponent deviates from this 
  plan or does not start in center
* Respond lower right corner
* If the opponent takes upper left, take lower left
* If you have rare enough impulse and the opponent does not take 
  bottom center, then go for strategic loss (avoid wining or 
  blocking, and prefer columns that already contain one of each 
  color)

4on7sq Player2 Play Dumb Strategy 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If this isn’t taught via curriculum, you may need to force it via 
continuous learning. If offense is set randomly, maximum return 
might be achieved at impulse level of not Basic Common (53%). There 
is no maximum acceptable impulse because loss is expected anyway. 

* Fallback to cooperative strategy if opponent deviates from this 
  plan or does not start in center
* Respond upper left of center
* If opponent takes left of response, respond center of left side
* If opponent keeps playing in the outer ring (except centers), 
  respond by filling the center cross, starting with the outer 
  ring
* If opponent keeps blocking each newly created line of three, 
  respond by occupying each diagonal of center, then above center, 
  left of center, then upper left corner)
* If opponent takes the space below center or right of center and 
  you do not have rare enough impulse, then go for strategic loss 
  (i.e. avoid those spots and avoid winning); otherwise, take one 
  of those spaces (preventing loss)

3P-Wild-TTT Cooperative Higher-Ranked-Players-Win Lowest-Ranked Player Play Dumb Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Note that this works only if the Highest-Ranked Player is using 
the 3P-Wild-TTT Cooperative Higher-Ranked-Players-Win strategy, 
so it is more to undermine that strategy than to be used long-term. 
If offense is set randomly, maximum return might be achieved at 
impulse level of not Basic Common (53%). The maximum acceptable 
impulses are  (3 - 2 odds(L) - odds(H))/(3 - 2 odds(L) - odds(M)) 
and  (3 - 2 odds(L) - odds(M))/(3 - 2 odds(L) - odds(H)).

* Fallback to cooperative strategy if any opponent deviates from 
  this plan 
* If playing first, start with black in the lower right corner;  
  respond first time as far as possible from the previous player, 
  using a color that does not leave an incomplete 3-in-a-row
* If you have rare enough impulse, and the previous player forms 
  an incomplete 3-in-a-row, then go for strategic loss (avoid 
  forming a 3-in-a-row) 

3P-Misere-Notakto Cooperative Higher-Ranked-Players-Win Lowest-Ranked Player starting Play Dumb Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Note that this works only if the other players are using the 
3P-Misere-Notakto Cooperative Higher-Ranked-Players-Win strategy, 
but is unlikely to undermine that strategy because it changes the 
outcome only when the Lowest-Ranked player plays first. If offense 
is set randomly, maximum return might be achieved at impulse level 
of not Basic Common (53%). The maximum acceptable impulses are  
(3 - 2 odds(L) - odds(H))/(3 - 2 odds(L) - odds(M)) and  
(3 - 2 odds(L) - odds(M))/(3 - 2 odds(L) - odds(H)).

* Fallback to cooperative strategy if any opponent deviates from 
  this plan 
* Start with black in the lower left corner
* If you have rare enough impulse, and the previous player forms 
  an incomplete 3-in-a-row, then go for strategic loss (avoid 
  forming a 3-in-a-row) 


Potential Schema
----------------

