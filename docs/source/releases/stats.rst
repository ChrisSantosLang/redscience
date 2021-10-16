======================
1.3 Ranked Tic-Tac-Toe
======================

Requirements
------------

Maintain a saved record of each match (the game played, who played, 
their forms of augmentation, the outcome), and of each choice made 
during the match. Allow users to see game stats per form of augmentation 
for each player (time since the player last played, number of matches 
played, % won, % draw, and average time to finish their turn). For 
example, Lora's win rate at Tic-Tac-Toe when reviewing.

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

To get CSV of moves::

  redscience moves tic-tac-toe {file}
  
To get CSV of stats::

  redscience player {name} -s {file}
  
To get CSV of favoritism::

  redscience player {name} -f {file}

Favoritism Tab
~~~~~~~~~~~~~~

 .. figure:: images/Favoritism.png

   Shown as of :doc:`recorded` (to show the evolution of the page).
   The checkboxes, "Document Social History” button, and “Profile 
   Selected Players” button do not display until :doc:`educated`. 

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
 
Evolution Page
~~~~~~~~~~~~~~

   .. figure:: images/LearningCurve.png

   Shown as of :doc:`corp` (to show the evolution of the page). 
   The “Profile Selected Players” button (fa-bar-chart) and score
   options other than "Rating" apear in :doc:`educated`, and 
   “Show Game Tree” buttons (fa-sitemap) show only for members of
   a Team or Corp (:doc:`team`)

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


Formulae
--------

Skill Rating
~~~~~~~~~~~~

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

:math:`\text{relative rating}_{a, b, g}` :
  The relative skill rating of player :math:`b` on game :math:`g`, 
  compared to player :math:`a` 
  
.. math::
   \text{relative rating}_{a, b, g} = 
    \frac{R_{b, g}}
     {R_{a, g}} 
    - 1


Stategic Outcomes
~~~~~~~~~~~~~~~~~

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
        & \quad \text{or } \hat{\mu}_{a, g, m+20} 
	  \ge \hat{\mu}_{max, g, m+20} 
	    - \hat{\sigma}_{a, g, m+20}\\
	    \\
      \text{Unstrategic}  & \quad \text{if } 
	    \displaystyle\sum_{i=(m-2)}^{m+2} \hat{\mu}_{a, g, i}
	    - \displaystyle\sum_{i=(m+22)}^{m+26} \hat{\mu}_{a, g, i}
        \ge  2 \hat{\sigma}_{a, g, m+20}
    \end{cases} 


Favoritism
~~~~~~~~~~

:math:`X_m(x)` :
  The occurence of event :math:`x` in match :math:`m`. 

:math:`E_m(x)` :
  The expected probability of event :math:`x` in match :math:`m`, given 
  the skill estimates going into the match  

.. math::
   E_m(x) = P(X_m(x) \mid \{\hat{\mu}_{a, m}, 
   \hat{\sigma}_{a, m} : a \in \text{players}_m \})
   
:math:`\text{win boost}_{a, b, g}` :
  The boost to player :math:`a`'s win rate on game :math:`g` in 
  the last ten matches with player :math:`b`

.. math::
   :name: win boost
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
   \text{draw boost}_{a, b, g} +
   2 (\text{win boost}_{a, b, g})

:math:`\text{favor}_{a, b, m}` :
  The favor player performed by :math:`a` for player :math:`b` in match 
  :math:`m`.
  
.. math:: 
  \text{favor}_{a, b, m} = 
   \begin{cases}
    E_m(win_a) + E_m(draw) & \quad  
      \text{if player } b \text{ wins match } m \\
	- E_m(win_b) - E_m(draw) & \quad 
	  \text{if player } a \text{ wins match } m \\
	E_m(win_a) - E_m(win_b) & \quad 
      \text{if they draw}    
   \end{cases}  
  
:math:`\text{favors owed}_{a, b, m}` :
  The favors player :math:`a` owes player :math:`b` in match  
  :math:`m`
  
.. math::  
  \text{favors owed}_{a, b, m} =
    \displaystyle\sum_{\substack{
      i=0 \\
      \text{game}_i = \text{game}_m }}^{m} 
      \text{favor}_{b, a, i}

:math:`\text{default}_{a, b, g}` :
  Whether player :math:`a`'s debt to player :math:`b` on game 
  :math:`g` is in default
  
