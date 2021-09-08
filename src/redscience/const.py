#!/usr/bin/env python3
"""Contains redscience constants plus functions for internationalization.

Most constants in this module are encoded as a ``Category`` (see the 
``category`` module) or as a ``NamedTuple``. Each displays in the
locale set via ``setlang()`` (provided an .mo file for that locale can 
be found in the appropriate folder). See the ``babelwrap`` module 
regarding internationalization. Use ``setrelease()`` to change the 
release (and thus *which* Category members display).

Examples::

  ttt=Game()
  print(ttt.RULES)
  print(Command.QUIT)
  ipywidgets.Dropdown(options=sorted(Command), value=Command.QUIT)
  ipywidgets.Button(
      description=Command.QUIT,
      tooltip=Command.QUIT.TOOLTIP,
      icon=Command.QUIT.ICON,
  )

  import matplotlib.pyplot as plt
  fig = plt.figure(1,(
      Layout.FIGURE_HEIGHT,
      Layout.FIGURE_WIDTH,
  ))
  ax = ttt.AXES(fig)
  ax.scatter(
      x = 1,
      y = 1,
      c = Color.WHITE.HEX,
      marker = Marker.CIRCLE.CODE,
      edgecolors = Color.BLACK.HEX,
  )
  plt.show()

"""

import collections
import enum
import functools
import itertools
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    NamedTuple,
    Optional,
    Tuple,
    Union,
)

import babelwrap
import category
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np

#!pip install portion
#import portion as P

_release: Optional[Tuple[Union[int,str], ...]] = None  # for type hint 

# Keep theses before setting Enums, so their values will be in the
# language from which they can be translated
def _(message: str) -> str:
    """
    The name to be used for the function that returns the 
    localized version of a str. Defined here only 
    temporarily for type hints (to be redefined elsewhere).
    """
    return message


def format_list(items: List[Any]) -> str:
    """
    The name to be used for the function that returns the 
    localized string to describe a list. Defined here only 
    temporarily for type hints (to be redefined elsewhere).
    """
    return str(items)


def release(name:str, min_parts:int=3) -> Tuple[Union[int,str], ...]:
    """Translates a release name into sortable tuples. E.g.:
    
    >>> release("1.0.1")
    (1, 0, 1)
      
    Args:
        name (str): The release name (e.g. "1.0.1.alpha")
        min_parts (int): The minimum parts for the tuple. Default is 3.
        
    Returns:
        A tuple with one part per dot-delimitted part of the name (padded with
        zeros if necessary to achieve min_parts). Unlike strings, the tuples 
        will sort correctly (the integer parts will be integers).
    """
    parts = name.split(".")
    parts.extend(["0"]*(min_parts-len(parts)))
    return tuple(int(part) if part.isnumeric() else part for part in parts)
  
def isreleased(obj: Any)->bool:
    """Tests whether an object is released. E.g.:
    
    >>> isreleased(Color.BLACK)
    True
    
    Args:
        obj (object): The object in question
        
    Returns:
        True if the object is in the release that was set
        
    Note:
        This function assumes that objects that might not be release have an
        attribute named "RELEASES" containing all the releases in which to 
        return True.
    """
    return not hasattr(obj, "RELEASES") or _release in obj.RELEASES
  
def setrelease(name: Optional[str]=None)->str:
    """Get or set the release. E.g.::
    
    >>> setrelease("1.1.0")
    (1, 1, 0)
    
    Args:
        name (str): The name of the release to set. If "", setrelease will set to 
            the version named in setup.cfg. If None, the previously set 
            release will be retained. Default to None.
        
    Returns:
        The set release as a tuple.
        
    Note:
        This function stores the release in _release
    """
    global _release
    if _release and name==None: return _release
    if name and len(name) > 0: 
        _release = release(name)
    else:
        # get from setup.cfg
        _release = release("1.0.0")
    return _release
  
setrelease()
 

