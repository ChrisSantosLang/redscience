===============
1.13 Corp Games
===============

Requirements
------------

Modify the Team Games program to allow users to benchmark *Strong* 
Social Intelligence (i.e. teams that collaborate on each move). 
Create a new type of player called "Corp" similar to a Team. 
When selecting a member to serve as Explorer, also select one or 
more members to serve as Debaters (contrast to *Weak* Social 
Intelligence in which the only Debater is the Explorer itself). 
Increase the Research Budget max to permit more use of Debaters 
(research/collaboration overhead is an expected weakness of Corps,
but might be addressed by reducing cost per experiment). The 
options for the specialization colormap on Corps are Explored, 
Debated, Accuracy, F1, LG, Empath, and Teach. For each event (and 
for top node), allow users to view a graph of the evolution of 
share (among all members) in exploring (a.k.a. hypothesizing), 
debating (a.k.a. hypothesis testing), and total participation. 

At the end of each experiment, instead of the Explorer learning 
strategic/unstrategic outcomes if predicted by the Explorer on its 
last move (as in introspection), determine the 
strategic/unstrategic outcome via vote among all members weighted 
by each member’s Long-Game for the grandparent node in the Corp’s 
game-classification tree. At the end of each full match, the skill 
rating is updated for Corp as a whole (never for an individual 
member of the Corp). 

Acceptance Test Plan
--------------------

Like in the previous Release, benchmark Corps of various 
compositions against each other and against existing players 
(including the current grand master of Test). Do any fare well 
against the grand master in the first 100 games? Is the optimal 
composition of a Corp the same as a regular Team? Do Corps evolve 
the same specialties as regular Teams? How do the two types of 
Teams fare against each other on Train and on Test? Are different 
types of players optimal at different stages of expertise? Do 
different machine learning algorithms (or parameters) work better 
for specialists, generalists, explorers and debaters?

Compare favoritism by Corps vs other kinds of players


Potential Schema
----------------

