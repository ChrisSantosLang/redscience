===============
1.7 Batch Games
===============

Requirements
------------

Modify the Various Games program to allow Admins and Trainers to 
create and run tournament plans, each composed of a name and 
computer-generated ID, plus at least one game set (which consists 
of a set of rules, a number of times to play, and a set of 
non-human players to play that many times). Until the tournament 
has been run, allow users to delete any of its game sets and to 
add copies of all game sets from another (or the same) tournament 
plan. After a tournament has been run, allow the user to view the 
results (when it ran, win rates, draw rate, duration and average 
number of moves per game), and to access the stats for each named 
player and to access the leader-board for each named set of rules. 
Also allow users to view a list of tournaments for each rule set 
(including when run, number of games, draw rate, and moves per 
game). 

From each Leaderboard and Favoritism Stats, allow users to select 
a set of players and automatically generate a tournament plan 
that consists of 100 rounds for each possible combination of 
players from that set. To qualify as a “Benchmark,” a tournament 
must be created from a Leaderboard, include the top ranked player, 
and include the Random player (after Release 10, it must include 
the “Standard” player for that game). For each player, automatically 
add the player it most prefers for that game. To qualify as “Social,”
a tournament must be created from Favoritism Stats, include the R
andom player, and include at least one player with Win Boost, Draw 
Boost, or Kick Back over 7%. 

Do not display game play while a tournament is running, but do add 
the games to the record and update player stats. Instead of running 
an entire set at a time, alternate between sets. For example in a 
Tic-Tic-Toe tournament between Player A, Player B, and Random, after 
A plays B, have each player play against Random before they play 
each other again. This will prevent normalization of ratings during 
favoritistic play.

Decks
~~~~~

Make it easier to generate games with exogenous uncertainty by 
permitting game creators to select a “deck” for that game and to 
place “dealt “ pieces for each player (or for no specific player) 
in the starting  configuration. At the start of each match, the 
deck will be assembled (including any shuffling), then the 
placed “dealt” pieces will be replaced top-to-bottom then 
left-to-right with items from the deck top-to-bottom. If the 
dealt piece is for a specific player, then convert it to that 
player’s color when placing.


Acceptance Test Plan
--------------------

Test each of the clickable elements and test that it displays 
appropriate errors for invalid entries. Before running 
tournaments, jot down the ratings of the players; afterwards, 
confirm that the sum of the ratings did not change. Run each 
of these tournaments on distinct Random players:

* Random Tic-Tac-Toe 500: Five sets of 100 games of 
  Tic-Tac-Toe between Random and itself
* Random 3on15line 500: Five sets of 100 games of 3on15line 
  between between Random and itself
* Random 3on5sq 500: Five sets of 100 games of 3on5sq between 
  between Random and itself
* Random 3-player-Notakto: Five sets of 100 games between 
  between Random and itself and itself  
* Random 3-player-Misere-Notakto: Five sets of 100 games 
  between Random and itself and itself  

Note the deviation in win rates, numbers of moves, and times taken to play.  

Create and play these games: 

4P-Blind-TTT:
  Partners, Cloaking hides, all spaces cloaked and dealt. Deck: [{ O3 O4 S S S S S S S }] “Each team starts with one circle placed at random” 72 variations )
TheoryOfMind (9x1x4 posts; cloaking obscures; all posts are cloaked except the first which is locked to all players; the second, fourth, sixth and eighth posts are wall; the third, fifth, seventh and ninth posts are locked to all but the first four players respectively, 4 players, 4-same-shape-in-a-row wins, adjacent mixed shapes loses, the first player starts with 3 dealt pieces on the first post and 1 on the fifth, seventh and ninth posts; the second player starts with 1 dealt piece on the third, seventh and ninth posts; the third player starts with 1 dealt piece on the third, fifth and ninth posts; the fourth player starts with 1 dealt piece on the third, fifth and seventh posts. Option to pass . Deck: [{ [{ [OOO], [XXX], [PPP], [PPP], [PPP] }], [{ [OOO], [XXX], [XXX], [PPP], [PPP] }], [{ [OOO], [XXX], [XXX], [XXX], [PPP] }], [{ [OOO], [OOO], [XXX], [PPP], [PPP] }], [{ [OOO], [OOO], [XXX], [XXX], [PPP] }], [{ [OOO], [OOO], [OOO], [XXX], [PPP] }] }] “All three shapes are on the board, no mixed groups” 1020 variations) 
3P-NeedyPoker (8x1x26 stacks; cloaking obscures; the first two posts are locked to all but exit by the first player, and similar for the second and third two posts and the second and third player; the seventh post is locked to chaos and locked against exit; the eighth post is locked to all but chaos, the second, fourth and sixth posts are cloaked, 3 vs chaos, Most pieces wins; Less-than-most committed pieces folds. 5 community pieces are dealt to the seventh post; the first two players start with 5 circles in the first and third posts respectively; the third player starts with 4 circles on the fifth post and 1 on the seventh post; the first three players start with 2 dealt pieces on the second, fourth and sixth post respectively, chaos starts with 15 circles in reserve, circle moves unlimited orthogonal by stack; other pieces move unlimited orthogonal by full stack and convert on cover by rank. Deck:[{ PPPP **** ++++ XXXX ^^^^ }] “4 from each of 5 ranks in deck”. Phase 1 “Pre-flop”: Option to pass; chaos cannot move; second, fourth and sixth posts are locked; bottom five spaces on the seventh post are cloaked. Phase 2 ”Flop”: Option to pass; chaos cannot move; second, fourth and sixth posts are locked; bottom two spaces on the seventh post are cloaked. Phase 3 “Turn”: Option to pass; chaos cannot move; second, fourth and sixth posts are locked; bottom space on the seventh post is cloaked. Phase 4 “River’: Option to pass; chaos cannot move; second, fourth and sixth posts are locked. Phase 5 “Showdown”: Single; chaos cannot move; first, third and fifth posts are locked. Phase 6 “chaos”: single; Option to pass; only chaos can move.)
3P-RichPoker (Same as 3P-NeedyPoker but chaos starts with 6 circles in reserve instead of 15)