class Color(category.Categorized):
    """Color used in a game. E.g.::

        Color.BLACK

    Attributes:
        STR (str): A localized name. How the Color prints.
        HEX (str): A hex code to communicate the Color to computers.
    """

    _ignore_ = "ColorValue"

    class ColorValue(NamedTuple):
        STR: str
        HEX: str

    # TRANSLATOR: Color of game piece as in "Move: Black circle to (2,1)"
    BLACK = ColorValue(STR=_("black"), HEX="#000000")

    # TRANSLATOR: Color of game piece as in "Move: White circle to (2,1)"
    WHITE = ColorValue(STR=_("white"), HEX="#ffffff")

    # TRANSLATOR: Color of game piece as in "Move: Pink circle to (2,1)"
    PINK = ColorValue(STR=_("pink"), HEX="#ff81c0")

    # TRANSLATOR: Color of game piece as in "Move: Yellow circle to (2,1)"
    YELLOW = ColorValue(STR=_("yellow"), HEX="#ffff14")

    # TRANSLATOR: Color of game piece as in "Move: Orange circle to (2,1)"
    ORANGE = ColorValue(STR=_("orange"), HEX="#fdaa48")

    # TRANSLATOR: Color of game piece as in "Move: Blue circle to (2,1)"
    BLUE = ColorValue(STR=_("blue"), HEX="#95d0fc")

    # TRANSLATOR: Color of game piece as in "Move: Purple circle to (2,1)"
    PURPLE = ColorValue(STR=_("purple"), HEX="#bf77f6")

    # TRANSLATOR: Color of game piece as in "Move: Green circle to (2,1)"
    GREEN = ColorValue(STR=_("green"), HEX="#96f97b")

    # TRANSLATOR: Color of game piece as in "Move: Gray circle to (2,1)"
    GRAY = ColorValue(STR=_("gray"), HEX="#929591")


# PlayerColor = category.category(*Color[0:4], name="PlayerColor")  # type: ignore[misc]


# class Layout(enum.IntEnum):
#     """Layout constants. E.g.::

#       Layout.POINTS_PER_INCH
#     """

#     FIGURE_WIDTH = 5
#     FIGURE_HEIGHT = 5
#     POINTS_PER_INCH = 54
#     MARKER_MARGIN = 8


# class Command(category.Categorized):
#     """Command from user to the application. E.g.::

#         Command.NEW

#     Attributes:
#         STR (str): A localized name. How the Command prints.
#         KEY (str): A localized shortcut key. 
    
#     Each Command tests == to its key as well as to itself. In English::
    
#         Command.NEW == "n"
#     """

#     _ignore_ = "CommandValue"

#     class CommandValue(NamedTuple):
#         STR: str
#         KEY: str

#     # TRANSLATOR: This is the command to start a new game (e.g. button text).
#     # TRANSLATOR: This is the shortcut key to start a new game.
#     # It should match the key listed in the prompt.
#     NEW = CommandValue(STR=_("Play New"), KEY=_("n"))

#     # TRANSLATOR: This is the command to end the application (e.g. button text).
#     # TRANSLATOR: This is the shortcut key to end the application.
#     # It should match the key listed in the prompt.
#     QUIT = CommandValue(STR=_("Quit"), KEY=_("q"))

#     # TRANSLATOR: This is the command to reverse last user input (e.g. button text).
#     # TRANSLATOR: This is the shortcut key to back-up by one user input.
#     # It should match the key listed in the prompt.
#     UNDO = CommandValue(STR=_("Back"), KEY=_("z"))

#     def __eq__(self: "Command", other) -> bool:
#         return (
#             other.lower() == self.KEY
#             if type(other) is str
#             else category.Categorized.__eq__(self, other)
#         )

#     def __ne__(self: "Command", other) -> bool:
#         return not self.__eq__(other)


# class PlayersOption(category.Categorized):
#     """Category of game by number/type of players. E.g.::

#         PlayersOption.TWO

#     Attributes:
#         STR (str): A localized name. How the PlayerOption prints.
#         NUM (int): The number of regular players.
#     """

#     _ignore_ = "PlayersValue"

#     class PlayersValue(NamedTuple):
#         STR: str
#         NUM: int

