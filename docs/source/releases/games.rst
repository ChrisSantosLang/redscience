=================
1.6 Various Games
=================

Requirements
------------

Modify the Secure Tic-Tac-Toe or Remote Tic-Tac-Toe program to 
maintain saved definitions of variations on Tic-Tac-Toe, and 
permit users/AI to play those games. 

Allow each Creator to create up to fifteen new games (each game 
must differ from already saved games by more than name), and allow 
each Trainer/Admin to create an unlimited number. After a game is 
created, allow editing only of its name and only by Admins. Allow 
players to choose games to play and to view its leader-board 
(sorted with its highest rated player on top). Always display the 
Random player on leader-boards. For each player on the 
leader-board, allow users to navigate to that player's stats, 
and to initiate a game (if a friend or non-human) or send a 
friend request (if human non-friend).

Color Assignment
~~~~~~~~~~~~~~~~

Each player of normal Tic-Tac-Toe has a distinct color of pieces in 
reserve, but some variations have all players share a single color 
or share multiple colors. 

Number of Players
~~~~~~~~~~~~~~~~~

The number of players can be 2, 3, 4, “Partners” (i.e. the first 
and third player get the same outcome and the second and fourth 
player get the same outcome), “2 vs Chaos”, or “3 vs Chaos”. In 
the last two options reserves/pieces are assigned to a player 
named “Chaos” who has no stats, always goes last, and plays 
randomly. Where Chaos needs a skill-level rating (e.g. for purposes 
of updating ratings), use the constant assigned to beginning players.
If all players win, then Chaos loses (even if the number of 
players in not " ...vs chaos".

Overachiever(s) disqualified
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An “Overachiever(s) disqualified” rule may be added to 4-player games. 
If so, the first time a set of winners is identified, the players 
in that set become disqualified from winning but the game continues 
(including play by those players). For example, “First 
3-same-color-in-a-row wins” becomes “Second to get 
3-same-color-in-a-row wins” and “Most pieces wins” becomes 
“Second most pieces wins.” If all players are disqualified or lose, 
then Chaos wins. 

Cloaking, Locking, Sticky and Exclusive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rules may specify “Cloaking Type” (Invisibility or Obscurity), 
which spaces are “cloaked”, and which spaces are locked for 
entry and/or exit to specific players. "Sticky" spaces are locked
against exit; "exclusive" spaces are locked against entry or exit 
(except by player(s) to whom they are exclusive). Players cannot 
move to any space for which their entry is locked or from any space
for which their exit is locked (but can move over/through them). 
Players can fully see every piece they placed, every piece they can 
move (imobile pieces aren’t necessarily visible to the players who 
“own” them), every piece occupying a non-cloaked space, every 
piece they have previously fully seen, and every piece they have 
attempted to cover. If the Cloaking Type is Obscurity then 
players can fully see all pieces of their assigned color(s) and 
can see the color--but not shape--of all other placed pieces. If 
what makes a move illegal is a wall or piece that is invisible 
to the player, then the player can attempt the move, but the 
result will be only to make the invisible piece or wall visible to 
the player (i.e. the turn ends without any piece actually moving). 

Most Area Wins
~~~~~~~~~~~~~~

The “Most area wins” rule (from Go)
means to assign the win at stalemate based on the total number of 
spaces (including locked blanks) that each player either occupies 
or could move through by moving any single one of their pieces any 
number of orthogonal moves (i.e. it excludes spaces occupied or 
surrounded by opponents). 

Simultaneous Play
~~~~~~~~~~~~~~~~~

In simultaneous play, each player sees the board as it was at the 
beginning of the round and registers a “plan” based on what moves 
would be legal if that player were first to move. After all plans 
are registered, if multiple players move to the same space and the 
collision is not resolved naturally via “by rank” rules, then all 
pieces moved to that space are destroyed.

Phases
~~~~~~

Each game has from 1 to 6 phases--stalemate advances the phase. 
Each phase other than the last may have a “fold” rule applying at 
the end of that phase to all but Chaos (e.g. “Less-than-most 
committed pieces folds” means that only the players with the most 
pieces locked against exit do not fold). Players who have folded 
cannot move for the rest of the game (but are still eligible to 
win). Each phase must also define whether there is an option to 
pass, which players (if any) are locked for that phase, whether 
all moves must be from reserves, which spaces are locked and/or 
“cloaked” for that phase, and whether turns are sequential 
(default), simultaneous, or “single” (i.e. simultaneous and lasts 
only one turn). 

Movement
~~~~~~~~

Each shape may have its own rules for move or capture. A player 
cannot move a placed piece if the player has an identical piece 
in reserve, If a shape “cannot move backwards”, then a player 
cannot move pieces of that shape away from his/her own goal line 
(or plane), and any move that reaches the goal requires the player 
to also select a replacing shape that can move backwards. 

Capture
~~~~~~~

Some pieces may be able to capture opponent pieces by covering 
them (e.g. chess), surrounding them (e.g. reversi), jumping them, 
chain-jumping them (e.g. draughts), or “cover by rank” (stratego). 
The second to last capture option adds an additional move to the 
player’s turn which can be used only to jump with the same piece 
or to pass. The last capture option means that the highest-ranked 
of the attacker/defenders captures the others. Pieces that cannot 
capture have the lowest rank and cannot cover each other (but 
become captured by covering a higher-ranked piece); pieces that 
capture in ways other than “by rank” have highest rank and award 
conflicts between each other to the attacker; otherwise cover of 
equal rank results in mutual destruction. Depending on the type 
of captor, captives may be destroyed, converted (not permitted 
for “cover by rank” except on stacks), reincarnated (i.e. added 
to the captor’s reserves), or reincarnate (x2) (double upon 
capture). If a piece “must capture” and at least one opportunity 
to capture is visible, then no non-capture is legal.

Multiple Boards
~~~~~~~~~~~~~~~

The number of boards can be 1, 2 or 3. When the outcome of a 
board is determined, it becomes locked to all players, but 
players can otherwise play on any board in any turn; whomever 
wins the most boards wins the game. 

Stacks
~~~~~~

If the board is “stacks”, then moves are always to the tops of 
stacks (so height is ignored when determining whether the move 
qualifies as “orthogonal”), but fall to the lowest empty space 
on that stack (e.g. Connect4); reserves can be placed on any 
stack that doesn’t appear to be full. Pieces that do not move 
“by stack” can move only from the top of a stack; the others 
bring all pieces above them along for the ride and can move 
only to posts that appear to have that much available space 
(e.g. moving a stack of poker chips); those that move “by full 
stack” (e.g. poker hands) can move only if on the bottom of a 
stack. 

Capture on Stacks
~~~~~~~~~~~~~~~~~
For conversion and reincarnation on cover, all players 
with the highest rank on the stack split the pot (each captor 
retains the pieces that make them highest rank; the remaining 
pieces are allocated in descending order of rank  round-robin 
to the captors starting randomly--i.e. if there are three 
reincarnate (x2) captors of two pieces, then one captor gets 
two and the others each get one). A player’s rank in a move 
“by stack” or “by full stack” is determined from the full set 
of pieces in the destination stack (after the move) owned by 
that player or by no player (“communal pieces”), ignoring any 
pieces of the lowest possible rank (chips), using the following 
hierarchy: highest-5-of-a-shape outranks highest-4-of-a-shape 
which outranks highest-5-straight which outranks 
highest-full-house (i.e. three-of-a-shape-plus-pair) which 
outranks highest-4-straight which outranks highest-3-of-a-shape 
which outranks highest-2-pair which outranks highest-3-straight 
which outranks highest-pair which outranks highest-2-straight 
which outranks highest-singleton.






Acceptance Test Plan
--------------------

Test each of the clickable elements and test that it displays appropriate errors for invalid entries. Create and play:

Tic-Tac-Toe

3on15line: 
  Played on 15x1x1 squares, 8 black and 7 white start in reserve 
  
Treblecross15:
  Played on 15x1x1 squares, Shared Color, 15 black start in 
  reserve

3P-Misere-Notakto:
  3 Player, Shared Color, 9 black start in reserve,
  
3P-Notakto:
  3 Player, Shared Color, 9 black start in reserve,
  First 3-same-color-in-a-row loses

4on7sq:
  Played on 7x7x1 squares, 25 black and 24 white start in reserve,
  First 4-same-color-in-a-row wins
  
5on15sq: 
  Played on 15x15x1 squares, 113 black and 112 white start in 
  reserve, First 5-same-color-in-a-row wins, 300 seconds/turn
  
Connect6-19x19:
  Played on 19x19x1 squares, start with white occupying (10,10)
  and 180 black and 180 white in reserve, First 
  6-same-color-in-a-row wins, 2 moves/turn, 300 seconds/turn
  
Tapatan: 
  3 black and 3 white start in reserve, Moves adjacent
  
Achi:
  4 black and 4 white start in reserve, Moves adjacent
  
9-Holes: 
  3 black and 3 white start in reserve, Moves linear or knight, 
  First 3-same-color-in-a-row-orth wins

Qubic-4:
  4x4x4 squares, 32 black and 32 white start in reserve, 
  First 4-same-color-in-a-row wins, 300 seconds/turn
  
Connect4:
  7x1x6 stacks, 21 black and 21 white start in reserve,
  First 4-same-color-in-a-row wins
  
4P-Blind-TTT:
  Partners, Partners share color, All spaces cloaked, Cloaking 
  hides
   
3P-MostWins-3x4:
  3x4x1 squares, 4 black, 4 white, and 4 pink start in reserve, 
  3 Player, Most-same-color-in-a-row wins
  
3P-LeastLoses-3x4:
  3x4x1 squares, 4 black, 4 white, and 4 pink start in reserve, 
  3 Player, Least-same-color-in-a-row loses
  
Wild-TTT-6sq3143:
  6x6x1 vertices, (3,1,1) and (4,3,1) are locked, 18 black and 
  18 white start in reserve, Players choose color
  
RockPaperScissors:
  1x1x2 stacks, Simultaneous, 
  Circle: Can capture, Cover by rank, Converts captive(s), 
  1 black and 1 white start in reserve; 
  Pentagon: Can capture, Cover by rank, Converts captive(s), 
  1 black and 1 white start in reserve; 
  X: Can capture, Cover by rank, Converts captive(s), 
  1 black and 1 white start in reserve; 
  
3P-9X-HideSeek: 
  5x5x1 squares, all but the center nine spaces exclusive to chaos; 
  starts with yellow pentagon in (1,1) and pink circles in all 
  remaining spaces except center nine; 3 vs chaos, Cloaking hides;  
  Most circles wins, Statemate if chaos cannot capture;
  Circle: Moves adjacent or knight, 1 black and 1 white start in reserve;
  Pentagon: Must capture, Cover, Destroys Captive(s), Moves 
  adjacent, 1 pink starts in reserve;
  Phase 1: Placement only, center nine spots are cloaked;  
  Phase 2: Option to pass, center nine spots are cloaked
  
Shopping9:
  3x1x9 stacks; First stack exclusive to black, second stack 
  exclusive to white and starts with 2 white pentagons, third 
  stack exclusive to pink; 2-vs-chaos, Cloaking hides, 
  Least pieces loses; Chaos wins if total circles > 9;
  Circle: 9 black and 7 white start in reserve;
  Pentagon: 8 pink start in reserve;
  Phase 1: Option to pass, All but first player locked;
  Phase 2: Option to pass, All but second player locked;
  Phase 3: Option to pass, All but chaos locked 
  
4P-TrendSetter: 
  1x3x1 squares, 4 Player, Simultaneous, All players lose if  stalemate, Any piece wins, 1 black, 1 white, 1 pink, and 1 
  yellow start in reserve   
  
3P-PublicGoods:
  5x1x8 stacks; each of the first four posts is locked to all but on one of the players respectively; the last post is locked to 
  chaos, 3-vs-chaos, Less pieces than chaos loses, the first three 
  players start with 1 pentagon each on the final post and 1, 2 
  or 3 circles on their exclusive post respectively, chaos starts 
  with 5 circles in reserve, circle moves unlimited orth by stack, 
  pentagon reincarnates (x2) by cover. Phase 1 “Invest”: Single; 
  option to pass; all posts locked to chaos. Phase 2 “Return”: 
  All posts locked to chaos; last post locked (so all returns will 
  automatically move to exclusive posts). 3 “chaos”: Option to 
  pass; all posts locked to all but chaos.)
  