.. math::  
  \text{if }
    \text{favors owed}_{a, b, m}
	> min \{ 1, max \{ \text{favors owed}_{a, b, n} : 
	  \text{game}_n = \text{game}_m, n < m \} \}


Social Flags
~~~~~~~~~~~~

:math:`\text{Random}_{a, m}` :
  True if player :math:`a` presents as random in match :math:`m`
  
.. math::  
   \text{ if } 
      \hat{\mu}_{a, \text{game}_m} 
        = \hat{\mu}_{random, \text{game}_m} 
		  \pm 2 \hat{\sigma}_{a, \text{game}_m}

:math:`\text{Novice}_{a, m}` :
  True if player :math:`a` presents as a novice in match :math:`m`
  
.. math::  
   \text{ if } 
      \hat{\mu}_{a, \text{game}_m} 
        < min \{ & ( min \{ \hat{\mu}_{\text{players}_m, \text{game}_m, m} \}
            + \hat{\sigma}_{a, \text{game}_m}),  \\
          & ( max \{ \hat{\mu}_{\text{players}_m, \text{game}_m, m} \} 
		    - \hat{\sigma}_{a, \text{game}_m}) \}

If player :math:`a` is a teammate of the user (e.g. Partner), or is 
not the first on its team to play after the user, calculate the flag 
as follows instead:

.. math::  
   \text{ if } 
     \hat{\mu}_{a, \text{game}_m} 
        < \hat{\mu}_{partner, \text{game}_m} 
		  - 3 \hat{\sigma}_{a, \text{game}_m}
		  
:math:`\text{Expert}_{a, m}` :
  True if player :math:`a` presents as an expert in match :math:`m`
  
.. math::  
   \text{ if } 
      \hat{\mu}_{a, \text{game}_m} 
        > max \{ & ( min \{ \hat{\mu}_{\text{players}_m, \text{game}_m, m} \}
		    + \hat{\sigma}_{a, \text{game}_m}), \\ 
          & ( max \{ \hat{\mu}_{\text{players}_m, \text{game}_m, m} \} 
		    - \hat{\sigma}_{a, \text{game}_m}) \}

If player :math:`a` is a teammate of the user (e.g. Partner), or is 
not the first on its team to play after the user, calculate the flag 
as follows instead:

.. math::  
   \text{ if } 
     \hat{\mu}_{a, \text{game}_m} 
        > \hat{\mu}_{partner, \text{game}_m} 
		  + 3 \hat{\sigma}_{a, \text{game}_m}

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
   \text{ if } 
     & \text{debt}_{a, m} < \text{debt}_{user, m} \\
     & \text{ or } ( (\text{debt}_{a, m} = \text{debt}_{user, m})
	   \text{ and } (R_{a, text{game}_m} > R_{user, text{game}_m} ))

:math:`\text{social flags}_{a, m}` :
  A set of flags describing player :math:`a` relative to the user on 
  match :math:`m`

.. math::  
   =
    \begin{cases}
      011 \text{ Random}  & \quad\text{if } 
	\text{Random}_{a, m}\\
      111 \text{ Antisocial} & \quad\text{else if } 
        \text{default}_{a, user, game_m}\\ 
      110 \text{ Richer Novice} & \quad\text{else if } 
        \text{Richer}_{a, m} \text{ and } \text{Novice}_{a, m}\\
      101 \text{ Richer Expert} & \quad\text{else if } 
        \text{Richer}_{a, m} \text{ and } \text{Expert}_{a, m}\\
      100 \text{ Richer} & \quad\text{else if } 
        \text{Richer}_{a, m}\\
      010 \text{ Poorer Novice} & \quad\text{else if } 
        \text{Novice}_{a, m}\\
      001 \text{ Poorer Expert} & \quad\text{else if } 
        \text{Expert}_{a, m}\\
      000 \text{ Poorer} & \quad\text{otherwise }
    \end{cases}



Potential Schema
----------------