#     # TRANSLATOR: Category to describe games with two regular players
#     TWO = PlayersValue(STR=_("2-Player"), NUM=2)

#     # TRANSLATOR: Category to describe games with three regular players
#     THREE = PlayersValue(STR=_("3-Player"), NUM=3)


# class Marker(category.Categorized):
#     """Category of game piece by what marker is use to display it. E.g.::
    
#         Marker.CIRCLE

#     Attributes:
#         STR: A localized str to name the marker. How the Marker prints.
#         CODE: The str used in pyplot for the marker.
#     """

#     _ignore_ = "MarkerValue"

#     class MarkerValue(NamedTuple):
#         STR: str
#         CODE: str

#     # TRANSLATOR: Description of the pyplot marker
#     CIRCLE = MarkerValue(STR=_("circle"), CODE="o")


# class StalemateOption(category.Categorized):
#     """Category of game by stalemate end it. E.g.::
    
#         StalemateOption.DRAW

#     Prints localized str.
#     """

#     # TRANSLATOR: Game rule that the game ends in a draw if there is a stalemate
#     DRAW = _("stalemate draws")


# class ColorOption(category.Categorized):
#      """Category of game by how it treats colors. E.g.::
    
#         ColorOption.ASSIGNED

#     Prints localized str.
#     """

#     # TRANSLATOR: Game rule that each player is assigned their own unique color
#     ASSIGNED = _("Assigned Colors")


# class BoardOption(category.Categorized):
#     """Category of game board. E.g.::
    
#         BoardOption.HASH

#     Attributes:
#         STR: A localized str to name the marker. How the BoardOption prints.
#         CODE: The str used in pyplot for the marker.
#     """

#     _ignore_ = "BoardValue"

#     class BoardValue(NamedTuple):
#         STR: str
#         AX: Callable[[matplotlib.figure.Figure, tuple], matplotlib.axes.Axes]

#     def hash_board(fig: matplotlib.figure.Figure, dims: tuple) -> matplotlib.axes.Axes:
#         """Tic-Tac-Toe board"""
#         rows, cols = dims[0], dims[1]
#         gs = fig.add_gridspec(1, 1)
#         ax = fig.add_subplot(gs[0, 0])
#         ax.patch.set_alpha(0.0)
#         ax.spines["top"].set_visible(False)
#         ax.spines["bottom"].set_visible(False)
#         ax.spines["right"].set_visible(False)
#         ax.spines["left"].set_visible(False)
#         ax.xaxis.set_ticks_position("none")
#         ax.xaxis.set_ticklabels([""])
#         ax.yaxis.set_ticks_position("none")
#         ax.yaxis.set_ticklabels([""])
#         ax.grid(True)
#         ax.xaxis.set_ticks(np.arange(0.5, cols + 0.5, 1))
#         ax.yaxis.set_ticks(np.arange(0.5, rows + 0.5, 1))
#         plt.xlim(cols + 0.5, 0.5)
#         plt.ylim(0.5, rows + 0.5)
#         return ax

#     # TRANSLATOR: The type of board used for Tic-Tac-Toe, as in "Played on a hash (3,3)"
#     HASH = BoardValue(STR=_("a hash"), AX=hash_board)


# class Directions(category.Categorized):
#     """Categories of ways in which to move or build in square-tiled space. E.g:

#       Directions.DIAGONAL(2)  # returns [(1,1), (1,-1), (-1,1), (-1,-1)]
#       Directions.DIAGONAL.call.cache_info()  # to get cache_info

#     Args:
#       dimensions: The (int) number of dimensions in the space

#     Attributes:
#       str: A localized str to name the type of directions. How the Directions
#         prints.
#       call: The bound method that yields the tuples.

#     Returns:
#       A list of relative coordinates (tuples)
#     """

#     _ignore_ = "DirectionsValue"

#     class DirectionsValue(NamedTuple):
#         STR: str
#         CALL: Callable[[int], tuple]

#     @functools.lru_cache(maxsize=8)
#     def any_direction(self: "Directions", dimensions: int):
#         zero = tuple([0] * dimensions)
#         unfiltered = itertools.product([1, 0, -1], repeat=dimensions)
#         return tuple([np.array(x) for x in unfiltered if x != zero])

