============================
1.0 Command Line Tic-Tac-Toe
============================

The :doc:`../curriculum` for building redscience divides the task 
into :doc:`../releases/releases`, of which Command Line 
Tic-Tac-Toe is the first. The following plan serves as an example 
of the kind of plan you can expect for other versions. 

Much of the curriculum walks students through implementing parts of 
this plan. It is possible to code from the software architecture
without reading the higher-level plans that the architecture is 
designed to fulfill (just like it is possible to modify open source 
code without knowing why it was built the way it was), but having
a higher-level understanding of what you are working on can make you 
more productive in innovation. Therefore, *this* is the recommended
starting point of the curriculum.

Requirements
------------

*(Various words are bolded in this first set of requirements to 
give a sense of what an ontology would have to include. An 
ontology needs to provide more than what we can expect from a 
narrative, but there is substantial overlap.)* 

Write a program that allows two **humans** (sharing the same keyboard) 
to play **Tic-Tac-Toe** at the **command prompt**, with **options** 
at any point to **quit**, **undo the last move**, or 
**start a new game**. Randomize the order of the **players** at the 
beginning of each new **game**. A player cannot attempt to place 
a **piece** from **reserves** to **coordinates** that the player knows 
are occupied. If a player has only one legal 
**move**, then choose it automatically (so the other player doesn’t 
have to wait). If a player has no legal move, automatically **pass**. 
Detect when a player repeats the exact same move facing the exact same 
**board**--this will be called “stalemate” and happens in 
Tic-Tac-Toe only when the board is full (so both players 
automatically pass). The **stalemate rule** determines the outcome if
the final phase of a game ends in stalemate. Each game may also have 
one or more **rules** that are checked at the end of each **turn** (e.g. 
“**First 3-same-color-in-a-row** **wins**”). 

The program should contain the following **rules** as a **constant**, 
and the rules should determine how **play** proceeds: 

* Played on **hash** (**3,3**)
* **2-Player**
* **Assigned Colors**
* **Circle**: 5 **black** and 4 **white** start in reserve
* First 3-same-color-in-a-row wins
* Stalemate **draws**

In general, a game move is either a pass, a 
**request to call it a draw**, **agreement**/**rejection** of such a 
request, a **jump** from **one spot** to another, or a 
**placement** from reserves of a given **shape** and **color** to a 
spot on the board. The rules of Tic-Tac-Toe permit players to choose 
only moves of the last type and to only specify “to” coordinates, 
since all pieces in that player’s reserves will be of the same shape 
and color, but design your code to evolve support for other games 
(e.g. other-dimensional boards, other kind of pieces/cards, etc).
 
Acceptance Test Plan
--------------------

Test that the program works. Confirm that it does not permit illegal 
moves, and that it recognizes draws and all kinds of wins (e.g. 
horizontal, vertical, upward-slanting-diagonal, and 
downward-slanting-diagonal). After finishing a game, confirm that 
you can roll back the choices using undo. Also confirm that you can 
end the game or restart at any time.

Potential Mockups
-----------------

To start from command line::

  pip install redscience
  redscience tic-tac-toe

.. figure:: images/commandline.png

   Each move adds a new section to the bottom...

