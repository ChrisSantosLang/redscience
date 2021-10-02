==============
Creating Games
==============

Clicking the **Copy** button on the **Step & Rules Tab** of a 
:doc:`game <game>` yields a new copy that can be altered until first 
saved:

.. image:: releases/images/3P-poker.png

In addition to specifying reserves and initial piece placement (which 
can include pieces dealt from a shuffled deck), the creator can designate 
spaces as exclusive to specific players or as "sticky" (no exit). Each 
phase can be *sequential*, *simultaneous*, or *single* (simultaneous, but 
lasting only one turn), can lock specific players, and can lock or cloak specific 
spaces. Each shape of piece can have its own power and way of moving (or not). 

A few options deserve special explanation:

* "Fold" rules are checked at the end of each phase. If a player 
  other than "Chaos" folds, then they are locked for the rest of 
  the match (but remain eligible to win).
* Instead of *2 Player*, *3 Player* or *4 Player*, a game can be 
  *Partners* (1st and 3rd vs 2nd and 4th), *2 + Chaos* or 
  *3 + Chaos* where "Chaos" is a randomized common-enemy. *4 Player*
  games can have an "Overachiever(s) disqualified" rule
  that disqualifies the first player(s) to qualify as winners
  from actually winning.
* Instead of the *Hash* used in Tic-Tac-Toe, the board can be *Squares* of
  various dimension or *Stacks* for which pieces can be placed or
  moved only to/from the tops. Pieces that move *by stack*
  bring along all pieces above them for the ride. Pieces that move 
  *by full stack* always bring the entire stack with them.
* Intead of *destroy*, the effect of capture can be *convert* which 
  changes the color of captives to match their captor, *reincarnate* 
  which adds the captured pieces to the captor's reserves,
  or reincarnate (x2) which doubles before adding to the 
  captor's reserves.
* Exercising the *chain-jump* power adds a move to the captor's turn 
  (provided the extra move is an additional jump).
  Exercising *cover by rank* means that the highest rank among those
  covering/being-covered captures the rest (or they are all destroyed if  
  the ranks are equal). When pieces that move by stack cover by rank, their 
  rank is that of the entire moved stack plus any communal pieces in the 
  covered stack (ignoring any pieces of the lowest possible rank). 
  Highest-5-of-a-shape outranks 
  highest-4-of-a-shape which outranks highest-5-straight which 
  outranks highest-full-house (i.e. three-of-a-shape-plus-pair) 
  which outranks highest-4-straight which outranks 
  highest-3-of-a-shape which outranks highest-2-pair which 
  outranks highest-3-straight which outranks highest-pair 
  which outranks highest-2-straight which outranks 
  highest-singleton.
  
All social behavior can be modelled via games, and special effort 
is made to ensure that users can construct all major games of 
economic game theory (e.g. *Public Goods*, *Prisoner Dilemma*, 
*Stag Hunt*, *Ultimatum*, *Volunteer*, *Battle of the Sexes*, 
*Dictator*, *Trust*, *Beer-Quiche*, etc.).