#     @functools.lru_cache(maxsize=8)
#     def orthogonal(self: "Directions", dimensions: int):
#         return tuple(np.identity(dimensions, dtype=int))

#     @functools.lru_cache(maxsize=8)
#     def diagonal(self: "Directions", dimensions: int):
#         orthogonals = list(map(tuple, self.orthogonal(dimensions)))
#         return tuple(
#             [x for x in self.any_direction(dimensions) if tuple(x) not in orthogonals]
#         )

#     @functools.lru_cache(maxsize=8)
#     def knight(self: "Directions", dimensions: int):
#         spots = []
#         for spot in itertools.product([2, 1, 0, -1, -2], repeat=dimensions):
#             inring = (spot.count(2) + spot.count(-2)) == 1
#             orthogonal = spot.count(0) >= (dimensions - 1)
#             if inring and not orthogonal:
#                 spots.append(np.array(spot))
#         return tuple(spots)

#     # TRANSLATOR: Category of directions in which chess queen can move
#     ANY = DirectionsValue(STR=_("any direction"), CALL=any_direction)

#     # TRANSLATOR: Category of directions in which chess bishop can move
#     DIAGONAL = DirectionsValue(STR=_("diagonal"), CALL=diagonal)

#     # TRANSLATOR: Category of directions in which chess rook can move
#     ORTHOGONAL = DirectionsValue(STR=_("orthogonal"), CALL=orthogonal)

#     # TRANSLATOR: Category of directions in which chess knight can move
#     KNIGHT = DirectionsValue(STR=_("knight move"), CALL=knight)


# class Outcome(category.Categorized):
#     """Function to apply localized formatting to strings. E.g:

#       Outcome.VICTORY(players=["Player 1"])

#     Args:
#       **kwargs: a string for each bookmark in the str

#     Returns:
#       The localized formated string.
#     """

#     _ignore_ = "FormatValue"

#     class FormatValue(NamedTuple):
#         STR: str
#         FORMAT: str
#         CALL: Callable[["Outcome", List[str]], str]

#     def formatter(self: "Outcome", players: List[str]) -> str:
#         return self.FORMAT.format(players=format_list(players))

#     # TRANSLATOR: Labels {winners} as the winner(s) of a game
#     #  e.g. "Victory: Player 1 and Player 3"
#     VICTORY = FormatValue(
#         STR=_("Victory"),
#         FORMAT=_("Victory: {players}"),
#         CALL=formatter,
#     )


# class CheckOption(category.Categorized):
#     """Game rules checked at the end of each move. Prints localized str. """

#     _ignore_ = "PatternCheck"

#     class PatternCheck(NamedTuple):
#         STR: str
#         PATTERN: str
#         DIRECTIONS: Directions
#         OUTCOME: Outcome

#     # TRANSLATOR: Game rule to award the win to any player that aranges three
#     # pieces of the same color in a row
#     THREE_SAME_COLOR_IN_ROW_WINS = PatternCheck(
#         STR=_("first 3-same-color-in-a-row wins"),
#         PATTERN="CCC",
#         DIRECTIONS=Directions.ANY,
#         OUTCOME=Outcome.VICTORY,
#     )


# class PieceRules(NamedTuple):
#     """Rules for a type of piece in a game. E.g.:

#         PieceRules(INITIAL_RESERVES=(5,4))

#     Attributes:
#         INITIAL_RESERVES: A tuple indicating the number in initial reserves
#             of each color, e.g. (5, 4) means 5 of the first color, and 4 of
#             the second.
#     """

#     INITIAL_RESERVES: Tuple[int, ...]

#     @property
#     def RESERVES_STR(self: "PieceRules") -> str:
#         """A constant localized str describing initial reserves for the
#         piece. E.g.:

#         piece.RESERVES_STR
#         """
#         by_color = []
#         for index in range(len(self.INITIAL_RESERVES)):
#             # TRANSLATOR: Part of a list of amounts of game pieces.
#             # e.g. "5 black" in "5 black and 4 white start in reserve"
#             by_color.append(
#                 _("{number} {color}").format(
#                     number=self.INITIAL_RESERVES[index],
#                     color=str(Color[index]).lower(),  # type: ignore[misc]
#                 ),
#             )

#         # TRANSLATOR: The rule for how many to have in reserve when a game
#         # begins.. E.g. "5 black and 2 white start in reserve"
#         return _("{list} start in reserve").format(list=format_list(by_color))

#     @property
#     def STRS(self: "PieceRules") -> Tuple[str, ...]:
#         """Get tuple of strings describing the rules for the piece. E.g.:

#         piece.STRS
#         """
#         lines = [self.RESERVES_STR]
#         return tuple(lines)

#     def __str__(self: "PieceRules") -> str:
#         return "/n".join(self.STRS)


# class Game(NamedTuple):
#     """A game definition. E.g.:

#         Game()  # To use all defaults (i.e. Tic-Tac-Toe)

#     Attributes:
#         PLAYERS: If specified, determines the PlayersOption. Default is 2-Player.
#         COLOR: If specified, determines the ColorOption. Default is Assigned
#             Colors.
#         BOARD: If specified, determines the BoardOption. Default is hash.
#         DIMENSIONS: If specified, determines the dimensions of the board as a
#             tuple of integers. Default is (3,3).
#         PIECES: If specified, determines piece-specific rules as a tuple of
#             PieceRules. Default is to have only one type of piece (circle) with
#             5 black and 4 white starting in reserve.
#         MOVE_CHECKS: If specified, list rules that are checked at the end of
#             each move as tuple of CheckOptions. Can be None. Default is to award
#             the win to any player that gets three of the same color in a row.
#         STALEMATE: If specified, determines the StalemateOption. Default is that
#             stalemate results in a draw.
#     """

#     PLAYERS: PlayersOption = PlayersOption.TWO
#     COLOR: ColorOption = ColorOption.ASSIGNED
#     BOARD: BoardOption = BoardOption.HASH
#     DIMENSIONS: Tuple[int, ...] = (3, 3)
#     PIECES: Tuple[PieceRules, ...] = (PieceRules(INITIAL_RESERVES=(5, 4)),)
#     MOVE_CHECKS: Union[Tuple[()], Tuple[CheckOption, ...]] = (
#         CheckOption.THREE_SAME_COLOR_IN_ROW_WINS,
#     )
#     STALEMATE: StalemateOption = StalemateOption.DRAW

#     @property
#     def STRS(self: "Game") -> Tuple[str, ...]:
#         """A constant tuple of localized strings describing the game. E.g:

#         game.STRS
#         """
#         lines = []
#         # TRANSLATOR: Line defining a game board e.g. "Played on hash (3,3)" for
#         # Tic-Tac-Toe where {board} is "hash" and {dimensions} is "(3,3)"
#         lines.append(
#             _("Played on {board} {dimensions}").format(
#                 dimensions=str(self.DIMENSIONS),
#                 board=str(self.BOARD),
#             )
#         )
#         lines.append(str(self.PLAYERS))
#         lines.append(str(self.COLOR))
#         for index in range(len(self.PIECES)):
#             # TRANSLATOR: Line defining rules for a type of game piece/card
#             # e.g. "Circle: Immobile, 5 black and 4 white start in reserve"
#             lines.append(
#                 _("{shape}: {rules}")
#                 .format(
#                     shape=str(Marker[index]),  # type: ignore[misc]
#                     rules=format_list(list(self.PIECES[index].STRS)),
#                 )
#                 .capitalize()
#             )
#         for rule in self.MOVE_CHECKS:
#             lines.append(str(rule).capitalize())
#         lines.append(str(self.STALEMATE).capitalize())
#         return tuple(lines)

#     @property
#     def RULES(self: "Game") -> str:
#         """A constant localized str describing the move checks and stalemate
#         rules. E.g:

