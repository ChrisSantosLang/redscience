==============
1.7 Batch Play
==============

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

Create and play 4P-Blind-TTT, TheoryOfMind, 3P-NeedyPoker, and 3P-RichPoker.

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

Game Definitions
----------------

Test Set
~~~~~~~~

4P-Blind-TTT:
  Partners, Partners share color, All spaces cloaked and dealt, 
  Cloaking hides, Deck: [{ O3 O4 S S S S S S S }] “1 black circle, 
  1 white circle, 7 blanks” 72 variations

TheoryOfMind:
  6x1x4 posts: first stack locked and starts with 3 black dealt 
  pieces, second stack exclusive to black and starts with white, 
  pink and yellow dealt pieces, third stack locked, fourth stack 
  exclusive to white and starts with pink, yellow, and black dealt 
  pieces, fifth stack exclusive to pink and starts with yellow, 
  black, and white dealt pieces, sixth stack exclusive to pink and 
  starts with yellow, black, and white dealt pieces;
  4 Player, 4-same-shape-in-a-row wins, Adjacent mixed shapes loses, 
  Cloaking obscures;
  Circle: 1 black, 1 white, 1 pink, and 1 yellow start in reserve; 
  Pentagon: 1 black, 1 white, 1 pink, and 1 yellow start in reserve; 
  X: 1 black, 1 white, 1 pink, and 1 yellow start in reserve; 
  Option to pass, second, fourth, fifth, and sixth stacks cloaked;
  Deck: [{ [{ [OOO], [XXX], [PPP], [PPP], [PPP] }], [{ [OOO], 
  [XXX], [XXX], [PPP], [PPP] }], [{ [OOO], [XXX], [XXX], [XXX], 
  [PPP] }], [{ [OOO], [OOO], [XXX], [PPP], [PPP] }], [{ [OOO], 
  [OOO], [XXX], [XXX], [PPP] }], [{ [OOO], [OOO], [OOO], [XXX], 
  [PPP] }] }] “All three shapes are on the board, no mixed groups” 
  1020 variations

3P-NeedyPoker:
  8x1x26 stacks: first stack exclusive to black and starts with 5 
  black circles, second stack exclusive to black and starts with 
  2 black dealt pieces, third stack exclusive to white and starts 
  with 5 white circles, fourth stack exclusive to white and starts 
  with 2 white dealt pieces, fifth stack exclusive to pink and 
  starts with 5 pink circles, sixth stack exclusive to pink and 
  starts with 2 pink dealt pieces, seventh stack sticky and starts 
  with 5 common dealt pieces and 1 pink circle, eigth stack 
  exclusive to chaos; 3 vs chaos, Cloaking obscures, Most pieces 
  wins; Less-than-most committed pieces folds
  Circle: Moves orthogonal by stack, 15 yellow start in reserve;
  Pentagon: Moves orth by full stack, Can Capture, Cover by rank, 
  Converts captive(s); 
  X: Moves orth by full stack, Can Capture, Cover by rank, 
  Converts captive(s); 
  Cross: Moves orth by full stack, Can Capture, Cover by rank,
  Converts captive(s); 
  Triangle: Moves orth by full stack, Can Capture, Cover by rank, 
  Converts captive(s); 
  Star: Moves orth by full stack, Can Capture, Cover by rank, 
  Converts captive(s); 
  Phase 1: Option to pass, chaos locked, second, fourth and sixth 
  posts locked and cloaked, bottom five spaces of the seventh post 
  are cloaked;
  Phase 2: Option to pass; chaos locked; second, fourth and sixth 
  posts locked and cloaked, bottom two spaces of the seventh post 
  are cloaked;
  Phase 3: Option to pass; chaos locked; second, fourth and sixth 
  posts locked and cloaked, bottom space of the seventh post is 
  cloaked;
  Phase 4: Option to pass; chaos locked; second, fourth and sixth 
  posts locked and cloaked;
  Phase 5: Single, chaos locked, first, third and fifth posts 
  locked;
  Phase 6: Single, Option to pass, only chaos unlocked, seventh 
  stack locked;
  Deck:[{ PPPP **** ++++ XXXX ^^^^ }] “4 pentagons, 4 Xs, 4 
  crosses, 4 triangles, and 4 starts in deck ”. 

3P-RichPoker:
  (Same as 3P-NeedyPoker 6 yellow circles start in reserve instead of 15)


Other interesting games
~~~~~~~~~~~~~~~~~~~~~~~

KPoker:
  6x1x6 stacks: first stack exclusive to black and starts with 1 
  black circle, second stack exclusive to black and starts with 
  1 black dealt piece, third stack exclusive to white and starts 
  with 1 white circle, fourth stack exclusive to white and starts 
  with 1 white dealt piece, fifth stack sticky and starts 
  with 1 black circle and 1 white circle, sixth stack 
  exclusive to chaos;
  2 vs chaos, Cloaking obscures, Most pieces wins, Less-than-most 
  committed pieces folds; 
  Circle: Moves orthogonal by stack, 4 yellow start in reserve;
  Pentagon: Moves orth by full stack, Can Capture, Cover by rank, 
  Converts captive(s); 
  X: Moves orth by full stack, Can Capture, Cover by rank, 
  Converts captive(s); 
  Cross: Moves orth by full stack, Can Capture, Cover by rank, 
  Converts captive(s);
  Phase 1: Option to pass, chaos locked, second and fourth posts 
  locked and cloaked; 
  Phase 2: Single, chaos locked, first and third stacks locked;
  Phase 3: Option to pass, only chaos unlocked, fifth stack locked;
  Deck:[{ P+X }] “1 pentagon, 1 X, and 1 cross in deck”.  

BeerQuiche60:
  4x1x5 posts: first stack exclusive to black and starts with 
  1 black dealt piece, second stack exclusive to white and starts 
  with 2 black dealt pieces, third stack exclusive to white and 
  starts with 1 white pentagon, fourth stack exclusive to chaos; 
  2-vs-chaos, Cloaking obscures, Most 2-same-color-and-kind-in-a-row wins; 
  Circle: 1 black and 5 yellow in reserve;
  Pentagon: Can capture, Cover by rank, Reincarnates captive(s) x2, 
  1 black and 1 white start in reserve; 
  Phase 1: Single, chaos locked;
  Phase 2: only white unlocked, second post locked; 
  Phase 3: Option to pass, only chaos unlocked; 
  Deck: [{ [OOOOOOOOOO], [OOOOOOOOOO], [PPPPPPPPPP], [PPPPPPPPPP], 
  [PPPPPPPPPP] }] “2 circle dectets and 3 pentagon dectets” 2 variations

Potential Schema
----------------
