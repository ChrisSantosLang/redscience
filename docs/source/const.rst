const module
============

.. automodule:: const

General Constants
-----------------

Color
`````

.. autoclass:: Color
   :members:
   :undoc-members:
   :show-inheritance:
    
Command
```````

.. autoclass:: Command
   :members:
   :undoc-members:
   :show-inheritance:
    
Layout
``````

.. autoclass:: Layout
   :members:
   :undoc-members:
   :show-inheritance:

Player Constants
-----------------

Player
``````

.. autoclass:: Player
   :members: VERSIONS
   :show-inheritance: 

PlayerType
``````````

.. autoclass:: PlayerType
   :members:
   :undoc-members:
   :show-inheritance:
    
PlayerColor
```````````

.. autoclass:: PlayerColor
   :members:
   :undoc-members:
   :show-inheritance:   

DefaultName
```````````

.. autoclass:: DefaultName
   :members:
   :undoc-members:
   :show-inheritance:
    
    
Piece Constants
---------------

Marker
``````

.. autoclass:: Marker
   :members:
   :undoc-members:
   :show-inheritance:
    
PieceRules
``````````

.. autoclass:: PieceRules
   :members: VERSIONS, RESERVES_STR, STRS
   :show-inheritance:
    
Directions
``````````

.. autoclass:: Directions
   :members:
   :undoc-members:
   :show-inheritance:
    
Game Constants
--------------

Game
````

.. autoclass:: Game
    :members: VERSIONS, RULES, AXES, MARKER_SIZE
    :show-inheritance:

PlayersOption
`````````````

.. autoclass:: PlayersOption
   :members:
   :undoc-members:
   :show-inheritance:
    
ColorOption
```````````

.. autoclass:: ColorOption
   :members:
   :undoc-members:
   :show-inheritance:
    
BoardOption
```````````

.. autoclass:: BoardOption
   :members:
   :undoc-members:
   :show-inheritance: 
    
CheckOption
```````````

.. autoclass:: CheckOption
   :members:
   :undoc-members:
   :show-inheritance:
    
StalemateOption
```````````````

.. autoclass:: StalemateOption
   :members:
   :undoc-members:
   :show-inheritance: 
    
Move Constants
--------------

Move
````

.. autoclass:: Move
   :members:
   :undoc-members:
   :show-inheritance:
    
Outcome
```````

.. autoclass:: Outcome
   :members:
   :undoc-members:
   :show-inheritance: 
   
Language Functions
------------------

setlang()
`````````

.. autofunction:: setlang

format_datetime()
`````````````````

.. autofunction:: format_datetime

format_decimal()
````````````````

.. autofunction:: format_decimal

format_list()
`````````````

.. autofunction:: format_list

format_percent()
````````````````

.. autofunction:: format_percent


format_format_unit()
````````````````````

.. autofunction:: format_unit

Versioning Functions
--------------------

setvers()
`````````

.. autofunction:: setvers

ALL
```

.. py:data:: const.ALL
  :value: (-inf,+inf)
A shortcut for the portion.interval.Interval_ that contains all (e.g. versions)

from_version()
``````````````

.. autofunction:: from_version

ntversions()
````````````

.. autofunction:: ntversions
