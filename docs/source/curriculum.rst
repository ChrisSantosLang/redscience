Curriculum
==========

Not only is the `code <https://github.com/ChrisSantosLang/redscience>`_ 
of redscience opensource, but a number of pre-code resources are 
provided openly as well, and their openness is tested by forming all 
of the resources into a curriculum and testing the ability of diverse 
students (armed with the curriculum) to rebuild redscience as they 
see fit.

Software development is typically divided into jobs or tasks:
 
* **Business Analysis/Ontology**: Anticipate what users will desire 
  as the platform evolves. Decide what to calculate/monitor, and how 
  to define entities (e.g. games, users, bots, etc). Document the 
  workflows to be tested.
* **UI Design**: Anticipate the diversity of direct users 
  (differences in training, devices, interests, etc.) Choose 
  phrasings, colors, shapes/fonts, sizes, patterns, widgets, layouts
  and navigation. Document mock-ups and the wording of messages.
* **Database Architecture**: Anticipate potential reuse of 
  information. Choose names for database tables and columns, and 
  document their definitions and indexes.
* **Software Architecture**: Anticipate code 
  writing/fixing/enhancing/evolving. Establish code languages and 
  tools for editing, debugging, deploying, and versioning code. 
  Divide the planned code into logical (reusable) units, and create 
  technical documentation and automated tests for each.
* **Pseudocoding**: Rewrite the documentation of each code unit as 
  ordered “To do” comments. Identify code units to be employed from 
  existing code libraries.
* **Coding**: Write, test, debug, and deploy the code.

This curriculum assumes that you might wish only to code. You can expect 
it to provide the completed deliverables for all other tasks. 
The "How to" articles in this curriculum will walk you through how to 
use those deliverables.

In typical development, coding reveals opportunities to improve the 
other deliverables. You are welcome to modify any deliverable (as one
might do in typical development), or entirely rebuild it from scratch. 
Be aware, however, that deliverables encountered in typical development
have had less opportunity for refinement, since typical projects have
never been coded before. Typical development might be more "messy" 
than what you would experience while following this curriculum.

Pseudocoding is usually done by coders. It is provided in this project 
because we assume that you want to be told about (and get practice 
with) widely-used existing code libraries and code structures. You 
don’t have to follow the suggestions of the pseudocode. If you have 
a better idea, please share it with us, so we can suggest it to future 
coders.

This project is divided into :doc:`releases`. Each builds upon the previous. 
This curriculum provides Requirements, a Testing Plan, and Potential 
Mockups for each Release. Together, these documents communicate the 
scope of the Release.  

This curriculum also includes a number of "How to" articles which 
step through the beginning of the first Release. The curriculum will
provide plenty of opportunity to get creative and prove your coding 
skills later, but our first priority is to make sure we are on the 
same page, so feel free to follow the "How to" articles to the letter.

Start by reviewing the Requirements, a Testing Plan, and Potential 
Mockups for the first Release (:doc:`commandline`), then begin 
with :doc:`devenvironment`.


.. toctree::
   :maxdepth: 4

   commandline
   devenvironment
   releases

