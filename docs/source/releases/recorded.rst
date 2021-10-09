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

To access from command line::

  redscience player name

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

.. figure:: images/Player.png

   (but the email/Universe textbox does not show until Release 1.3). 

* When the user is the creator or an Admin, clicking the Avatar 
  navigates to the Avatar Selection page
* The name text field does not accept ‘*’, ‘(‘, or ‘)’.
* The “Copy Player” button (fa-files-o) saves the current record 
  and opens a Player page for a new Persona. 
* The stats table is sorted by Last Match (most recent on top). 
  Display the type of augmentation with the game (A=Alone, 
  D=Delegating, R=Reviewing). The “Sort by this Column” buttons 
  re-display the table sorted by the values in the associated 
  column; if already sorted by that column, reverse the order.
* The “Play New Game” buttons (fa-fort-awesome) saves the current 
  record and navigates to the Home Page with the associated game
  and this player prefilled. 
* The Rating numbers are “Show Evolution” buttons which save the 
  current record and navigate to the Evolution Page with this 
  player, the associated game (and augmentation) and score 
  selected. The rating displays a conservative estimate (i.e 
  rating minus two standard deviations), but displays in bold if 
  within a standard deviation of the maximum rating for that game 
  among all player/augmentation combinations.
* The Favoritism numbers are “Show Favoritism” buttons which 
  navigate to the Favoritism tab with the associated game (and 
  augmentation) selected.
  

   
 .. figure:: images/HumanSelect.png

   Clicking an Avatar navigates back to the player page with the 
   avatar replaced with the selected avatar
   