#         game.RULES
#         """
#         rule_list: List[Union[CheckOption, StalemateOption]] = list(self.MOVE_CHECKS)
#         rule_list.append(self.STALEMATE)
#         # TRANSLATOR: Labels {rules} as rules of a game
#         #  e.g. "Rules: First 3-same-color-in-a-row wins and stalemate draws"
#         return _("Rules: {rules}").format(
#             rules=str(format_list(rule_list)).capitalize(),
#         )

#     def __str__(self: "Game") -> str:
#         return "\n".join(self.STRS)

#     def AXES(self, fig: matplotlib.figure.Figure) -> matplotlib.axes.Axes:
#         """A constant matplotlib.axes.Axes for this game. E.g.:

#             game.AXES(fig=plt.figure(1,(FIGURE_HEIGHT, FIGURE_WIDTH)))

#         Args:
#             fig: The Matplotlib.figure.Figure of the Axes
#         """
#         return self.BOARD.AX(fig, self.DIMENSIONS)

#     @property
#     def MARKER_SIZE(self) -> float:
#         """MARKER_SIZE: A constant int size for markers in this game"""
#         figure_max = max(Layout.FIGURE_HEIGHT, Layout.FIGURE_WIDTH)
#         spot_size = figure_max / max(self.DIMENSIONS)
#         return (spot_size * Layout.POINTS_PER_INCH - Layout.MARKER_MARGIN) ** 2


# class DefaultName(category.Categorized):
#     """Default names for players. Prints localized str. """

#     # TRANSLATOR: Default name for a player in a game (independent of order)
#     PLAYER_ONE = _("Player 1")

#     # TRANSLATOR: Default name for a player in a game (independent of order)
#     PLAYER_TWO = _("Player 2")

#     # TRANSLATOR: Default name for a player in a game (independent of order)
#     PLAYER_THREE = _("Player 3")

#     # TRANSLATOR: Default name for a player in a game (independent of order)
#     PLAYER_FOUR = _("Player 4")


# class PlayerType(category.Categorized):
#     """Types of players. Prints localized str. """

#     # TRANSLATOR: A type of player in a game
#     HUMAN = _("Human")


# class Player(NamedTuple):
#     """A player definition. E.g.:

#         Player()  # To use all defaults (i.e. human)

#     Attributes:
#         TYPE: If specified, determines the PlayerType. Default is Human.
#     """

#     TYPE: PlayerType = PlayerType.HUMAN


# class Placement(NamedTuple):

#     TO: Tuple[int, ...]
#     COLOR: Color = Color.BLACK
#     MARKER: Marker = Marker.CIRCLE

#     def __str__(self: "Placement") -> str:
#         # TRANSLATOR: Names a placement in a game e.g. "Black circle to (1,2)"
#         return (
#             _("{color} {shape} to {destination}")
#             .format(color=self.COLOR, shape=self.MARKER, destination=self.TO)
#             .capitalize()
#         )


# class Jump(NamedTuple):

#     FROM: Tuple[int, ...]
#     TO: Tuple[int, ...]

#     def __str__(self: "Jump") -> str:
#         # TRANSLATOR: Names a move in a game e.g. "(2,3) to (1,2)
#         return _("{origin} to {destination}").format(
#             origin=self.FROM, destination=self.TO
#         )


# class Move(category.Categorized):
#     """A type of move in a game. Prints localized str. Examples:

#       Move.PASS
#       Move.PLACE(COLOR=Color.WHITE, MARKER=Marker.CIRCLE, TO=(2,3))
#       Move.JUMP(FROM=(1,1), TO=(2,3))

#     Attributes:
#       TO (in JUMP and PLACE only): Tuple of integers specifying the
#         destination coordinates.
#       COLOR (in PLACE only): Color enum specifying the color to be placed.
#         Default is Color.BLACK
#       MARKER (in PLACE only): Marker enum specifying the shape to be placed.
#         Default is Marker.CIRCLE
#       FROM (in JUMP only): Tuple of integers specifying the origin coordinates.
#     """

#     _ignore_ = "MoveValue"

#     class MoveValue(NamedTuple):
#         STR: str
#         CALL: Any