NeedyTrust:
  4x1x9 stacks; the posts are locked to all but the first, to chaos, to all but the second, and to all but chaos respectively, 
  2-vs-chaos, More pieces than chaos wins, Less pieces than chaos 
  loses, the first player starts with 2 circles on the first post, 
  1 pentagon on the third stack, and 2 circles in reserve; the 
  second player starts with 1 X on the second post; chaos starts 
  with 4 circles on the fourth post and 2 in reserve; pentagon 
  converts by cover; X reincarnates (x2) by cover. Phase 1: All 
  posts locked to all but the first player. Phase 2 “Return”: All 
  posts locked to all but the second player. Phase 3 “chaos”: Option 
  to pass; all posts locked to all but chaos.
  
RichTrust:
  like NeedyTrust, but the first player starts with 1 pentagon on 
  the third stack, and 4 circles in reserve, and chaos starts with 
  3 circles on the fourth post and 2 in reserve.
  
3Blotto13 (3 boards of 2x1x13 posts, Most pieces wins, each player starts with a reserve of 13 circles. Cloaking offers invisibility; all spaces cloaked; each player has one post locked to all other players on each board)
KBeauty9 (3x1x9 posts; cloaking offers invisibility; all posts are cloaked; each post is locked to all but one player, 4 players, Most-in-a-row wins, Overachiever(s) disqualified; each player starts with a reserve of 9 circles. Phase 1 “Player 1”: Option to pass; only the first player can play. Phase 2 “Player 2”: Option to pass; only the second player can play. Phase 3 “Player 3”: Option to pass; only the third player can play. Phase 4 “Player 4”: Option to pass; only the fourth player can play; the player ending the phase with most in a row is disqualified.) Shows advantages of Introversion and Empathy
StagHunt (4x1x3 posts; the first and second posts are locked to all but the first and second player respectively; the third and fourth posts are locked against the second and first players respectively; 2-vs-chaos, Most 2-same-color-in-a-row wins, the first two players start with one pentagon in reserve and one pentagon on one of the first two posts respectively, chaos starts with 6 circles in reserve; pentagons remove via cover (like mines). Phase 1 “Hunt”: Simultaneous play; the last two columns are locked to chaos. Phase 2 “chaos”: Option to pass; all posts locked to all but chaos) Shows advantages of Empath

