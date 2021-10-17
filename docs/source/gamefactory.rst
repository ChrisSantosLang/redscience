==============
Creating Games
==============

Clicking the **Copy** button on the **Step & Rules Tab** or **Events Tab** of a 
:doc:`game <game>` yields a new copy that can be altered (until first 
saved):

.. image:: releases/images/3P-poker.png

In addition to specifying reserves and initial piece placement (which 
can include pieces dealt from a shuffled deck), the creator can designate 
spaces as exclusive to specific players or as "sticky" (no exit). Each 
phase can be *sequential*, *simultaneous*, or *single* (which is simultaneous, but 
last only one turn), can lock specific players, and can lock or cloak specific 
spaces. Each shape of piece can have its own power and way of moving (or not). 

A few options deserve special explanation:

* Instead of *2 Player*, *3 Player* or *4 Player*, a game can be 
  *Partners* (odd vs. even), *2 + Chaos* or 
  *3 + Chaos*. "Chaos" is a randomized common-enemy. *4 Player*
  games can have an "Overachiever(s) disqualified" rule
  that disqualifies the first player(s) to qualify as winners
  from actually winning.
* "Fold" rules are checked at the end of each phase. If a player 
  other than "Chaos" folds, then that players is locked for the rest of 
  the match (but remains eligible to win).
* Instead of the *Hash* used in Tic-Tac-Toe, the board can be *Squares* of
  various dimension or *Stacks* for which pieces can be placed or
  moved only to/from the tops. Pieces that move *by stack*
  bring all pieces above them along for the ride. Pieces that move 
  *by full stack* always bring the entire stack.
* Intead of *destroy*, the effect of capture can be to *convert* which 
  changes the color of captives to match their captor, to *reincarnate* 
  which converts and moves the captured pieces to the captor's reserves,
  or to *reincarnate (x2)* which reincarnates but multiplies the captives.
* Pieces with the *chain-jump* power can make multiple jumps in a row 
  in a single turn. When pieces with the *cover by rank* power cover (or
  are covered by) other pieces, the piece with the highest rank captures 
  the rest. All are destroyed if the ranks are equal.  Pentagon 
  outranks star which outranks cross which outranks X which outranks 
  triangle which outranks circle (but circle outranks pentagon and only 
  pentagon). When pieces that move *by stack* cover by rank, the 
  rank is a combined rank of all pieces of that color in the final stack 
  plus any communal pieces in the final stack (ignoring any pieces of the 
  lowest possible rank). Highest-5-of-a-shape outranks 
  highest-4-of-a-shape which outranks highest-5-straight which 
  outranks highest-full-house (i.e. three-of-a-shape-plus-pair) 
  which outranks highest-4-straight which outranks 
  highest-3-of-a-shape which outranks highest-2-pair which 
  outranks highest-3-straight which outranks highest-pair 
  which outranks highest-2-straight which outranks 
  highest-singleton.
  
All social behavior can be modelled via games, and special effort 
has been made to ensure that users can construct games of each kind in 
economic game theory (e.g. *Public Goods*, *Prisoner Dilemma*, 
*Stag Hunt*, *Ultimatum*, *Volunteer*, *Battle of the Sexes*, 
*Dictator*, *Trust*, *Beer-Quiche*, etc.). Please let us know if there
is a kind of game that cannot be constructed.
