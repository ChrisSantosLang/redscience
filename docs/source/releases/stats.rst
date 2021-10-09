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
   
:math:`\text{top burst}_{a, g}` :
  The highest growth in conservative skill estimate of player 
  :math:`a` on game :math:`g`
  
.. math::
   \text{top burst}_{a, g} 
     = max \{
	   R_{a, g, 1} - R_{a, g, 0} \dots
       R_{a, g, m} - R_{a, g, m-1} \}  

:math:`\text{strategic}_(m, a)` :
  Whether the outcome of match :math:`m` seemed "strategic" for 
  player :math:`a` twenty matches later. 
  
.. math::  
   =
    \begin{cases}
      \text{Strategic}  & \quad \text{if } 
	    \displaystyle\sum_{i=(m+22)}^{m+26} \hat{\mu}_{a, g, i}
        - \displaystyle\sum_{i=(m-2)}^{m+2} \hat{\mu}_{a, g, i}
        \ge  2 \hat{\sigma}_{a, g, m+20}\\
        & \quad \text{or} \hat{\mu}_{a, g, m+20} 
	  \ge \hat{\mu}_{max, g, m+20} 
	    - \hat{\sigma}_{a, g, m+20}\\
      \text{Unstrategic}  & \quad \text{if } 
	    \displaystyle\sum_{i=(m-2)}^{m+2} \hat{\mu}_{a, g, i}
	    - \displaystyle\sum_{i=(m+22)}^{m+26} \hat{\mu}_{a, g, i}
        \ge  2 \hat{\sigma}_{a, g, m+20}
    \end{cases} 
  
:math:`\text{Random}_{a, m}` :
  True if player :math:`a` presents as random in match :math:`m`
  
.. math::  
   \text{Random}_{a, m} \text{if} 
      \hat{\mu}_{a, \text{game}_m} 
        = \hat{\mu}_{random, \text{game}_m} 
		  \pm 2 \hat{\sigma}_{a, \text{game}_m}

:math:`\text{Novice}_{a, m}` :
  True if player :math:`a` presents as a novice in match :math:`m`
  
.. math::  
   \text{Novice}_{a, m} \text{if} 
      \hat{\mu}_{a, \text{game}_m} 
        < min \{ ( min \{ \hat{\mu}_{\text{players}_m, \text{game}_m, m} \}
            + \hat{\sigma}_{a, \text{game}_m}),  
          ( max \{ \hat{\mu}_{\text{players}_m, \text{game}_m, m} \} 
		    - \hat{\sigma}_{a, \text{game}_m}) \}

If player :math:`a` is a teammate of the user (e.g. Partner), or is 
not the first on its team to play after the user, calculate the flag 
as follows instead:

.. math::  
   \text{Novice}_{a, m} \text{if} 
     \hat{\mu}_{a, \text{game}_m} 
        < \hat{\mu}_{partner, \text{game}_m} 
		  - 3 \hat{\sigma}_{a, \text{game}_m}
		  
:math:`\text{Expert}_{a, m}` :
  True if player :math:`a` presents as an expert in match :math:`m`
  
.. math::  
   \text{Expert}_{a, m} \text{if} 
      \hat{\mu}_{a, \text{game}_m} 
        > max \{ ( min \{ \hat{\mu}_{\text{players}_m, \text{game}_m, m} \}
		    + \hat{\sigma}_{a, \text{game}_m}),  
          ( max \{ \hat{\mu}_{\text{players}_m, \text{game}_m, m} \} 
		    - \hat{\sigma}_{a, \text{game}_m}) \}

If player :math:`a` is a teammate of the user (e.g. Partner), or is 
not the first on its team to play after the user, calculate the flag 
as follows instead:

.. math::  
   \text{Expert}_{a, m} \text{if} 
     \hat{\mu}_{a, \text{game}_m} 
        > \hat{\mu}_{partner, \text{game}_m} 
		  + 3 \hat{\sigma}_{a, \text{game}_m}
		  