#     # TRANSLATOR: Move in a game when the player forfeits their turn
#     PASS = _("Pass")

#     # TRANSLATOR: Move in a game when the player adds a piece or card
#     PLACE = MoveValue(STR=_("Place from reserves"), CALL=Placement)

#     # TRANSLATOR: Move in a game from one spot to another
#     JUMP = MoveValue(STR=_("Reposition"), CALL=Jump)

#     # TRANSLATOR: Move in a game when the player offers a voluntary draw
#     OFFER = _("Offer to draw")

#     # TRANSLATOR: Move in a game when the player accepts an offer to draw
#     AGREE = _("Agree to draw")

#     # TRANSLATOR: Move in a game when the player rejects an offer to draw
#     REFUSE = _("Refuse to draw")


# Delay this set to default language until after all constants are declared;
# otherwise the strings will get translated upon declaration, and that will
# prevent us from changing language later (since we will have lost the original
# strings)
# setlang = babelwrap.SetLang(globals())
# setlang("")

# defaults['misc']['title'] = _('Command Line Tic-Tac-Toe')

# defaults['misc']['turn_label'] = _('Turn: {player_name}')
# defaults['misc']['rules_label'] = _('Rules: {rule_or_list}')
# defaults['misc']['victory_label'] = _('Victory: {victor_or_list}')
# _("{color}{piece_type} to {coordinates}")

# defaults['misc']['prompt'] = _('What\'s your move? (\'#,#\' or q/z/n for quit/undo/new game)')
# defaults['misc']['close'] = _('c')
# defaults['misc']['undo'] = _('z')
# defaults['misc']['restart'] = _('s')
# defaults['misc']['illegal'] = _('That is not a legal option.')
# defaults['misc']['error'] = _('Error in program')
# defaults['misc']['draw'] = _('Draw')


# defaults['misc']['colors'] = [ 'xkcd:black', 'xkcd:white', 'xkcd:pink',
#     'xkcd:yellow' ]
# defaults['misc']['color_names'] = [ _('black'), _('white'), _('pink'),
#     _('yellow') ]
# defaults['misc']['markers'] = [ 'o', 'p', 'X', 'P', '^', '*' ]
# defaults['misc']['shapes'] = [ _('circle'), _('pentagon'), _('X'),
#     _('cross'), _('triangle'), _('star') ]
# defaults['shape'] = { '__type__' : 'shape',
#         'mobility' : _('no movement'),
#         'power' : _('no power'),
#         'initial_reserves' : [5,4] }
# defaults['phase'] = { '__type__': 'phase',
#         'pass' : _('no voluntary pass') }
# defaults['rules'] = {
#         '__type__': 'rules',
#         'name': _('a game'),
#         'players_type': _('2 players'),
#         'colors_type': _('assigned colors'),
#         'dimensions': [3, 3],
#         'shapes': [ defaults['shape'] ],
#         'board_type': _('hash'),
#         'initial_state': [ ],
#         'phases': [ defaults['phase'] ],
#         'turn_density': _('1 piece/turn'),
#         'draw_option': _('no voluntary draw'),
#         'stalemate_result': _('stalemate draws'),
#         'move_checks': [ _('first 3-same-color-in-a-row wins') ]
# }

# class FormatAs(Categorized):
#     """Function to apply localized formatting to strings. E.g:

#         FormatAs.TURN(player="Player 1")

#     Args:
#         **kwargs: a string for each bookmark in the str

#     Returns:
#         The localized formated string.
#     """

#     def formatter(self, *args, **kwargs):
#         return self.str.format(*args, **kwargs)

# TRANSLATOR: Labels {player} as having the turn in a game
#  e.g. "Turn: Player 1"
#    TURN = collections.namedtuple("FormatValue", "STR CALL")(_("Turn: {player}"), formatter)

#     # TRANSLATOR: Labels {winners} as the winner(s) of a game
#     #  e.g. "Victory: Player 1 and Player 3"
#     VICTORY = collections.namedtuple("FormatValue", "STR CALL")(_("Victory: {winners}"), formatter)
# test commit2
