======================
1.4 Secure Tic-Tac-Toe
======================

Requirements
------------

Modify the Statistical Tic-Tac-Toe program to give specific users 
ownership of specific records. Add four more security levels, 
convert all but one existing Admin to a Persona of that one Admin,
and consolidate all Random players into one (do not permit creation 
of additional random players):

Anonymous:
  Has no stats, and can choose only non-human players for player 
  slots other than itself. All anonymous users share a single anonymous 
  player record

Persona:
  Has stats, but no email address (i.e. no one can log-in as a Persona).

Creator:
  Can edit the name, avatar, and email address of their own player 
  record and any player record they created. They are the only ones 
  who can view their email address. They can create up to 3 Personas 
  (via copy of any human), upto 15 new games (via Copy in Release 5). 
  They can choose Personas they created for player slots other than 
  the first. Their security can be upgraded by any Admin.
  
Trainer:
  Additionally able to create unlimited games and players of any type, 
  and to create and run tournaments and comparisons of rule sets. This 
  security must be restricted because Trainers could create large 
  amounts of data quickly. A Trainer can stop the Playground clock if 
  all players are either non-human or created by the Trainer (in this 
  case, the match is ignored in updating skill-level. Their security 
  can be upgraded by any Admin.
  
Admin:
  Maximum permissions

All users start logged in as Anonymous, but can create a new Creator 
account, and/or log in to an existing Creator, Trainer, or Admin account 
(which will be in the “Public Universe)”. To log in, the user provides 
an email address, then a temporary code is emailed to that address. When 
first creating a player other than Creator, the user may change the 
defaulted Universe to a new Universe (with a unique new name) or to an 
existing Universe in which the creator of the new player already has a 
Persona. A player’s Universe (like type) is forever locked once saved.

Users can invite "Next available" or named players of the same Universe 
as the first player to play Tic-Tac-Toe. Play will be delayed until a 
matching invitation is issued by the other player(s)--non-human players 
will issue matching invitations as soon as they can (Random and Standard 
AI can issue one immediately, but continuously-learning or experimenting 
bots may have other matches they need to complete first. When inviting a 
human to play, the invitation automatically go to the same-named Persona 
of the matching Universe (automatically create one, if necessary).

Acceptance Test Plan
--------------------

Test each of the clickable elements and test that it displays 
appropriate errors for invalid entries. Confirm the special security 
permissions.

Potential Mockups
-----------------

To get temporary login token emailed::

  redscience login {email}
  

Change User Page
~~~~~~~~~~~~~~~~

 .. figure:: images/ChangeUser.png

* The game dropdown offers one option for each combination of 
  game this player has played and form of augmentation used. 

* The “Sign-out” button (fa-sign-out) changes the user to Anonymous
* The “Send Code” button (fa-paper-plane-o) sends the temporary 
  code to the entered email address and changes the avatar to the 
  one associated with that email address
* The “Go” button (fa-arrow-right) uses the entered temporary code 
  to login to the account associated with the email address. If 
  there is no account associated with that address, create a 
  Creator player 

Creations Tab
~~~~~~~~~~~~~

 .. figure:: images/Creations.png

  Shown as of :doc:`generalintelligence` (to anticipate the 
  evolution of the page). 

* Sorted by Usage (highest on top) = 100 * (number of mentions in game 
  sets or in games not in sets) / (days since created)
* The “Show Player” buttons (fa-address-card-o) navigate to the Stats 
  tab of the associated players

