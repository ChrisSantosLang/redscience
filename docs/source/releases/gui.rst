===================
1.1 GUI Tic-Tac-Toe
===================

Requirements
------------

Adapt the Command Line Tic-Tac-Toe to work entirely with the mouse. 
Require separate clicks to select a move (at which point the move 
displays highlighted as "proposed"), and to accept it. Add a 
count-down timer that resets to one minute every time the turn 
changes and automatically accepts the proposed move when the minute 
is up. Any player who does not select their move before the timer 
runs out, or who leaves the playground before the game is complete, 
loses. In addition to displaying the name of the game being played, 
display its rules (piece-specific rules like ability to move or 
capture can be displayed via tooltip). 

Impulses
~~~~~~~~

Randomly assign each player two private impulses: Subtle vs. Basic 
(33.333% frequency) and Rare vs Common (20% frequency). Having private 
impulses provides strategic advantage in games for which opponents 
could exploit predictability; making them available to all players 
levels the playing field.
 
Acceptance Test Plan
--------------------

Test each of the clickable elements and test that it displays 
appropriate errors for invalid entries

Potential Mockups
-----------------

To start from command line:: 

  redscience
  
.. figure:: images/HomePage1.png

   Comboboxes and dropdown are disabled at GUI Tic-Tac-Toe Release
   
.. figure:: images/Playground.png

  * The avatars and assigned colors of the other players are shown 
    in order of play (next player first). If there are no invisible 
    spaces, then also display the total count of each other player’s 
    reserves. For the user, however, show count by shape, and allow 
    the user to see rules specific to that shape as tooltips. The 
    display of impulses are indicated by icons (fa-heartbeat). 
  * The bar on the bottom of the page changes to gray as the time 
    runs out. If the user has prefilled a move, but has not accepted 
    it, then it will automatically be accepted when the clock runs 
    out; otherwise, the player who let the clock run out loses.
  * The active move is indicated by an arrow (fa-arrow-circle-right). 
  * If the “From” of the active move is already specified or cannot 
    be edited, then clicking any legal “To” coordinates changes the 
    “To” of the active move to those coordinates and places a small 
    piece highlighted in green at the clicked coordinates. If that 
    leaves all moves fully specified, then it enables “Accept Move”. 
  * Clicking a proposed move on the board (small highlighted piece) 
    clears its “To” and any subsequent moves. This will also disable 
    the “Accept Move” button.
  * The “Accept Move” button (fa-check, style=success) advances the 
    turn.
