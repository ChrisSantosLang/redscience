===============================
1.11 General Intelligence Games
===============================

Requirements
------------



Acceptance Test Plan
--------------------

Test each of the clickable elements and test that it displays 
appropriate errors for invalid entries. Compare all the rule sets 
from :doc:`games`, then try to build more games that do not fit the 
larger clusters (e.g. by following the patterns of more unique 
sets). Once you believe you have fleshed-out the space of rule sets, 
define six Training Olympics which span that space (e.g. including 
RockPaperScissors and events from each cluster), but which do not 
overlap. Make the first Training Olympics (called "Test") have a 
minimum set of events to span the spaces. Call the other Training 
Olympics "Train1" - "Train5". Use your best techniques to train a 
player on "Train1" - "Train5" consecutively (never observing the 
events in "Test"). Compare its learning curves to those of 
specialists--does it learn more slowly? Are the curves different for 
later training sets? Benchmark that player on Test and on each 
individual event in Test. Can it play well against you? How does it 
fare against Random, the standard specialists, and reigning champions?

Potential Mockups
-----------------

Events Tab
~~~~~~~~~~

 .. figure:: images/Events.png

* The name text field does not accept whitespace, ‘\*’, ‘(‘, or ‘)’, 
  but automatically prepends ‘\*’ when saving (if there is no ‘\*’)
* The "Save" button is replaced with a ”Copy” button once the 
  Olympics is saved.
* The event combobox and “Add Event” button (fa-plus) is available 
  only on unsaved Olympics. The combobox offers the name of each 
  event. Clicking the button adds a row for the selected event 
  (if it isn’t already added).
* The “Delete Event” buttons (fa-trash-o) are visible only on unsaved 
  Olympics. Clicking one deletes the associated row.
* The “Show Leaderboard” buttons (fa-th-list) save the Olympics and 
  navigate to the Leaderboad tab of the associated event

Compare Tab (for Event)
~~~~~~~~~~~~~~~~~~~~~~~

 .. figure:: images/Compare.png

* The events combobox offers the names of all events not already 
  listed below. The “Add to Comparison” button (fa-plus) adds rows 
  for the selected event and every other event that has already been 
  compared to the selected event.
* The “Show Tree” button (fa-sitemap) appears only after there are 
  cluster IDs. Clicking it navigates to the Dendrogram page for the 
  clusters.
* The table is sorted by Uniqueness then by Cluster ID. The “Sort 
  by this Column” buttons re-display the table sorted by the values 
  in the associated column; if already sorted by that column, then 
  reverse the order.
* The “Start Comparison” button (fa-balance-scale) disables the 
  display, and calculates the missing values for all checked rows 
  (showing each value when calculated). The display is reenabled 
  when there are no more missing values (or when the user selects
  “Abort”). 
* The “Create Olympics” button (fa-flask) opens the Events tab of a 
  new Olympics (Game Factory) with the checked events already 
  selected.
* The “Show Leaderboard” buttons (fa-th-list) navigate to the 
  Leaderboad tabs of the associated events

Dendrogram Page
~~~~~~~~~~~~~~~

 .. figure:: images/Dendrogram.png
 
   Shown as of :doc:`corps` (to anticipate the evolution of the page)
   The dropdowns and ratings show only if launched for a Team or 
   Corp. 
   
* If this page is launched for a Team or Corp, then the player 
  dropdown offers the members of that Team or Corp.
* The score dropdown offers *Accuracy*, *F1*, *Long-Game*, *TCH* 
  and *EMP*
* Clicking on an event name launches the Leaderboard tab for that 
  event.
* Clicking on the score to the right of an event name launches the 
  Evolution page for that event with the selected Player and Score


 
Potential Schema
----------------