matches: PRIMARY KEY is match_id::

  match_id int NOT NULL AUTO_INCREMENT
  created_ts timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
  creator_id  int NOT NULL FOREIGN KEY(players.player_id)
  game_id int NOT NULL FOREIGN KEY (games.game_id)
  player1_id int NOT NULL FOREIGN KEY(players.player_id) (player order by id)
  player1_tool_cat tintyint NOT NULL DEFAULT 0
  player1_outcome_cat tintyint NOT NULL DEFAULT 0
  player1_mu int NOT NULL DEFAULT 0
  player1_sigma int NOT NULL DEFAULT 0
  player2_id int NOT NULL FOREIGN KEY(players.player_id)
  player2_tool_cat tintyint NOT NULL DEFAULT 0
  player2_outcome_cat tintyint NOT NULL DEFAULT 0
  player2_mu int NOT NULL DEFAULT 0
  player2_sigma int NOT NULL DEFAULT 0
  player3_id int FOREIGN KEY(players.player_id)
  player3_tool_cat tintyint NOT NULL DEFAULT 0
  player3_outcome_cat tintyint NOT NULL DEFAULT 0
  player3_mu int NOT NULL DEFAULT 0
  player3_sigma int NOT NULL DEFAULT 0
  player4_id int FOREIGN KEY(players.player_id)
  player4_tool_cat tintyint NOT NULL DEFAULT 0
  player4_outcome_cat tintyint NOT NULL DEFAULT 0
  player4_mu int NOT NULL DEFAULT 0
  player4_sigma int NOT NULL DEFAULT 0
  draw_fl bool NOT NULL DEFAULT 0
  duration time NOT NULL DEFAULT 0
  move_tally int NOT NULL DEFAULT 0
  real_match_id FOREIGN KEY(games.match_id)
  explorer_id int FOREIGN KEY(players.player_id)
  taught_fl bool NOT NULL DEFAULT 0

  INDEX game_id, player1_id, player2_id, player3_id, player4_id, match_id

moves: PRIMARY KEY is match_id, move_num::

  match_id int NOT NULL FOREIGN KEY(games.match_id)
  move_num int NOT NULL AUTO_INCREMENT
  created_ts timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP 
  creator_id  int NOT NULL FOREIGN KEY(players.player_id)
  game_id int NOT NULL FOREIGN KEY (games.game_id)
  decision_interval int NOT NULL DEFAULT 0
  to_spot int NOT NULL DEFAULT 0
  rel_color_cat tinyint NOT NULL DEFAULT 0 (player color, next color,…)
  shape_cat tinyint NOT NULL DEFAULT 0 
  from_spot int NOT NULL DEFAULT 0
  outcome_cat tinyint NOT NULL DEFAULT 0 
  predicted_outcome_cat tintyint NOT NULL DEFAULT 0 
	
  UNIQUE INDEX creator_id, created_ts, outcome_cat, predicted_outcome_cat
  INDEX match_id

stats: PRIMARY KEY is player_id, aug_cat , game_id::

  player_id int NOT NULL FOREIGN KEY(players.player_id)
  tool_cat tinyint (review, debate, etc)
  game_id int NOT NULL FOREIGN KEY (games.game_id)
  created_ts timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
  creator_id  int NOT NULL FOREIGN KEY(players.player_id)
  last_match_ts timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
  played_tally int NOT NULL DEFAULT 0
  won_tally int NOT NULL DEFAULT 0
  lost_tally int NOT NULL DEFAULT 0
  decision_interval_tally int NOT NULL DEFAULT 0
  rating_mu int NOT NULL DEFAULT 0
  rating_sigma int NOT NULL DEFAULT 0
  top_burst int NOT NULL DEFAULT 0
  explore_tally int NOT NULL DEFAULT 0
  critic_tally int NOT NULL DEFAULT 0

  INDEX player_id
  UNIQUE INDEX game_id, rating_mu, player_id 

favor_stats: PRIMARY KEY is player1_id, player1_tool_cat, player2_id, player2_tool_cat game_id::

  player1_id int NOT NULL FOREIGN KEY(players.player_id)
  player1_tool_cat tintyint NOT NULL DEFAULT 0
  player2_id int NOT NULL FOREIGN KEY(players.player_id)
  player2_tool_cat tintyint NOT NULL DEFAULT 0
  game_id int NOT NULL FOREIGN KEY (games.game_id)
  created_ts timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
  creator_id  int NOT NULL FOREIGN KEY(players.player_id)
  last_match_ts timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
  played_tally int NOT NULL DEFAULT 0
  win_boost float 
  kick_back float
  draw_boost float
  preference float
  debt float
  debt_default_fl bool NOT NULL DEFAULT 0

  INDEX player_id
  
Hints
-----

Rotation
~~~~~~~~

::

  def rotated(label):
    return widgets.HTML(value='''
      <p style='
        writing-mode: vertical-lr; 
        transform: rotate(180deg);
        display: inline-block;
      '>''' + label + "</p>")

  widgets.HBox([rotated("Hello1"), rotated("Hello2")])
