=========================
For Trainers: Creating AI
=========================

Any user can use any *AI*, *Team*, or *Corp* as a tool to help them
:doc:`play <playground>`. On the :doc:`pages <player>` for such tools, 
Trainers see a **Copy** button they can use to duplicate the tool and adjust 
the settings on the new copy to improve it. Finding/creating the best tools 
may be the most powerful way to raise one's :doc:`rankings <game>`.

.. image:: releases/images/CurriculumSimple.png

Many player settings, including *Type* and *Universe*, cannot be changed
once saved. If you want to change those settings, just make a new copy! 

If the player's *Type* is *AI*, then the player page will have a **Curriculum Tab** 
instead of a Creations Tab. Even after an *AI* is saved, its creator
can add recorded matches to its curriculum by specifiying parts of 
tournaments or other players' histories to be studied. Its creator 
can also set the *AI* to automatically learn from its own experiences.
If you ever want a copy of an earlier version of an *AI*, you can "fork"
it from a specified earlier timestamp. Trainers can set parameters for 
the learing algorithm and the following (or can auto-tune them to 
a given curriculum and game):

:math:`\text{Offense}` (vs. Defense):
  :math:`1.0` means maximize wins; :math:`0.0` means minimize losses
  
:math:`\text{Tactical}` (vs. Stategic):
  :math:`1.0` means prioritize the current game; :math:`0.0` means maximize rating; 
  :math:`\text{Tactical}` greater than :math:`\text{Offense}` means 
  never sacrifice a current win for future wins; 
  :math:`\text{Tactical}` greater than :math:`(1 - \text{Offense})` 
  means never take a loss for future wins

:math:`\text{Faith}` (vs. Skeptical):
  :math:`1.0` means confidence in one's data never decays; :math:`0.0` means 
  confidence expires instantly; otherwise confidence decays with the age of
  the data
  
:math:`\text{Introvert}` (vs. Extrovert):  
  :math:`1.0` means practice on simulations as much as possible before acting; 
  :math:`0.0` means learn only via action (so as not to "lose touch" with
  reality)

:math:`\text{Empath}` (vs. Projective):  
  :math:`1.0` means predict others’ moves based on their stats and recent behavior; 
  :math:`0.0` means expect others to do whatever you would do in their situation

:math:`\text{Curious}` (vs. Practical):  
  :math:`1.0` means practice unexpected scenarios as much as possible; :math:`0.0`
  means practice only expected scenarios 

If the player's *Type* is *Team* or *Corp*, then the player page will
have a **Members Tab** instead of a Curriculum or Creations Tab.
The creator can add *AI* as members, and can delete any members that have 
become obsolete. Each individual *AI* has biases. *Teams* and *Corps* 
leverage diversty of biases. Each regular *Team* fields its highest-ranked
member for each event (i.e. specialists). In a *Corp*, multiple *AI* may 
collaborate on each decision via various forms of government.
