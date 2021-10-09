======================
1.5 Remote Tic-Tac-Toe
======================

Requirements
------------

Modify the Secure Tic-Tac-Toe program to permit users to play against 
each other through simultaneously logged-in accounts.

Give each Creator the ability to invite other Creators to be their 
friend and to accept friend invitations. Add confirmed friends to the 
list of players they can invite to play Tic-Tac-Toe (as well as a 
"Next available human" option). 

Acceptance Test Plan
--------------------

Test by opening two browser windows and logging into a separate 
account on each.  Test each of the clickable elements and test that 
it displays appropriate errors for invalid entries. Play the two 
accounts against each other.

Potential Mockups
-----------------

Friends Tab
~~~~~~~~~~~

 .. figure:: images/Friends.png

* The “Show Player” buttons (fa-address-card-o) save the record 
  and navigate to the Stats tab of the associated Player
* The “Accept Friend Request” button (fa-check) moves the player to 
  the friends list (below combobox)
* The “Ban Friend Requests” button (fa-ban) moves the player to the 
  banned list (below friends)
* The “Add to Friends” button (fa-user-plus) sends a friend request 
  to the selected player
* The “Revoke Ban” button (fa-ban) moves the player to the fiends 
  list 

Potential Schema
----------------

friend_requests: PRIMARY KEY is invitor_id, invited_id::

	creator_id  int NOT NULL FOREIGN KEY(players.player_id)
	invited_id int NOT NULL FOREIGN KEY(players.player_id)
  created_ts timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
  request_status tinyint NOT NULL DEFAULT 0

  INDEX creator_id
  INDEX invited_id


play_invites: PRIMARY KEY is player_id::

	creator_id  int NOT NULL FOREIGN KEY(players.player_id)
  created_ts timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
  game_id int NOT NULL FOREIGN KEY (games.game_id)
  player2_cat tinyint NOT NULL DEFAULT 0
  player2_id int FOREIGN KEY(players.player_id)
  player3_cat tinyint NOT NULL DEFAULT 0
  player3_id int FOREIGN KEY(players.player_id)
  player4_cat tinyint NOT NULL DEFAULT 0
  player4_id int FOREIGN KEY(players.player_id)
