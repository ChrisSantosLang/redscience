===============
1.12 Team Games
===============

Requirements
------------

Modify the General Intelligence Games program to allow users to 
compare the results of different techniques for forming teams 
(rather than assume a team of one). Teams are meant for general 
intelligence--i.e. facing diverse (and new) challenges. Playing 
by delegating, reviewing or debating with a team should permit 
users to swap the augmentor mid-game/tournament, when the nature 
of the game/tournament is better understood. 

Create a new type of player called "Team" which is a set of AI 
players created by the creator of the Team (each AI can have 
only one team), plus optionally the Random bot. A member's 
chance of being selected to represent its Team in an event is 
that member's squared current skill rating in that event divided 
by the sum of all members’ squared current skill ratings in that 
event. Do not display Curriculum for Teams, but offer an option 
to copy the entire Team at its current state of development. 
Allow users to view the stats (rating is best rating among team) 
and learning curve at the Team level. Also allow users to view 
specialization among members as a color-map of rule sets vs 
members displaying the users' choice of either Job Share (i.e. 
percent of last 100 games assigned to that member), Rating, 
Accuracy, F1, or Long Game.  

Worldviews
~~~~~~~~~~

At the start of each event, the system uses a global AI model to 
select one member to be the Explorer, but it maintains its own 
game-classification tree to support that model. A member's F1 for 
a given node of the tree is its average F1 for all games under 
that node weighted by the inverse of the distance of the game 
leaf to the node. Each statistic in the specialization colormap 
can similarly be calculated for each tree node. Revise the tree 
after each full game, sort events in the colormap by their 
position in the classification tree, and permit users to view the 
dendrogram of any statistic and member. 

Auto-expansion
~~~~~~~~~~~~~~

Allow users to set Teams to maintain “Observers”. If this is set, 
whenever game/experiment outcomes are learned whichever member 
has the largest number of observations of the event will also 
learn the outcome (even if not serving as Explorer/Debater). If 
the event is brand new to the team, then a brand new member will 
be created to be the observer for that event.


Acceptance Test Plan
--------------------

Test each of the clickable elements and test that it displays 
appropriate errors for invalid entries. Create three teams of 
brand new players for each team size from one up to one more 
than the number of events and train them all on Train1-5. The 
first team of each size should use your best algorithm for all 
members, the other two of each size should use a mix of learning 
algorithms. Do they end up evolving the same specializations? 
Benchmark forks of these teams on Test--are larger teams always 
better?

Create at least five more teams of your optimal team size, but of
members trained individually: one made from forks of champions of 
Train events, another made purely from forks of your generalist 
from Release 9 (before observing Test), another made of similarly 
individually trained generalists but with diverse learning 
algorithms, another made from one novice plus forks of generalists, 
and at least one more made of a sensible mixture of specialists, 
generalists, novices, and/or members from your original teams. 
Benchmark all of these new teams on Test against each other, and 
against forks of your best teams so far (including a Team that 
has already mastered Test).

Explore the weaknesses of your best team. Is it vulnerable to the 
security attacks that worked in Releases 8 and 9? Although no 
single player may be better at adapting to new rules, are there 
some rule sets for which your best team cannot match continuously 
learning individual specialists? If so, what do those rule sets 
have in common (i.e. what kinds of situations might best be 
delegated to less-general intelligence)?  


Potential Mockups
-----------------

Members Tab
~~~~~~~~~~~

 .. figure:: images/Members.png

* The bots combobox offers the name of AI created by the creator 
  of this Team (or Corp) that are not already affiliated with a Team 
  (or Corp); for Corps, also offer “Random” if not already a member. 
  The “Add” button (fa-user-plus) adds a column for the selected AI
* The stat dropdown offers “Job Share” (default), “Rating” (for 
  Teams only) “Accuracy”, “F1”, and “Long-Game” (“Teach”, “Empath”, 
  “Explore Share” and “Debate Share” are added for Corp in 
  :doc:`Corp`). Selecting a value changes what values appear in the 
  table.
* The “Show Player” buttons (fa-address-card-o) navigate to the 
  Stats tab of the associated slayers
* The rows of the table are sorted by cluster ID and the columns 
  are sorted by “All events”. The “Sort by this Row” buttons 
  re-display the table sorted by the values in the associated row; 
  if already sorted by that row, reverse the order. Clicking on any 
  event row also cycles the rows to make the selected row fourth 
  (i.e. moves a block of rows from the top to the bottom, or 
  vice-versa). 
* The “Remove from Team” buttons (fa-trash-o) show only if the stat 
  is “Job Share” and the member’s “Job Share” does not exceed 1% 
  for any event. Clicking it removes the associate member from the 
  Team or Corp and refreshes the table.
* Each stat is a “Show Evolution” button which saves the current 
  record and navigates to the Evolution Page with one row for each 
  member who has ever been in the Team or Corps top five (plus the 
  selected member) with the selected stat and event. For specific 
  events, the hue and luminosity of each button scales from 
  black/blue to the colors of hot metal (see heatmap_style).


Potential Schema
----------------

Hints
-----

::

  def heatmap_style(heat=0, max_heat=100, min_heat=0, hue_offset=200, hue_range=230):
    """CSS styles for heatmap areas. Varies from black (cool) to white, and by hue
    
    Args:
        heat (float): The heat the heatmap area (default is 0)
        max_heat, min_heat (float): The range of possible heats. heat will be 
            be shifted into this range (default is 0-100)
        hue_offset (float): The hue of min_heat (default is 200, blue)
        hue_range (float): The size of the hue range. Set hue_range=0 for constant 
            hue. Set positive hue_range to traverse the color wheel clockwise. 
            Set it >360 to repeat hues (default is 230)

    Returns:
        str: e.g. "background-color:hsl(200, 70%, 10%); color:hsl(0, 100%, 100%);"
    """
    
    min_heat, max_heat = min(min_heat, max_heat), max(min_heat, max_heat)
    norm_heat = (max(min(heat, max_heat), min_heat)-min_heat)/(max_heat-min_heat)
    return ("background-color:hsl({bghue}, 70%, {bglum}%); color:hsl(0, 100%, {txlum}%);".format(
        bghue = str(int((norm_heat*hue_range)+hue_offset)%360),
        bglum = str(int(norm_heat*88)+10),
        txlum = str(int(norm_heat < 0.65)*100) ))



  # Example use:
  import numpy as np
  max_value=np.amax(data)
  cont = "<p style='{0} text-align:center; padding: 1px 0; width:34px; height:28px;'>{1}%</p>"
  rows = []
  for data_row in data:
    row = []
    for value in data_row:
        row.append(widgets.HTML(value=cont.format(heatmap_style(value, max_value), str(value))))
    rows.append(widgets.HBox(row))
  table=widgets.VBox(rows)

