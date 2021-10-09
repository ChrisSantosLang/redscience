========================
1.2 Recorded Tic-Tac-Toe
========================

Requirements
------------

Modify the GUI Tic-Tac-Toe program to allow users to select players 
to play Tic-Tac-Toe. Maintain a saved record of each player 
including name, avatar, type, security, and Universe (for now, all 
players will have Universe = ”Public Universe”; security will be 
"Admin" if type is Human and None if type is "Random").



Random
~~~~~~

When a player of Type - Random is playing (or augmenting) a turn, 
compile a list of all legal sets of moves for that turn for each piece, 
counting each reserve piece individually, then pick randomly from that 
list. For example, if Random had two black circles and one white triangle 
in reserve, and could pass, and there were two empty spaces in which 
Random could play (“A” and “B”), then Random would choose “White 
triangle To A” 1/7th of the time, “White triangle To B” 1/7th of the 
time, “Black circle To A” 2/7th of the time, “Black circle To B” 
2/7th of the time, and “Pass” 1/7 of the time.  

Review and Delegate
~~~~~~~~~~~~~~~~~~~

Permit each user to be augmented by a non-human 
player (just "Random" for now). If the timer runs out before the user 
confirms a move-selection, then the non-human makes the move; if the 
type of augmentation is “Reviewing” then the non-human player prefills 
the move for the user (but the user can change it), if the type of 
augmentation is “Delegating” then the non-human does not prefill the 
move (but the user can expire the clock early by clicking accept 
without selecting a move). 
 
Acceptance Test Plan
--------------------

Test each of the clickable elements and test that it displays 
appropriate errors for invalid entries. Create at least three 
Random players. Play all three forms of augmentation against Random. 
To test that a Random player does not settle on predictable behavior, 
undo and repeat to see that it plays differently. Close Python and reopen 
it to confirm that it remembers the players names, avatars, types, 
and security.

Potential Mockups
-----------------

To read player data from command line (not email address)::

  redscience player name
  
  
Player Page
~~~~~~~~~~~

.. figure:: images/Player.png

   Shown as of :doc:`stats` Version (to anticipate the evolution of 
   the page). The tabs and their contents do not display in the current 
   version.


* When the user is the creator or an Admin, clicking the Avatar 
  navigates to the AI Avatar page for AI players or to the Team 
  Avatar page other types of players.
* The name text field does not accept whitespace, ‘*’, ‘(‘, or ‘)’.
* The “Copy Player” button (fa-files-o) saves the current record and 
  opens a Player page for a new player (Persona if copied from a 
  Human player). 
* For Persona and other non-human players, display the player type 
  (disabled after first save) instead of security level, and universe
  (disabled after first save) instead of email. Hide email unless the 
  user is the owner of the email or is an admin. 

* The stats table is sorted by Last Match (most recent on top). For 
  human players, display the type of augmentation with the rules 
  (A=Alone, B=Debating, D=Delegating, R=Reviewing). The “Sort by 
  this Column” buttons re-display the table sorted by the values in 
  the associated column; if already sorted by that column, reverse 
  the order.
* The “Play New Game” buttons (fa-fort-awesome) save the current 
  record and navigate to the Home Page with the associated game
  and this player prefilled. It displays only for non-human players, 
  friends, and personas created by the user.
* The Rating, Accuracy, F1, Long-Game, Teach, and Empath numbers 
  are “Show Evolution” buttons which save the current record and 
  navigate to the Evolution Page with this player, the associated 
  game (and augmentation) and score selected. The rating displays 
  a conservative estimate, but displays in bold if within a 
  standard deviation of the maximum rating for that game among all 
  player/augmentation combinations.
* The Favoritism numbers are “Show Favoritism” buttons which 
  navigate to the Favoritism tab with the associated game (and 
  augmentation) selected.
  
Team Avatar Page
~~~~~~~~~~~~~~~~
   
 .. figure:: images/HumanSelect.png

   Clicking an Avatar navigates back to the player page with the 
   avatar replaced with the selected avatar
   

Potential Schema
----------------

players: PRIMARY KEY is player_id::

  player_id int NOT NULL AUTO_INCREMENT
  created_ts timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
  creator_id  int NOT NULL FOREIGN KEY(players.player_id)
  parent_id FOREIGN KEY(players.player_id)
  name varchar( )  NOT NULL
  universe varchar( )  NOT NULL
  avatar int NOT NULL
  type_cat int NOT NULL (cannot change)
  security_cat int 
  status_cat int NOT NULL (logged-out, playing, waiting, browsing)
  email_ad varchar( )
  ts_last_login timestamp
  recent_game_selections
  recent_player_selections
  algorithm_json varchar( )
  cont_learn_fl int
  introspection_depth int
  team_id int FOREIGN KEY(players.player_id)
  
  UNIQUE INDEX name, universe	
  UNIQUE INDEX team_id, player_id

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
