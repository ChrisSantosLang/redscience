#!/usr/bin/env python3
"""Contains redscience constants plus functions for internationalization.

Most constants in this module are encoded as a Category (a kind of
Enum defined in this module) or as a NamedTuple. Each displays in the
locale set via "setlang()", provided there are translations in an .mo
file (named _DOMAIN) in a folder of _LANG_DIR matching the desired locale.

A call to setlang() as follows sets the first locale it can match:

  setlang("zh_CN", "es_MX", "ar_TN", "en_US")

... however, it is more typical to force the default like this:

  setlang("")

Either call to setlang() sets the locale for these babel functions
described at http://babel.pocoo.org/en/latest/api/numbers.html,
http://babel.pocoo.org/en/latest/api/units.html,
http://babel.pocoo.org/en/latest/api/dates.html, and
http://babel.pocoo.org/en/latest/api/lists.html:

  print(format_decimal(-12345.6789))
  print(format_percent(-12345.6789))
  print(format_unit(-12345.6789, "second"))
  print(format_datetime(datetime.datetime.now()))
  chipmunks = format_list(["Alvin", "Simon", "Theodore"])))

Examples of using a NamedTuple (e.g. Game) or Category (e.g.
Command) to get strings that display differently depending on
the set locale:

  ttt=Game()
  print(ttt.RULES)
  print(Command.QUIT)
  ipywidgets.Dropdown(options=sorted(Command), value=Command.QUIT)
  ipywidgets.Button(
      description=Command.QUIT,
      tooltip=Command.QUIT.TOOLTIP,
      icon=Command.QUIT.ICON,
  )

Example using attributes (such as Color "HEX" and Marker "CODE")
that do not get translated:

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
import gettext
import locale
import logging
from typing import Iterable, NamedTuple, Optional, Tuple, Union

import babel.core
import babel.dates
import babel.lists
import babel.numbers
import babel.units
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

_DOMAIN = "games"
_LANG_DIR = "\\Users\\Chris.santos-lang\\locales"
_LOG_DIR = "\\Users\\chris.santos-lang\\logs"
_SOURCE_LANGUAGE = "en"

logger = logging.getLogger()
# if not logger.hasHandlers():
#     log_format = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
#     log_file = logging.FileHandler("{0}/{1}.log".format(_LOG_DIR, _DOMAIN))
#     log_file.setFormatter(log_format)
#     logger.addHandler(log_file)
#     log_console = logging.StreamHandler()
#     log_console.setFormatter(log_format)
#     logger.addHandler(log_console) # remove this to log only to file
#     logger.setLevel('DEBUG') # use INFO when no longer debugging


def setlang(*langs: str) -> babel.core.Locale:
    """Sets the language of _() and returns the associated babel.core.Locale.

    If no supported match can be found for langs, it will default to the
        locale of the machine or to SOURCE_LANGUAGE, so 'setlang("")' would
        restore to default.

    Args:
        *langs (str): locale names in order of preference. e.g. "en_US"

    Returns: The babel.core.Locale associated with the set langauge. It will
        keep any previously set locale if no parameters are passed, so
        'setlang()' is the getter.
    """

    if hasattr(setlang, "_locale") and not langs:
        return setlang._locale

    # append related languages
    languages = list(langs)
    for lang in filter(bool, langs):
        try:
            parsed = babel.core.Locale.parse(lang.replace("-", "_"))
        except (babel.core.UnknownLocaleError, ValueError) as e:
            logging.warning(f"Cannot parse language '{lang}'")
        languages.append(parsed.language)

    # append the language of the local machine
    language_code, encoding = locale.getdefaultlocale()
    languages.append(language_code[0:2])

    # choose the first language with qualifying .mo file
    folder = ""
    for lang in languages:
        path = gettext.find(_DOMAIN, _LANG_DIR, [lang])
        if path:
            folder = path.split(_LANG_DIR + "\\")[1].split("\\")[0]
            break

    global _
    try:
        _ = gettext.translation(_DOMAIN, _LANG_DIR, [folder]).gettext
    except (FileNotFoundError) as e:
        logging.error(
            "No {domain}.mo found in {dir}".format(
                domain=_DOMAIN,
                dir=_LANG_DIR,
            )
        )
        _ = lambda x: x

    try:
        new_locale = babel.core.Locale.parse(lang.replace("-", "_"))
    except (babel.core.UnknownLocaleError, ValueError) as e:
        logging.warning(f"No locale found for '{lang}'")
        new_locale = babel.core.Locale(_SOURCE_LANGUAGE)

    folderisnew = (not hasattr(setlang, "_folder")) or (setlang._folder != folder)
    if (langs and list(langs)[0]) or folderisnew:
        setlang._locale, setlang._folder = new_locale, folder
        logging.debug(
            "{locale} {path}".format(
                path=path,
                locale=repr(setlang._locale),
            )
        )

    global format_list
    format_list = functools.partial(babel.lists.format_list, locale=new_locale)
    format_list.__doc__ = "\n".join(
        [
            "    Default locale from setlang(); otherwise:",
            babel.lists.format_list.__doc__,
        ],
    )

    global format_decimal
    format_decimal = functools.partial(
        babel.numbers.format_decimal,
        locale=new_locale,
    )
    format_decimal.__doc__ = "\n".join(
        [
            "    Default locale from setlang(); otherwise:",
            babel.numbers.format_decimal.__doc__,
        ],
    )

    global format_percent
    format_percent = functools.partial(
        babel.numbers.format_percent,
        locale=new_locale,
    )
    format_percent.__doc__ = "\n".join(
        [
            "    Default locale from setlang(); otherwise:",
            babel.numbers.format_percent.__doc__,
        ],
    )

    global format_datetime
    format_datetime = functools.partial(
        babel.dates.format_datetime,
        locale=new_locale,
    )
    format_datetime.__doc__ = "\n".join(
        [
            "    Default locale from setlang(); otherwise:",
            babel.dates.format_datetime.__doc__,
        ],
    )

    global format_unit
    format_unit = functools.partial(babel.units.format_unit, locale=new_locale)
    format_unit.__doc__ = "\n".join(
        [
            "    Default locale from setlang(); otherwise:",
            babel.units.format_unit.__doc__,
        ],
    )
    return setlang._locale


# Keep this before setting Enums, so their values will be in the
# language from which they can be translated
setlang(_SOURCE_LANGUAGE)


class Category(enum.EnumMeta):
    """MetaClass for Categorized (not for public use)."""

    def __contains__(self, item):
        """Check if item is in self"""
        return (
            isinstance(item, enum.Enum)
            and hasattr(self, item.name)
            and item.value == self[item.name].value
        )

    def __and__(self, other):
        """Intersection"""
        if not isinstance(other, collections.abc.Iterable):
            other = [other]
        return category(member for member in other if member in self)

    def __rand__(self, other):
        """Intersection (from right)"""
        return self & other

    def __or__(self, other):
        """Union"""
        if not isinstance(other, collections.abc.Iterable):
            other = [other]
        union = list(self)
        for member in other:
            if isinstance(member, Categorized) and member not in self:
                union.append(member)
        return category(union)

    def __ror__(self, other):
        """Union (from right)"""
        return self | other

    def __sub__(self, other):
        """Difference"""
        return category(x for x in self if x not in (self & other))

    def __xor__(self, other):
        """Symmetric difference"""
        return (self | other) - (self & other)

    def __rxor__(self, other):
        """Symmetric difference (from right)"""
        return self ^ other

    def __str__(self):
        return format_list(list(self))

    def __repr__(self):
        return f"<category {self.__name__}>"

    def __getitem__(self, indexOrSlice):
        if isinstance(indexOrSlice, (int, slice)):
            return list(self)[indexOrSlice]
        else:
            return enum.EnumMeta.__getitem__(self, indexOrSlice)

    def __bool__(self):
        return len(self) > 0

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        """Equality"""
        if isinstance(other, Category):
            return self >= other and other >= self
        else:
            return enum.EnumMeta.__eq__(self, other)

    def __neq__(self, other):
        """Inequality"""
        return not (self == other)

    def __ge__(self, other):
        """Check if all of other are in self"""
        if not isinstance(other, collections.abc.Iterable):
            other = [other]
        return all(member in self for member in other)

    def __le__(self, other):
        """Check if all of self are in other"""
        if not isinstance(other, collections.abc.Iterable):
            other = [other]
        return all(member in other for member in self)

    def __lt__(self, other):
        """Is proper subset"""
        return self <= other and not self >= other

    def __gt__(self, other):
        """Is proper superset"""
        return self >= other and not self <= other


class Categorized(enum.Enum, metaclass=Category):
    """Derive from this class to define a new Category. e.g.:

        class BoardOption(Categorized):
            HASH = collections.namedtuple("BoardValue", "STR AX")(
                _("a hash"),
                hash_board,
            )

    This creates a BoardOption Category with only one member: BoardOption.HASH.
    BoardOption.HASH has two attributes, STR and AX. The AX is a function named
    "hash_board".

    If a member has an attribute named "STR", then that's how that member will
    print; if it has an attribute named "CALL", then that's what will call when
    that member is fed arguments; if the CALL is a tuple class
    (e.g. NamedTuple), then feeding arguments to that member will transform it
    into an instance of that tuple class. The translation function, _(), is
    applied to print and all attribute gets.

    See https://docs.python.org/3/library/enum.html for information
    about Enums in general.

    Categories support set functions. e.g. each of the following is True:

        isinstance(Color, Category)
        isinstance(Color.BLACK, Categorized)
        PlayerColor < Color
        PlayerColor.BLACK == Color.BLACK
        Color.BLACK in (PlayerColor - (Color.WHITE, PlayerColor.PINK))
        (PlayerColor ^ Color) >= (PlayerColor | Color.GRAY) - (Color & PlayerColor)

    "&"  yeilds set intersection
    "|"  yeilds set union
    "-"  yeilds set difference
    "^"  yeilds set symmetric difference
    "==" means members have the same names and values
    ">=" means contains
    ">"  means is proper superset
    "<"  means is proper subset

    Raises: AttributeError upon attempt to add, delete, or change a member
        attribute
    """

    def __getattr__(self, name):
        if (
            name == "_value_"
            or not hasattr(self, "_value_")
            or not hasattr(self._value_, name)
        ):
            return enum.Enum.__getattribute__(self, name)
        else:
            return _(getattr(self._value_, name))

    def __setattr__(self, name, new_value):
        if (
            name == "_value_"
            or not hasattr(self, "_value_")
            or not hasattr(self._value_, name)
        ):
            enum.Enum.__setattr__(self, name, new_value)
        else:
            raise AttributeError(
                "Can't change attribute (name: {name}) "
                "of {enum}".format(name=name, enum=repr(self))
            )

    def __delattr__(self, name):
        if hasattr(self, "_value_") and hasattr(self._value_, name):
            raise AttributeError(
                "Can't delete attribute (name: {name}) "
                "of {enum}".format(name=name, enum=repr(self))
            )
        else:
            enum.Enum.__delattr__(self, name)

    def __dir__(self):
        result = enum.Enum.__dir__(self)
        for name in dir(self._value_):
            if name not in result:
                result.append(name)
        return sorted(result)

    def __str__(self):
        return self.STR if hasattr(self, "STR") else _(str(self.value))

    def __hash__(self):
        return hash(repr(self))

    def __reduce_ex__(self):
        return enum.Enum.__reduce_ex__(self)

    def __call__(self, *args, **kwargs):
        if hasattr(self, "CALL"):
            if hasattr(self.CALL, "__base__") and self.CALL.__base__ == tuple:
                obj = object.__new__(self.__class__)
                obj._value_ = self.CALL(*args, **kwargs)
                obj._name_ = self.name
                return obj
            else:
                return self.CALL(self, *args, **kwargs)
        else:
            return self

    def __eq__(self, other):
        """To support call that creates new instance"""
        return (self.name == other.name) and (self.value == other.value)

    def __neq__(self, other):
        """To support call that creates new instance"""
        return not (self == other)

    def __int__(self):
        return list(type(self)).index(self)


def category(*members, name="Categorized") -> "Category":
    """Generate Category from members of other Categories. e.g.:

    category(Color.BLACK, Marker.CIRCLE)
    """

    members = tuple(members[0]) if len(members) == 1 else members
    classdict = Category.__prepare__(name, (Categorized,))
    for member in members:
        if not isinstance(member, Categorized):
            raise TypeError(
                """'{member}' object cannot be interpreted as a
                Categorized""".format(
                    member=type(member).__name__
                )
            )
        if member.name in classdict:
            if classdict[member.name] != member.value:
                raise TypeError(
                    """Attemped to reuse key: '{name}'
                    """.format(
                        name=member.name
                    )
                )
        else:
            classdict[member.name] = member.value
    category = Category.__new__(Category, name, (Categorized,), classdict)
    category.__module__ = __name__
    category.__qualname__ = Categorized.__qualname__
    bases = []
    for member in reversed(members):
        member_bases = getattr(member, "_catbases_", [member.__class__])
        for base in member_bases:
            if base not in bases:
                bases.insert(0, base)
                names = [item.name for item in list(base)]
                for attr in list(base.__dict__):
                    if attr not in enum.Enum.__dict__ and attr not in names:
                        setattr(category, attr, getattr(base, attr))
    category._catbases_ = bases if name == "Categorized" else [category]
    if len(bases) == 1:
        category.__doc__ = bases[0].__doc__
    else:
        base_list = format_list([base.__name__ for base in category._catbases_])
        category.__doc__ = """A Category derived from
            {bases}""".format(
            bases=base_list
        )
    return category


class Color(Categorized):
    """Color used in a game. E.g.

        Color.BLACK

    Attributes:
        STR: A localized str to name the color. How the Color prints.
        HEX: A str of the hex code to communicate the Color to computers.
    """

    # TRANSLATOR: Color of game piece as in "Move: Black circle to (2,1)"
    BLACK = collections.namedtuple("ColorValue", "STR HEX")(_("black"), "#000000")

    # TRANSLATOR: Color of game piece as in "Move: White circle to (2,1)"
    WHITE = collections.namedtuple("ColorValue", "STR HEX")(_("white"), "#ffffff")

    # TRANSLATOR: Color of game piece as in "Move: Pink circle to (2,1)"
    PINK = collections.namedtuple("ColorValue", "STR HEX")(_("pink"), "#ff81c0")

    # TRANSLATOR: Color of game piece as in "Move: Yellow circle to (2,1)"
    YELLOW = collections.namedtuple("ColorValue", "STR HEX")(_("yellow"), "#ffff14")

    # TRANSLATOR: Color of game piece as in "Move: Orange circle to (2,1)"
    ORANGE = collections.namedtuple("ColorValue", "STR HEX")(_("orange"), "#fdaa48")

    # TRANSLATOR: Color of game piece as in "Move: Blue circle to (2,1)"
    BLUE = collections.namedtuple("ColorValue", "STR HEX")(_("blue"), "#95d0fc")

    # TRANSLATOR: Color of game piece as in "Move: Purple circle to (2,1)"
    PURPLE = collections.namedtuple("ColorValue", "STR HEX")(_("purple"), "#bf77f6")

    # TRANSLATOR: Color of game piece as in "Move: Green circle to (2,1)"
    GREEN = collections.namedtuple("ColorValue", "STR HEX")(_("green"), "#96f97b")

    # TRANSLATOR: Color of game piece as in "Move: Gray circle to (2,1)"
    GRAY = collections.namedtuple("ColorValue", "STR HEX")(_("gray"), "#929591")


PlayerColor = category(Color[0:4], name="PlayerColor")


class Layout(enum.IntEnum):
    """Layout constants. E.g.:

    Layout.POINTS_PER_INCH

    """

    FIGURE_WIDTH = 5
    FIGURE_HEIGHT = 5
    POINTS_PER_INCH = 54
    MARKER_MARGIN = 8


class Command(Categorized):
    """Command from user to the application. E.g.:

        Command.NEW

    Attributes:
        STR: A localized str. How the Command prints.
        KEY (str): A localized shortcut key. Each Command tests == to
            its key as well as to itself, so Command.NEW=="n" in English
    """

    # TRANSLATOR: This is the command to start a new game (e.g. button text).
    # TRANSLATOR: This is the shortcut key to start a new game.
    # It should match the key listed in the prompt.
    NEW = collections.namedtuple("CommandValue", "STR KEY")(_("Play New"), _("n"))

    # TRANSLATOR: This is the command to end the application (e.g. button text).
    # TRANSLATOR: This is the shortcut key to end the application.
    # It should match the key listed in the prompt.
    QUIT = collections.namedtuple("CommandValue", "STR KEY")(_("Quit"), _("q"))

    # TRANSLATOR: This is the command to reverse last user input (e.g. button text).
    # TRANSLATOR: This is the shortcut key to back-up by one user input.
    # It should match the key listed in the prompt.
    UNDO = collections.namedtuple("CommandValue", "STR KEY")(("Back"), _("z"))

    def __eq__(self: "Command", other) -> bool:
        return (
            other.lower() == self.KEY
            if type(other) is str
            else Categorized.__eq__(self, other)
        )

    def __ne__(self: "Command", other) -> bool:
        return not self.__eq__(other)


class PlayersOption(Categorized):
    """Category of game by number/type of players. E.g.:

        PlayersOption.TWO

    Attributes:
        str: A localized str to name the Category. How the PlayerOption prints.
        num_players: The (int) number of regular players.
    """

    # TRANSLATOR: Category to describe games with two regular players
    TWO = collections.namedtuple("PlayersValue", "STR NUM")(_("2-Player"), 2)

    # TRANSLATOR: Category to describe games with three regular players
    THREE = collections.namedtuple("PlayersValue", "STR NUM")(_("3-Player"), 3)


class Marker(Categorized):
    """Category of game piece by what marker is use to display it.

    Attributes:
        STR: A localized str to name the marker. How the Marker prints.
        CODE: The str used in pyplot for the marker.
    """

    # TRANSLATOR: Description of the pyplot marker
    CIRCLE = collections.namedtuple("MarkerValue", "STR CODE")(_("circle"), "o")


class StalemateOption(Categorized):
    """The rule that determines how game ends if there is a stalemate.
    Prints localized str."""

    # TRANSLATOR: Game rule that the game ends in a draw if there is a stalemate
    DRAW = _("stalemate draws")


class ColorOption(Categorized):
    """The rule that determines how game ends if there is a stalemate.
    Prints localized str."""

    # TRANSLATOR: Game rule that each player is assigned their own unique color
    ASSIGNED = _("Assigned Colors")


class BoardOption(Categorized):
    """A type of board on which to play a game. Prints localized str. """

    def hash_board(fig: matplotlib.figure.Figure, dims: tuple) -> matplotlib.axes.Axes:
        """Tic-Tac-Toe board"""
        rows, cols = dims[0], dims[1]
        gs = fig.add_gridspec(1, 1)
        ax = fig.add_subplot(gs[0, 0])
        ax.patch.set_alpha(0.0)
        ax.spines["top"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.xaxis.set_ticks_position("none")
        ax.xaxis.set_ticklabels([""])
        ax.yaxis.set_ticks_position("none")
        ax.yaxis.set_ticklabels([""])
        ax.grid(True)
        ax.xaxis.set_ticks(np.arange(0.5, cols + 0.5, 1))
        ax.yaxis.set_ticks(np.arange(0.5, rows + 0.5, 1))
        plt.xlim(cols + 0.5, 0.5)
        plt.ylim(0.5, rows + 0.5)
        return ax

    # TRANSLATOR: The type of board used for Tic-Tac-Toe, as in "Played on a hash (3,3)"
    HASH = collections.namedtuple("BoardValue", "STR AX")(_("a hash"), hash_board)


import itertools

import numpy as np


class Directions(Categorized):
    """Categories of ways in which to move or build in square-tiled space. E.g:

        Directions.DIAGONAL(2)  # returns [(1,1), (1,-1), (-1,1), (-1,-1)]
        Directions.DIAGONAL.call.cache_info()  # to get cache_info

    Args:
        dimensions: The (int) number of dimensions in the space

    Attributes:
        str: A localized str to name the type of directions. How the Directions
            prints.
        call: The bound method that yields the tuples.

    Returns:
        A list of relative coordinates (tuples)
    """

    @functools.lru_cache(maxsize=8)
    def any_direction(self, dimensions):
        zero = tuple([0] * dimensions)
        unfiltered = itertools.product([1, 0, -1], repeat=dimensions)
        return tuple([np.array(x) for x in unfiltered if x != zero])

    @functools.lru_cache(maxsize=8)
    def orthogonal(self, dimensions):
        return tuple(np.identity(dimensions, dtype=int))

    @functools.lru_cache(maxsize=8)
    def diagonal(self, dimensions):
        orthogonals = list(map(tuple, self.orthogonal(dimensions)))
        return tuple(
            [x for x in self.any_direction(dimensions) if tuple(x) not in orthogonals]
        )

    @functools.lru_cache(maxsize=8)
    def knight(self, dimensions):
        spots = []
        for spot in itertools.product([2, 1, 0, -1, -2], repeat=dimensions):
            inring = (spot.count(2) + spot.count(-2)) == 1
            orthogonal = spot.count(0) >= (dimensions - 1)
            if inring and not orthogonal:
                spots.append(np.array(spot))
        return tuple(spots)

    # TRANSLATOR: Category of directions in which chess queen can move
    ANY = collections.namedtuple("DirectionsValue", "STR CALL")(
        _("any direction"),
        any_direction,
    )

    # TRANSLATOR: Category of directions in which chess bishop can move
    DIAGONAL = collections.namedtuple("DirectionsValue", "STR CALL")(
        _("diagonal"),
        diagonal,
    )

    # TRANSLATOR: Category of directions in which chess rook can move
    ORTHOGONAL = collections.namedtuple("DirectionsValue", "STR CALL")(
        _("orthogonal"),
        orthogonal,
    )

    # TRANSLATOR: Category of directions in which chess knight can move
    KNIGHT = collections.namedtuple("DirectionsValue", "STR CALL")(
        _("knight move"),
        knight,
    )


class Outcome(Categorized):
    """Function to apply localized formatting to strings. E.g:

        Outcome.VICTORY(players=["Player 1"])

    Args:
        **kwargs: a string for each bookmark in the str

    Returns:
        The localized formated string.
    """

    def formatter(self, players):
        return self.format.format(players=format_list(players))

    # TRANSLATOR: Labels {winners} as the winner(s) of a game
    #  e.g. "Victory: Player 1 and Player 3"
    VICTORY = collections.namedtuple("FormatValue", "STR FORMAT CALL")(
        _("Victory"),
        _("Victory: {players}"),
        formatter,
    )


class CheckOption(Categorized):
    """Game rules checked at the end of each move. Prints localized str. """

    # TRANSLATOR: Game rule to award the win to any player that aranges three
    # pieces of the same color in a row
    THREE_SAME_COLOR_IN_ROW_WINS = collections.namedtuple(
        "PatternCheck",
        "STR PATTERN DIRECTIONS OUTCOME",
    )(
        _("first 3-same-color-in-a-row wins"),
        "CCC",
        Directions.ANY,
        Outcome.VICTORY,
    )


class Game(NamedTuple):
    """A game definition. E.g.:

        Game()  # To use all defaults (i.e. Tic-Tac-Toe)

    Attributes:
        PLAYERS: If specified, determines the PlayersOption. Default is 2-Player.
        COLOR: If specified, determines the ColorOption. Default is Assigned
            Colors.
        BOARD: If specified, determines the BoardOption. Default is hash.
        DIMENSIONS: If specified, determines the dimensions of the board as a
            tuple of integers. Default is (3,3).
        PIECES: If specified, determines piece-specific rules as a tuple of
            PieceRules. Default is to have only one type of piece (circle) with
            5 black and 4 white starting in reserve.
        MOVE_CHECKS: If specified, list rules that are checked at the end of
            each move as tuple of CheckOptions. Can be None. Default is to award
            the win to any player that gets three of the same color in a row.
        STALEMATE: If specified, determines the StalemateOption. Default is that
            stalemate results in a draw.
    """

    class PieceRules(NamedTuple):
        """Rules for a type of piece in a game. E.g.:

           PieceRules(INITIAL_RESERVES=(5,4))

        Attributes:
            INITIAL_RESERVES: A tuple indicating the number in initial reserves
                of each color, e.g. (5, 4) means 5 of the first color, and 4 of
                the second.
        """

        INITIAL_RESERVES: Tuple[int, ...]

        @property
        def RESERVES_STR(self: "PieceRules") -> str:
            """A constant localized str describing initial reserves for the
            piece. E.g.:

            piece.RESERVES_STR
            """
            by_color = []
            for index in range(len(self.INITIAL_RESERVES)):
                # TRANSLATOR: Part of a list of amounts of game pieces.
                # e.g. "5 black" in "5 black and 4 white start in reserve"
                by_color.append(
                    _("{number} {color}").format(
                        number=self.INITIAL_RESERVES[index],
                        color=str(Color[index]).lower(),
                    ),
                )

            # TRANSLATOR: The rule for how many to have in reserve when a game
            # begins.. E.g. "5 black and 2 white start in reserve"
            return _("{list} start in reserve").format(list=format_list(by_color))

        @property
        def STRS(self: "PieceRules") -> Tuple[str, ...]:
            """Get tuple of strings describing the rules for the piece. E.g.:

            piece.STRS
            """
            lines = [self.RESERVES_STR]
            return tuple(lines)

        def __str__(self: "PieceRules") -> str:
            return "/n".join(self.STRS)

    PLAYERS: PlayersOption = PlayersOption.TWO
    COLOR: ColorOption = ColorOption.ASSIGNED
    BOARD: BoardOption = BoardOption.HASH
    DIMENSIONS: Tuple[int, ...] = (3, 3)
    PIECES: Tuple[PieceRules, ...] = (PieceRules(INITIAL_RESERVES=(5, 4)),)
    MOVE_CHECKS: Union[Tuple[()], Tuple[CheckOption, ...]] = (
        CheckOption.THREE_SAME_COLOR_IN_ROW_WINS,
    )
    STALEMATE: StalemateOption = StalemateOption.DRAW

    @property
    def STRS(self: "Game") -> Tuple[str, ...]:
        """A constant tuple of localized strings describing the game. E.g:

        game.STRS
        """
        lines = []
        # TRANSLATOR: Line defining a game board e.g. "Played on hash (3,3)" for
        # Tic-Tac-Toe where {board} is "hash" and {dimensions} is "(3,3)"
        lines.append(
            _("Played on {board} {dimensions}").format(
                dimensions=str(self.DIMENSIONS),
                board=str(self.BOARD),
            )
        )
        lines.append(str(self.PLAYERS))
        lines.append(str(self.COLOR))
        for index in range(len(self.PIECES)):
            # TRANSLATOR: Line defining rules for a type of game piece/card
            # e.g. "Circle: Immobile, 5 black and 4 white start in reserve"
            lines.append(
                _("{shape}: {rules}")
                .format(
                    shape=str(Marker[index]),
                    rules=format_list(list(self.PIECES[index].STRS)),
                )
                .capitalize()
            )
        for rule in self.MOVE_CHECKS:
            lines.append(str(rule).capitalize())
        lines.append(str(self.STALEMATE).capitalize())
        return tuple(lines)

    @property
    def RULES(self: "Game") -> str:
        """A constant localized str describing the move checks and stalemate
        rules. E.g:

        game.RULES
        """
        rule_list = list(self.MOVE_CHECKS)
        rule_list.append(self.STALEMATE)
        # TRANSLATOR: Labels {rules} as rules of a game
        #  e.g. "Rules: First 3-same-color-in-a-row wins and stalemate draws"
        return _("Rules: {rules}").format(
            rules=str(format_list(rule_list)).capitalize(),
        )

    def __str__(self: "Game") -> str:
        return "\n".join(self.STRS)

    def AXES(self, fig: matplotlib.figure.Figure) -> matplotlib.axes.Axes:
        """A constant matplotlib.axes.Axes for this game. E.g.:

            game.AXES(fig=plt.figure(1,(FIGURE_HEIGHT, FIGURE_WIDTH)))

        Args:
            fig: The Matplotlib.figure.Figure of the Axes
        """
        return self.BOARD.AX(fig, self.DIMENSIONS)

    @property
    def MARKER_SIZE(self) -> float:
        """MARKER_SIZE: A constant int size for markers in this game"""
        figure_max = max(Layout.FIGURE_HEIGHT, Layout.FIGURE_WIDTH)
        spot_size = figure_max / max(self.DIMENSIONS)
        return (spot_size * Layout.POINTS_PER_INCH - Layout.MARKER_MARGIN) ** 2


class DefaultName(Categorized):
    """Default names for players. Prints localized str. """

    # TRANSLATOR: Default name for a player in a game (independent of order)
    PLAYER_ONE = _("Player 1")

    # TRANSLATOR: Default name for a player in a game (independent of order)
    PLAYER_TWO = _("Player 2")

    # TRANSLATOR: Default name for a player in a game (independent of order)
    PLAYER_THREE = _("Player 3")

    # TRANSLATOR: Default name for a player in a game (independent of order)
    PLAYER_FOUR = _("Player 4")


class PlayerType(Categorized):
    """Types of players. Prints localized str. """

    # TRANSLATOR: A type of player in a game
    HUMAN = _("Human")


class Player(NamedTuple):
    """A player definition. E.g.:

        Player()  # To use all defaults (i.e. human)

    Attributes:
        TYPE: If specified, determines the PlayerType. Default is Human.
    """

    TYPE: PlayerType = PlayerType.HUMAN


class Move(Categorized):
    """A type of move in a game. Prints localized str. Examples:

        Move.PASS
        Move.PLACE(COLOR=Color.WHITE, MARKER=Marker.CIRCLE, TO=(2,3))
        Move.JUMP(FROM=(1,1), TO=(2,3))

    Attributes:
        TO (in JUMP and PLACE only): Tuple of integers specifying the
            destination coordinates.
        COLOR (in PLACE only): Color enum specifying the color to be placed.
            Default is Color.BLACK
        MARKER (in PLACE only): Marker enum specifying the shape to be placed.
            Default is Marker.CIRCLE
        FROM (in JUMP only): Tuple of integers specifying the origin coordinates.
    """

    class Placement(NamedTuple):

        TO: Tuple[int, ...]
        COLOR: Color = Color.BLACK
        MARKER: Marker = Marker.CIRCLE

        def __str__(self: "Placement") -> str:
            # TRANSLATOR: Names a placement in a game e.g. "Black circle to (1,2)"
            return (
                _("{color} {shape} to {destination}")
                .format(color=self.COLOR, shape=self.MARKER, destination=self.TO)
                .capitalize()
            )

    class Jump(NamedTuple):

        FROM: Tuple[int, ...]
        TO: Tuple[int, ...]

        def __str__(self: "Jump") -> str:
            # TRANSLATOR: Names a move in a game e.g. "(2,3) to (1,2)
            return _("{origin} to {destination}").format(
                origin=self.FROM, destination=self.TO
            )

    # TRANSLATOR: Move in a game when the player forfeits their turn
    PASS = _("Pass")

    # TRANSLATOR: Move in a game when the player adds a piece or card
    PLACE = collections.namedtuple("MoveValue", "STR CALL")(
        _("Place from reserves"),
        Placement,
    )

    # TRANSLATOR: Move in a game from one spot to another
    JUMP = collections.namedtuple("MoveValue", "STR CALL")(_("Reposition"), Jump)

    # TRANSLATOR: Move in a game when the player offers a voluntary draw
    OFFER = _("Offer to draw")

    # TRANSLATOR: Move in a game when the player accepts an offer to draw
    AGREE = _("Agree to draw")

    # TRANSLATOR: Move in a game when the player rejects an offer to draw
    REFUSE = _("Refuse to draw")


# Delay this set to default language until after all constants are declared;
# otherwise the strings will get translated upon declaration, and that will
# prevent us from changing language later (since we will have lost the original
# strings)
x = setlang("")


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
