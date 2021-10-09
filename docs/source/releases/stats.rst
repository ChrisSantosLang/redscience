===========================
1.3 Statistical Tic-Tac-Toe
===========================

Requirements
------------

Maintain a saved record of each match (the game played, who played, 
their forms of augmentation, the outcome), and of each choice made 
during the match. Allow users to see game stats per form of augmentation 
for each player (time since the player last played, number of matches 
played, % won, % draw, and average time to finish their turn). For 
example, Lora's win rate at Tic-Tac-Toe when reviewing.

::

  redscience player -s name

Skill Rating
~~~~~~~~~~~~

Maintain a skill-level rating estimate for each player with form of 
augmentation per game (e.g. Lora’s skill at Tic-Tac-Toe when 
reviewing), and add the conservate estimate to player stats along with 
top burst (i.e largest single-game increase in conservative estimate). To 
each record of a match, add the estimated ratings of each player before 
the match, the standard deviation in each estimate, and whether the 
outcome seemed “strategic” or “unstrategic” for each player twenty matches 
later.

At the beginning of each game, calculate skill “warning 
flags” for each player in the match. By researching play history, 
human players could get the information in these flags and could use 
it to their advantage (e.g. to cooperate across multiple matches); 
we level the playing-field by making the information available to all 
players. 

Favoritism
~~~~~~~~~~

To each record of a match, add each player’s expected probability of 
winning, and the expected probability of a draw. When maintaining skill 
level estimates, also maintain an account of favors “owed” for each pair 
of players with form of augmentation (per game). Allow users to view 
Favoritism Stats for each player, game with form of augmentation and  
partner/opponent (Win Boost, Kick Back, Draw Boost, Relative Rating, 
Preference, Favors Owed, and time since last match together.

::

  redscience player -f name

Formulae
--------

:math:`\text{game}_m`:
  The game for match :math:`m`.
  
:math:`\text{players}_m`:
  The players for match :math:`m`.
  
:math:`\hat{\mu}_{a, g}` :
  The mean skill estimate for player :math:`a` on 
  game :math:`g`. :math:`\hat{\mu}_{random, g}` is the mean skill 
  estimate for the random player, :math:`\hat{\mu}_{a, g, m}` is the 
  mean skill estimate going into match :math:`m`, and 
  \hat{\mu}_{max, g, m} is the highest skill estimate among all 
  players at that time.
  
:math:`\hat{\sigma}_{a, g}` :
  The standard deviation in the skill estimate for player 
  :math:`a` on game :math:`g`. :math:`\hat{\sigma}_{a, g, m}` is the 
  standard deviation going into match :math:`m`.
  
:math:`R_{a, g}` :
  The conservative skill estimate of player :math:`a` on 
  game :math:`g`
  
.. math::
   R_{a, g} = \hat{\mu}_{a, g} - 3 \hat{\sigma}_{a, g} 
   
:math:`TB_{a, g}` :
  The highest growth in conservative skill estimate of player 
  :math:`a` on game :math:`g`
  
.. math::
   TB_{a, g} = max \{ (R_{a, g, 1} - R_{a, g, 0}) \dots (R_{a, g, m} - R_{a, g, m-1}) \}  