Other interesting games
~~~~~~~~~~~~~~~~~~~~~~~

KPoker (6x1x6 stacks; cloaking obscures; the first two posts are locked to all but exit by the first player, and similar for the second two posts and the second player; the fifth post is locked to chaos and locked against exit; the sixth post is locked to all but chaos, the second and fourth posts contain 1 cloaked space on 5 wall pieces each, 2 vs chaos, Most pieces wins, the first two players start with 1 circle in the first and third posts respectively, 1 circle each on the fifth post, and 1 dealt piece on the second and fourth posts respectively, chaos starts with 4 circles in reserve, circle moves unlimited orthogonal by stack; other pieces move unlimited orthogonal by full stack and convert on cover by rank. Deck:[{ P+X }] “Obscured pieces dealt from a shuffled deck of one pentagon, cross and X each”. Phase 1 “Bet”: Option to pass; Less-than-most committed pieces folds; chaos cannot move; second and fourth posts are locked. Phase 2 “Showdown”: Single; chaos cannot move; first and third posts are locked. Phase 3 “chaos”: Option to pass; only chaos can move.) 
BeerQuiche60 (4x1x5 posts; cloaking obscures; the bottom space of the first post and bottom two spaces of the second post are cloaked; the first and last posts are locked to all but the first player and chaos respectively, the others are locked to all but the second player, 2-vs-chaos, Most 2-same-color-and-kind-in-a-row wins, the first player starts with 1 dealt piece on the first post, two dealt pieces on the second post, 1 circle in reserve and 1 pentagon in reserve; the second player starts with 1 pentagon on the third post and 1 in reserve; chaos starts with 5 circles in reserve; pentagon reincarnates (x2) on cover. Phase 1 “Play”: Single; chaos cannot play. Phase 2 “Collect”: Only player 2 can play; second post is locked. Phase 3 “chaos”: Option to pass; only chaos can play. Deck: [{ [OOO], [OOO], [PPP], [PPP], [PPP] }] “60% chance that all obscured pieces are pentagons; otherwise they are all circles” 2 variations)


Potential Mockups
-----------------

To run tournament from CSV::

  redscience tournament {file} {security token}
  

Tournament Factory Page
~~~~~~~~~~~~~~~~~~~~~~~

 .. figure:: images/TournamentFactory.png

* The image is widgets.HTML(value="<i class='fa fa-trophy fa-5x 
  text-warning'></i>")
* The “Copy Tournament” button (fa-files-o) is available to 
  Trainers and Admins. It saves the current record and opens a 
  new (not yet run) Tournament page with same tournment_type, 
  games, players, and numbers of matches to play. Any editing of 
  players, rules or number of matches changes the tournament_type 
  to “Other”. 
* The “Start Tournament” button (fa-flag-checkered) saves the 
  current record, disables the display, and runs the tournament 
  (showing results for each part when run). The display is 
  reenabled when the tournament has been run (or when the user 
  selects “Abort”). 
* The “Study” combobox and button (fa-graduation-cap) becomes 
  available to Trainers and Admins in :doc:`educated`. It saves 
  the current record, opens the Curriculum of the player selected 
  in the combobox, and adds Tournament to the Curriculum (use 
  back button to undo). Default the combobox to the study option 
  most recently selected by the user.
* The “Delete from Tournament” button (fa-trash-o) removes that 
  game (and players) from the page. 
* The “Add to Tournament” button (fa-plus) adds the rules sets, 
  players, and numbers of matches to play from the selected in the 
  Tournament combobox. Default the Tournament combobox to the 
  Tournament most recently selected by the user. 
 
Tournaments Tab
~~~~~~~~~~~~~~~

 .. figure:: images/Tournaments.png

  Shown as of :doc:`introspection` when Debates column is added
 
* Show no more than 20 most recent Tournaments in Universe most 
  recently selected by user. Sort most recent to top.
* The “Show Tournament” button (fa-trophy) saves the current 
  record and opens the associated tournament 


Potential Schema
----------------