Other interesting games
~~~~~~~~~~~~~~~~~~~~~~~
4P-Coordination (1x3x1 squares, 4 players, All players win if stalemate, Any piece loses, each player starts with one circle in reserve. Simultaneous play.) 
PrisonerDilemma (5x1x2 posts; the second post is all wall; the first, third and fourth posts are locked to all but the first three players respectively, 2-vs-chaos, Most 2-same-color-in-a-row wins, the first player starts with one X on the first post and one X in reserve, the second player starts with one pentagon on the third post and one pentagon in reserve, chaos starts with six circles in reserve; pentagon and X remove via cover by rank. Phase 1 “Testify”: Simultaneous play;all posts locked to chaos. Phase 2 “chaos”: Option to pass; all posts locked to all but chaos) Shows advantages of Empath
NeedyUltimatum (like NeedyTrust, but the first player starts with a reserve of 3 circles; the second player starts with 3 circles and 1 pentagon on the first post and 1 X in reserve; chaos starts with 5 circles on the third post, 2 on the fourth post, and 3 in reserve; X removes on cover.) 
3P-Volunteer (5x1x3 posts; the first four posts are locked to all but the first four players respectively; each of the last two posts ends with a wall, 3-vs-chaos, Least 2-same-color-in-a-row loses, the first player starts with two pentagons on the first post and one pentagon in reserve, the second and third players start similarly with the second and third post and cross and X respectively, chaos starts with eight circles in reserve; pentagon, cross, and X remove via cover by rank. Phase 1 “Choose”: Simultaneous play; all posts locked to chaos. Phase 2 “chaos”: Option to pass; all posts locked to all but chaos.) Shows advantages of Empath
BoS (2 boards of 2x2x1 vertices;each player has one space locked against all other players on each board; the remaining space is locked to all players and diagonal to a different non-chaos player on each board, 2-vs-chaos, Least area wins, each player (including chaos) starts with one circle in reserve. Phase 1 “Choose”: Simultaneous play; all posts locked to chaos. Phase 2 “chaos”: All posts locked to all but chaos.) Shows advantages of Empath
Centipede10 (2x1x10 posts; alternating spaces on the first post are locked to all but the first two players; the second column is locked to all but chaos, 2-vs-chaos, Most pieces wins, the first two players each start with a reserve of 5 circles, chaos starts with a reserve of 8 circles; the circle converts on cover. Phase 1 “Race”: Sequential play; option to pass; all posts locked to chaos; players swap positions at end of phase. Phase 2 “chaos”: Option to pass; all posts locked to all but chaos.)
NeedyDictator (like NeedyUltimatum but the second player has no reserves.)
ContractHunt (4x1x3 posts; the first two posts are locked to chaos, the second posts is locked to the first player; the third and fourth posts are locked against the second and first players respectively, 2-vs-chaos, Most 2-same-color-in-a-row wins, the first player starts with a pentagon in reserve and a pentagon on the first post, the second player starts with two pentagons in reserve, chaos starts with 6 circles in reserve; pentagons remove via cover (like mines). Phase 1 “Contract”: Single; all posts locked to chaos and the first player; the fourth post locked to all. Phase 2 “Hunt”: Simultaneous; all posts locked to chaos. Phase 3 “chaos”: Option to pass; all posts locked to all but chaos) Shows advantages of Empath
ContractPD (5x1x2 posts; the second post is all wall; the first post is locked to chaos, third and fourth posts are locked to all but the second player and chaos respectively, 2-vs-chaos, Most 2-same-color-in-a-row wins, the first player starts with one X on the first post and one X in reserve, the second player starts with two pentagons in reserve, chaos starts with six circles in reserve; pentagon and X remove via cover by rank. Phase 1 “Contract”: Single; all posts locked to chaos and the first player; the fifth post locked to all. Phase 2 “Testify”: Simultaneous play; all posts locked to chaos. Phase 3 “chaos”: Option to pass; all posts locked to all but chaos.) Shows advantages of Empath
OptionalPD (5x1x2 posts; the second post is all wall; the first, third and fourth posts are locked to all but the first three players respectively, 2-vs-chaos, Most 2-same-color-in-a-row wins, the first player starts with two Xs in reserve, the second player starts with two pentagons in reserve, chaos starts with six circles in reserve; pentagon and X remove via cover by rank. Phase 1 “Opt-in”: Single; Option to Pass; fourth and fifth posts locked; all posts locked to chaos; Draw if less than 2 pieces played at end of phase. Phase 2 “Testify”: Simultaneous play; all posts locked to chaos. Phase 3 “chaos”: Option to pass; all posts locked to all but chaos,) Shows advantages of Empath
3P-BoS (3 boards of 2x2x1 vertices;each player has one space locked against all other players on each board; chaos’s space is diagonal to a different non-chaos player on each board, 3-vs-chaos, Least area wins, each player (including chaos) starts with one circle in reserve. Phase 1 “Choose”: Simultaneous play; all posts locked to chaos. Phase 2 “chaos”: All posts locked to all but chaos.) Shows advantages of Empath
NeedyCentipede4 (same as Centipede, but chaos starts with 4 circles on the second post 6 in reserve.)
RichUltimatum (like NeedyUltimatum, but the first player starts with 4 circles on the second post and 3 in reserve; the second player starts with 1 pentagon on the first post and 1 X in reserve; chaos starts with 5 circles on the third post, 2 on the fourth post, and 3 in reserve.)
RichDictator (like RichUltimatum, but the second player has no reserves.)
4P-TrolleyDilemma (4x1x4 stacks; each of the posts is locked to all but one of the players respectively; 4 Players, Most-in-a-row loses, the first player starts with 1 circle in reserve, the second player starts with 1 pentagon on the first post and 2 circles on the second, the third and fourth players start with three circles each on their respective post, pentagon reincarnates (x2) by cover. Phase 1 “Dilemma”: Single; option to pass; all post locked to all but first player. Phase 2 “Return”: All posts locked to chaos (so all returns will automatically move to exclusive posts). 
3P-TrolleyDilemma (6x1x5 stacks; each of the first three posts is locked to all but one of the players respectively; the last three posts are locked all but chaos, 3-vs-chaos, Most-in-a-row loses, the first player starts with 1 circle in reserve, the second player starts with 1 pentagon on the first post and 2 circles on the second, the third player starts with three circles on the third post, chaos starts with 5 circles in reserve, pentagon reincarnates (x2) by cover. Phase 1 “Dilemma”: Single; option to pass; all post locked to all but first player. Phase 2 “Return”: All posts locked to chaos (so all returns will automatically move to exclusive posts). 3 “chaos”: Option to pass; all posts locked to all but chaos.)


Potential Mockups
-----------------

To export game::

  redscience game {name} -e {file}
  
To import game::

  redscience game {name} -i {file} {security token}
  

Game Factory Page
~~~~~~~~~~~~~~~~~

 .. figure:: images/3P-poker.png

   Shown as of :doc:`tournaments` (to anticipate evolution of page).
   Deck and dealt pieces do not show until then.
   
* The name text field does not accept whitespace, ‘*’, ‘(‘, or ‘)’.
* The "Save" button validates the record and saves if valid. Once
  saved, only the name can be edited (and only by an admin), but
  a "Copy" button may appear which opens a new unsaved Player 
  Factory page with values prefilled to match this page. Creators 
  see this button until their quota is exhausted. Blank dropdowns,
  palette options, and integer selects of zero are hidden on 
  saved pages. A new rule set will not save if another identical 
  rule set (except name) has already been saved.
* The stalemate dropdown offers “Stalemate draws” as default,  
  “All players win if stalemate”, “All players lose if stalemate”, 
  “Most same-color-in-a-row wins”, and “Least same-color-in-a-row 
  loses” (can extend to “Most pieces wins”, 
  “Any 3-same-color-in-a-row wins”, “Last 3-same-color-in-a-row 
  wins”, “Stalemate loses”, “Stalemate wins”, etc.).
* The “Add Check” button (fa-plus) inserts another turnCheck 
  dropdown (with “Delete Check” button. 
* The turnCheck dropdown offers “First 3-same color-in-a-row wins”, 
  “First 3-same-color-in-a-row loses”, “First 
  3-same-color-in-a-row wins (no diagonal)”, “First 
  4-same-color-in-a-row wins”, “First 5-same-color-in-a-row wins”, 
  “First 6-same-color-in-a-row wins” (can extend to “First 
  2-same-color-in-a-row loses”, “Last pentagon wins”, “En 
  passant”, “Castle”, “All players lose if any 
  3-same-color-in-a-row”, etc). 
* The “Delete Check” button (fa-trash-o) removes that turnCheck 
  dropdown.
* The players dropdown offers “2 Player”, “2 vs Chaos”, “3 Player”, 
  “3 vs Chaos”, “4 Player” or “Partners” (can extend to … “1 vs 
  chaos”). Changing the players adds/removes goals from the board. 
  If the color is not shared, then it also adds/removes reserved 
  integer selects (default the values in added integer selects to 
  those in the highest-numbered existing player). 
* The shapes dropdown offers “1 shape”, “2 shapes” (can extend to 
  “3 shapes”, “4 shapes”, “5 shapes” or “6 shapes”). Changing the 
  selection adds/removes reserved integer selects (default the 
  values in added integer selects to those in the highest-numbered 
  existing shape). 
* The color dropdown offers “Assigned colors”, “Shared color”, 
  “Partners share color”, or “Players choose color”.
* The cloaking dropdown offers "No cloaking", “Cloaking hides”, 
  or “Cloaking obscures".
* The pieces dropdown offers “1 piece/turn” or “2 pieces/turn”
* The time dropdown offers “3 seconds/turn”, “6 seconds/turn”, 
  “10 seconds/turn”, “15 seconds/turn”, “20 seconds/turn”, “30 
  seconds/turn”, “40 seconds/turn”, “60 seconds/turn”, “90 
  seconds/turn”, “120 seconds/turn”, “180 seconds/turn”, “240 
  seconds/turn” or “300 seconds/turn”.
* The boards dropwdown offers “1 boards”, “2 boards”, or “3 
  boards”.
* The phases dropwdown offers “1 phase”, “2 phases”, “3 phases”, 
  “4 phases”, “5 phases”, or “6 phases”.
* The board dropdown offers “Hash”, “Squares”, or “Stacks” (can 
  extend to “Tetrakis squares”, “Squares on Toroid”, “Hexagons”, 
  etc.). Changing the dimensions causes the board to redraw, and 
  may adjust the dimensions. For Hash, the dimensions are frozen 
  at 3x3x1. For Stacks, the third dimension must be greater than 
  1. Player1 Goal is always at y=max (or x=1, if the max y is 1). 
  For two-player games, Player 2 goal is opposite (e.g. y=1). For 
  games with more players, the goals proceed around the board 
  counter-clockwise (e.g. Player 2 Goal at x=1).
* Each of the dimension integer selects offers integers from 1 to
  the floor of (512 / the product of the other two dimensions) 
  upto a max of 19. Changing the dimensions causes the board to 
  redraw; if two dimensions are 1, it will draw a horizontal 
  row; if one is 1, it will draw a plane; if none is 1, it will 
  draw a 3D graph. 
* Each power dropdown offers “No power”, “Must capture”, and “Can 
  capture”. If “No power” is selected, then the associated power_
  condition and power_result dropdowns are cleared and disabled. 
  Pentagon outranks star which outranks cross which outranks X 
  which outranks triangle which outranks circle (but circle 
  outranks pentagon and only pentagon). 
* Each power_condition dropdown offers “Cover” and “Cover by rank” 
  (can extend to “Move on diag + en passe”, “Move on triagonal”, 
  “Jump”, “Chain Jump”, “Chain Jump (+ back)”, “Surround line”, 
  “Surround orthogonal”, “Approach”, “Adjacent”, etc. If a “Cover” 
  condition is selected on non-stacks, then clear all results 
  except Remove and Reincarnate.
* Each power_result dropdown offers “Removes captive(s)”, 
  “Converts captive(s)”, “Reincarnate Captive(s)” (can extend to 
  “Paralyzes captive(s)”, etc.). To “Reincarnate” captives means 
  to convert, remove, triple, and add them to one’s own reserves.
* Each move dropdown offers “Moves adjacent”, “Moves orth by 
  stack” or “Moves linear or knight” (can extend to “Stationary”, 
  “Moves forward orth”, “Moves forward diag”, “Moves adjacent (no 
  back/side)”, “Pawn move forward/center “, “Moves orth (no back)”, 
  “Rook move orth/castle”, “Moves adjacent (no back)”, “Knight move 
  2x1x0”, “Moves adj diagonal”, “Moves adj orthogonal”, “Knight 
  move 2x1x1”, “Moves diagonal”, “Moves orthogonal”, “Moves linear”)
* The phase drowdown offers as many Phase labels as indicated in 
  the phases drowdown. selecting the phase resets the interface 
  below it to the selected phase.
* The order dropdown offers "Sequential", "Simultaneous", and 
  "Single".
* The phase_movement dropdown offers "Movement allowed" and 
  "Placement only".
* The pass dropdown offers "Option to pass" and "No option to pass"
* Clicking an exclusive marker, cloak marker, lock marker, sticky 
  marker, dealt common, or one of the shape markers next to a 
  reserved integer select selects it with green highlighting. 
  Clicking a space with the selected property will clear that 
  property from the space; clicking a space that lacks the selected
  property will add it. The cloak and lock properties are the only 
  ones that can be changed after phase 1.
* Each reserved integer select offers integers from 0 to the maximum 
  number that can be played (e.g. the product of the dimension 
  integer selects divided by the number of colors). If the maximum 
  is selected for all selects of a given shape, then the move 
  dropdown for that shape is cleared and disabled. These are editable
  only for phase 1.
  

Leaderboard Tab
~~~~~~~~~~~~~~~

 .. figure:: images/Leaderboard.png

   Shown as of :doc:`generalintellgence` (to anticipate the 
   evolution of page). Dots should be replaced with the rest of 
   the list of top rated players. 
   The “Benchmark” button (fa-balance-scale) does not show 
   until :doc:`tournaments`, the “Show Learning-curve” buttons 
   (fa-line-chart) do not show up until :doc:`educated`, the 
   Difficulty level and Related games do not show up until 
   :doc:`generalintellgence`.

* The “Show All Creations” button (fa-flask) navigates to the 
  Creations tab of the creator’s Player Page
* The player combobox lists players who have played this game 
  in the selected Universe. The “Add Player” button (fa-plus) 
  adds the selected player to the Leaderboard below (in sorted 
  order).
* The Universe combobox lists “Public Universe” and any other 
  Universes in which the user has Persona (do not display if 
  there is only one option). Defaults to the Universe most 
  recently selected by the user.
* Sort descending by skill rating + Top-Burst. In parentheses, 
  show how long that level has been held. The top ten players 
  are ranked. Display up to ten players from the selected 
  universe, including ranked players, the user (if played), 
  random (in all universes), and the standard player (SP) for 
  the rule set if there is one (in all universes). There might 
  not be enough room to display all ranked players. Show 
  checkboxes for Random and AI players.
* The “Benchmark Selected Bots” (fa-balance-scale) button is 
  available for Trainers and Admins. It saves the current record 
  and navigates to the Tournament page with 100 games for each 
  combination of checked players. If the players include the top 
  player, the player it is most Favored By, Random and at least 
  one other player, then it qualifies as a “Benchmark” tournament.
* The “Show Evolution” button (fa-line-chart) saves the current 
  record and navigates to the Evolution Page with this rule set, 
  the checked players, and “Rating” selected.
* The “Show Player” buttons (fa-address-card-o) navigate to the 
  Stats tab of the associated Player
* The “Play New Game” buttons (fa-fort-awesome) saved the current 
  record and navigates to the Home Page with this Rule set 
  prefilled and the associated player prefilled in the second 
  slot. It displays only for non-human players, friends, and 
  personas created by the user.
* The “Add to Friends” buttons (fa-user-plus) sends a friend 
  request to the associated player. It displays whenever no 
  “Play New Game” button displays.


Potential Schema
----------------