:math:`X_m(x)` :
  The occurence of event :math:`x` in match :math:`m`. 

:math:`E_m(x)` :
  The expected probability of event :math:`x` in match :math:`m`, given 
  the skill estimates going into the match  

.. math::
   E_m(x) = P(X_m(x) \mid \{\hat{\mu}_{a, m}, 
   \hat{\sigma}_{a, m} : a \in \text{players}_m \})

:math:`\text{favor}_{a, b, m}` :
  The favor player performed by :math:`a` for player :math:`b` in match 
  :math:`m`.
  
.. math:: 
  \text{favor}_{a, b, m} = 
   \begin{cases}
    E_m(win_a) + E_m(draw) & \quad  
      \text{if player } b \text{ wins match } m \\
	- (E_m(win_b) + E_m(draw)) & \quad 
	  \text{if player } a \text{ wins match } m \\
	E_m(win_a) - E_m(win_b) & \quad 
      \text{if they draw}    
   \end{cases}  
  
:math:`\text{favors owed}_{a, b, m}` :
  The favors player :math:`a` owes player :math:`b` in match  
  :math:`m`
  
.. math::  
  \text{favors owed}_{a, b, m} = -
    \displaystyle\sum_{\substack{
      i=0 \\
      \text{game}_i = \text{game}_m }^{m} 
      \text{favor}_{a, b, i}

:math:`\text{default}_{a, b, g}` :
  Whether player :math:`a`'s debt to player :math:`b` on game 
  :math:`g` is in default
  
.. math::  
  \text{default}_{a, b, g} =
    \text{favors owed}_{a, b, m}
	> min \{ 1, max \{ \text{favors owed}_{a, b, n} : 
	  \text{game}_n = \text{game}_m, n < m \} \}

:math:`\text{debt}_{a, m}` :
  The favors owed by player :math:`a` to all other players in 
  match :math:`m`

.. math::  
   \text{debt}_{a, m} =
     \displaystyle\sum_{i \in players_m}
       \text{favors owed}_{a, i, m} 

:math:`\text{Richer}_{a, m}` :
  True if player :math:`a` presents as richer than the user in 
  match :math:`m`
  
.. math::  
   \text{Richer}_{a, m} \text{if} 
     text{debt}_{a, m} < \text{debt}_{user, m}
	 \lor ( text{debt}_{a, m} = \text{debt}_{user, m}
	   \land R_{a, text{game}_m} > R_{a, text{game}_m} )

:math:`\text{social flags}_{a, m}` :
  A set of flags describing player :math:`a` relative to the user on 
  match :math:`m`

.. math::  
   \text{social flags}_{a, m} =
    \begin{cases}
      \text{Random}          & \quad  011 & \quad\text{if } 
	    \text{Random}_{a, m}\\
      \text{Antisocial}      & \quad  111 & \quad\text{else if } 
        \exists b \in players_m \text{default}_{a, b, game_m}\\ 
      \text{Richer Novice}   & \quad  110 & \quad\text{else if } 
        \text{Richer}_{a, m} \land \text{Novice}_{a, m}\\
      \text{Richer Expert}   & \quad  101 & \quad\text{else if } 
        text{Richer}_{a, m} \land \text{Expert}_{a, m}\\
      \text{Richer}          & \quad  100 & \quad\text{else if } 
        text{Richer}_{a, m}\\
      \text{Poorer Novice}   & \quad  010 & \quad\text{else if } 
        \text{Novice}_{a, m}\\
      \text{Poorer Expert}   & \quad  001 & \quad\text{else if } 
        \text{Expert}_{a, m}\\
      \text{Poorer}          & \quad  000 & \quad\text{otherwise }
    \end{cases}


:math:`\text{win boost}_{a, b, g}` :
  The boost to player :math:`a`'s win rate on game :math:`g` in 
  the last ten matches with player :math:`b`

.. math::
   \text{win boost}_{a, b, g} = 
       \displaystyle\sum_{\substack{
         i=(n-10) \\
         game_i = g \\
         players_i \subset \{a, b\}
       }}^{n}
       \frac{X_i(win_a) - E_i(win_a)}{10}   

:math:`\text{kick back}_{a, b, g}` :
  The boost to player :math:`b`'s win rate on game :math:`g` in 
  the last ten matches with player :math:`a`
  
.. math::
   \text{kick back}_{a, b, g} = 
       \displaystyle\sum_{\substack{
         i=(n-10) \\
         game_i = g \\
         players_i \subset \{a, b\}
       }}^{n}
       \frac{X_i(win_b) - E_i(win_b)}{10}  

:math:`\text{draw boost}_{a, b, g}` :
  The boost to player :math:`a`'s draw rate on game :math:`g` in 
  the last ten matches with player :math:`b`
  
.. math::
   \text{draw boost}_{a, b, g} = 
       \displaystyle\sum_{\substack{
         i=(n-10) \\
         game_i = g \\
         players_i \subset \{a, b\}
       }}^{n}
       \frac{X_i(draw) - E_i(draw)}{10}  
 
:math:`\text{preference}_{a, b, g}` :
  Player :math:`a`'s preference to play with player :math:`b` on 
  game :math:`g`
  
.. math::
   \text{preference}_{a, b, g} = 
   \text{draw_boost}_{a, b, g} +
   2 (\text{win_boost}_{a, b, g})
 
:math:`\text{relative rating}_{a, b, g}` :
  The relative skill rating of player :math:`b` on game :math:`g`, 
  compared to player :math:`a` 
  
.. math::
   \text{relative rating}_{a, b, g} = 
    \frac{R_{b, g}}
     {R_{a, g}} 
    - 1

Acceptance Test Plan
--------------------

Test each of the clickable elements. Play the Random players against 
each other for at least 20 games and confirm that Rating Diff, 
Win Boost, Draw Boost, Kick Back are small. Play against them in a 
favoring way, letting one win and making the other lose and confirm 
that you can detect the favoritism. Close Python and reopen it to 
confirm that it remembers the stats.

Potential Mockups
-----------------


 .. figure:: images/Favoritism.png

   (but the checkboxes, “Document Social History” and “Profile 
   Selected Players” buttons (fa-bar-chart) do not display until 
   version 1.6). 

* The game dropdown offers one option for each combination of 
  game this player has played and form of augmentation used. 
* The rows are sorted by Last Match (most recent on top). The 
  “Sort by this Column” buttons re-display the table sorted by 
  the values in the associated column; if already sorted by that 
  column, reverse the order.
* The “Show Player” buttons (fa-address-card-o) save the record 
  and navigate to the Stats tab of the associated Player.
* The Relative Rating numbers are “Show Evolution” buttons which 
  save the current record and navigate to the Evolution Page with 
  the selected rule set and “Rating” selected for both the player 
  and the associated other player.
  
   .. figure:: images/LearningCurve.png

   (but the title is “Recorded Tic-Tac-Toe”, and Rating is the only 
   score option until version 1.6, the “Profile Selected Players” 
   button (fa-bar-chart) does not display until version 1.6, and 
   “Show Game Tree” buttons (fa-sitemap) do not show until version 
   1.10)

* The player combobox offers all players. If the selected game is 
  not available for the new player, then select the first game 
  available for the new player. 
* The game combobox offers all games played by the selected player.  
  Selecting a game adds the curve to the graph.
* The score select offers only “Rating” for now, the title is 
  “Rating History”, and the x-axis is observed to date.
* The “Add Curve” button (fa-plus) inserts an identical row (same 
  player, rule_set, and score) with its own “Add Curve” button, 
  and replaces itself with a “Delete Curve” button. If multiple 
  curves display, also display a legend.
* The “Delete Curve” button (fa-trash-o) removes that row (and 
  adds an “Add Curve” button to the last).
