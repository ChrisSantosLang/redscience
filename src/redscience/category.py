#!/usr/bin/env python3
"""
Classes and functions for defining categories.
"""

import collections
import configparser
import enum
import os
import re
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

CONFIG_PATH = "../../setup.cfg"
VERSION_SECTION = "metadata"
VERSION_OPTION = "version"

_version: Optional[Tuple[Union[int,str], ...]] = None  

def version(name:str, min_parts:int=3) -> Tuple[Union[int,str], ...]:
    """Translates a version name into sortable tuples. E.g.:
    
    >>> version("1.0.1")
    (1, 0, 1)
      
    Args:
        name (str): The version name (e.g. "1.0.1")
        min_parts (int): The minimum parts for the tuple. Default is 3.
        
    Returns:
        A tuple with one member per dot-delimitted part of the name (padded with 
        as many zeros as necessary to achieve min_parts). The numeric parts are 
        integers so, the tuples sort correctly (unlike string names).

    Omits leading "v" if any. An extra "~" part is appended to non-prelease 
    versions to make them preceed prelease versions. E.g.:

    >>> version("v1.0.0-alpha") < version("1.0")
    True

    References:
        https://semver.org/
    """
    if name and name[0] == "v": name = name[1:]
    parts = re.split("-|\.", name)
    parts.extend(["0"]*(min_parts-len(parts)))
    if "-" not in name: parts.append("~")
    return tuple(int(part) if part.isnumeric() else part for part in parts)
  
def setvers(name: Optional[str]=None)->str:
    """Get or set the version. E.g.:
    
    >>> setvers("1.1.0")
    (1, 1, 0)
    
    Args:
        name (str): The name of the version to set. ``setvers("")`` will set to 
            the version named in ``setup.cfg``. If ``None``, the previously set 
            version will be retained. Default to ``None``.
        
    Returns:
        The version as a tuple. ``setvers()`` is the getter.
        
    Note:
        This function stores the set version in ``_version``
    """
    global _version
    if _version and name==None: return _version
    if name and len(name) > 0: 
        _version = version(name)
    elif os.path.exists(CONFIG_PATH):
        parser = configparser.ConfigParser()
        parser.read(CONFIG_PATH)
        if (parser.has_section(VERSION_SECTION) 
            and parser.has_option(VERSION_SECTION, VERSION_OPTION)):
            _version = version(parser.get(VERSION_SECTION, VERSION_OPTION))
    _version = _version or version("1.0.0")     
    return _version
  
setvers()

def inversion(obj: Any)->bool:
    """Tests whether an object is in the version. E.g.:
    
    >>> inversion(Color.BLACK)
    True
    
    Args:
        obj (object): The object in question
        
    Returns:
        True if the object is in the version that was set
        
    Note:
        This function assumes that any object which might not be in a version has 
        an attribute named "VERSIONS" which contains all versions that contain it.
    """
    return not hasattr(obj, "VERSIONS") or _version in obj.VERSIONS

class Category(enum.EnumMeta):
    """MetaClass for Categorized (not for public use)."""

    _catbases_: List["Category"] = []

    def __contains__(self, item):  # Check if item is in self
        return (
            isinstance(item, enum.Enum)
            and hasattr(self, item.name)
            and item.value == self[item.name].value
            and inversion(self[item.name])
        )

    def __and__(self, other):  # Intersection
        if not isinstance(other, collections.abc.Iterable):
            other = [other]
        return ctg(member for member in other if member in self)

    def __rand__(self, other):  # Intersection (from right)
        return self & other

    def __or__(self, other):  # Union
        if not isinstance(other, collections.abc.Iterable):
            other = [other]
        union = list(self)
        for member in other:
            if isinstance(member, Categorized) and member not in self:
                union.append(member)
        return ctg(union)

    def __ror__(self, other):  # Union (from right)
        return self | other

    def __sub__(self, other):  # Difference
        return ctg(x for x in self if x not in (self & other))

    def __xor__(self, other):  # Symmetric difference
        return (self | other) - (self & other)

    def __rxor__(self, other):  # Symmetric difference (from right)
        return self ^ other

    def __str__(self):
        return babelwrap.format_list(list(self))

    def __repr__(self):
        return f"<category {self.__name__}>"

    def __iter__(self):  # filter version in list
        return filter(inversion, enum.EnumMeta.__iter__(self))

    def __dir__(self):  # filter version in dir
        return [name for name in enum.EnumMeta.__dir__(self)
            if name[0]=="_" or inversion(self[name])]

    def __getitem__(self, index):
        if isinstance(index, (int, slice)):
            return list(self)[index]
        else:
            return enum.EnumMeta.__getitem__(self, index)

    def __bool__(self):
        return len(self) > 0

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):  # Equality
        if isinstance(other, Category):
            return self >= other and other >= self
        else:
            return enum.EnumMeta.__eq__(self, other)

    def __neq__(self, other):  # Inequality
        return not (self == other)

    def __ge__(self, other):  # Check if all of other are in self
        if not isinstance(other, collections.abc.Iterable):
            other = [other]
        return all(member in self for member in other)

    def __le__(self, other):  # Check if all of self are in other
        if not isinstance(other, collections.abc.Iterable):
            other = [other]
        return all(member in other for member in self)

    def __lt__(self, other):  # Is proper subset
        return self <= other and not self >= other

    def __gt__(self, other):  # Is proper superset
        return self >= other and not self <= other


class Categorized(enum.Enum, metaclass=Category):
    """
    Derive from this class to define a new Category. e.g.::

        class BoardOption(Categorized):
            _ignore_ = "BoardValue"
            class BoardValue(NamedTuple):
                STR: str
                AX: Callable[[matplotlib.figure.Figure, tuple], 
                    matplotlib.axes.Axes]
                VERSIONS: portion.interval.Interval = -P.empty()
            HASH = BoardValue(STR = _("a hash"), AX = hash_board)
            SQUARES = BoardValue(
                STR = _("squares"), 
                AX = squares_board,
                VERSIONS = P.closed(version("1.5.0"), P.inf),
            )
    
    Raises: 
        AttributeError: Upon attempt to add, delete or change member. 

    The above example assumes the existence of functions named ``hash_board``
    and ``squares_board``. It creates a ``Category`` named ``BoardOption`` with 
    two members, ``BoardOption.HASH`` and ``BoardOption.SQUARES``, each of which 
    has three attributes: ``STR``, ``AX`` and ``VERSIONS``. 
    
    The classic example of a Category is the values in a dropdown. Categories 
    behave differently in different locales. If a member has an attribute named 
    ``STR``, then that's how that member will print. The translation function, 
    ``babelwrap._()``, is applied when printing and when getting any 
    attributes (see the ``babelwrap`` module). For example, given the above, the 
    following would return "a hash" automatically translated into the language of 
    the set locale:
    
    >>> str(BoardOption.HASH)
    'a hash'
    
    Categories also behave differently in different versions. If a member has an 
    attribute named ``VERSIONS``, then that member will appear in the list for only 
    those versions. For example, in ``version("1.0.0")``, 
    ``ipywidgets.Dropdown(options=BoardOption)`` would yield a dropdown with 
    only the locale translation of "a hash", but would yield a dropdown with 
    options for both "a hash" and "squares" in ``version("1.5.0")`` and above.
    
    If a member has an attribute named ``CALL``, then the value of that attribute 
    will be invoked when that member is called. If the CALL is a ``tuple`` class 
    (e.g. ``NamedTuple``), then that member is a "factory member", and calling it 
    will return a new ``Categorized`` with the attributes of that ``tuple`` class 
    (initialized with the called parameters). For example::
    
        class Jump(NamedTuple):
            FROM: Tuple[int, ...]
            TO: Tuple[int, ...]
            def __str__(self: "Jump") -> str:
                return _("{origin} to {destination}").format(
                    origin=self.FROM, destination=self.TO
                )

        class Move(Categorized):
            _ignore_ = "MoveValue"
            class MoveValue(NamedTuple):
                STR: str
                CALL: Any
            PASS = _("Pass")
            JUMP = MoveValue(STR=_("Reposition"), CALL=Jump)

        jumps = (Move.JUMP(FROM=(1,2), TO=dest) for dest in ((3,1), (3,3), (2,4)))  
        Option = ctg(*jumps, name="Option", uniquify=True) | Move.PASS
    
    In this example, the ``Move`` category has two members: There is 
    one member ``Move.PASS`` that has no attributes, and one factory member 
    ``Move.JUMP`` that has ``STR`` and ``CALL`` attributes. The factory member
    is used to create the ``Options`` category which includes ``Option.PASS``,
    ``Option.JUMP``, ``Option.JUMP1`` and ``Option.JUMP2``. ``Option.PASS`` 
    has the same attributes as ``Move.PASS`` (in fact, they are equal); each of 
    the "JUMP" members of Options  has ``FROM`` and ``TO`` attributes.

    >>> print(Move, Option, sep="\\n")
    Pass and Reposition
    (1,2) to (3,1), (1,2) to (3,3), (1,2) to (2,4) and Pass
    
    Categories support set operations. You can check type:
    
    >>> isinstance(Move, Category), isinstance(Move.PASS, Categorized)
    True, True
    
    Test equality: 
    
    >>> Option.PASS == Move.PASS
    True
    
    ...but equal members can have different contexts! 
    
    >>> print(type(Move.PASS), type(Option.PASS), sep="\\n"))
    Pass and Reposition
    (1,2) to (3,1), (1,2) to (3,3), (1,2) to (2,4) and Pass
    
    Introspect:  
    
    >>> Option.PASS in Move, Option.JUMP in Move
    True, False

    Set difference:
    
    >>> str(Option - Move)
    '(1,2) to (3,1), (1,2) to (3,3) and (1,2) to (2,4)'

    Set intersection:
    
    >>> str(Option & Move)
    'Pass'

    Set union: 
    
    >>> str(Option | Move)
    '(1,2) to (3,1), (1,2) to (3,3), (1,2) to (2,4), Pass and Reposition'
    
    Set symmetric difference: 
    
    >>> str(Option ^ Move)
    '(1,2) to (3,1), (1,2) to (3,3), (1,2) to (2,4) and Reposition'
    
    Test for containment:
    
    >>> Option >= (Move - Move.JUMP)
    True
    
    Test for proper subset:
    
    >>> (Move - Move.JUMP) < Option
    True
           
    Categories inherit ``_ignore_`` (and more) from ``Enum``.
    
    References:
        https://docs.python.org/3/library/enum.html.
    """

    def __getattr__(self, name):
        if (
            name == "_value_"
            or not hasattr(self, "_value_")
            or not hasattr(self._value_, name)
        ):
            return enum.Enum.__getattribute__(self, name)
        else:
            return babelwrap._(getattr(self._value_, name))

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
            if name not in result and name[0]!="_":
                result.append(name)
        return sorted(result)

    def __str__(self):
        return self.STR if hasattr(self, "STR") else babelwrap._(str(self.value))

    def __hash__(self):
        return hash(self.name)

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

    def __or__(self, other):  # Union
        return ctg(self) | other


def _uniquify(name: str, collection: Iterable[str])-> str:
    """Make name unique by adding small int to end, E.g.:

    >>> _uniquify("JUMP1", ["JUMP1"]) 
    'JUMP2'
        
    Arg: 
        name (str): The name to be made unique 
        collection: The collection in which to be unique
    
    Return:
        A name that is not already in the collection and that ends in the 
            smallest positive integer suffix required to make it unique.
    """
    counter = 1
    while name in collection:
        name = re.fullmatch(r"(\w+\D)(\d*)", name).group(1) + str(counter)
        counter += 1
    return name


def ctg(
  *members: Iterable[Categorized], 
  name: str = "Categorized", 
  uniquify: bool = False,
  ) -> type:
    """Generate Category from members of other Categories. e.g.::

        ctg(Color.BLACK, Marker.CIRCLE)
        
    Args:
        *members: The members for the new Category.
        name (str): The name of the new Category. Defaults to "Categorized"
        uniquify (bool): If true, name collisions will be resolved by altering the 
            member names. Useful with factory members. Defaults to False

    Returns: 
        The Category.
    
    Raises: 
        TypeError: Upon attempt to combine non-equal members with the 
            same name when uniquify is False.
    """

    if len(members) == 1:
        if isinstance(members[0], Iterable):
            members = tuple(members[0])
        else:
            member = (members[0],)
    classdict = Category.__prepare__(name, (Categorized,))
    for member in members:
        if not isinstance(member, Categorized):
            raise TypeError(
                """'{member}' object cannot be interpreted as a Categorized""".format(
                    member=type(member).__name__
                )
            )
        elif uniquify:
            classdict[_uniquify(str(member.name), classdict)] = member.value  # type: ignore[index]
        elif member.name in classdict:
            raise TypeError(f"""Attemped to reuse key: '{member.name}'""")
        else:
            classdict[member.name] = member.value  # type: ignore[index]
    category = Category.__new__(Category, name, (Categorized,), classdict)  # type: ignore[call-overload]
    category.__module__ = __name__
    category.__qualname__ = Categorized.__qualname__
    bases: List[type] = []
    for member in reversed(members):
        member_bases = getattr(member, "_catbases_", [member.__class__])
        for base in member_bases:
            if base not in bases:
                bases.insert(0, base)
                names = [item.name for item in list(base)]
                for attr in list(base.__dict__):
                    if attr not in enum.Enum.__dict__ and attr not in names:
                        setattr(category, attr, getattr(base, attr))
    catbases = bases if name == "Categorized" else [category]
    setattr(category, "_catbases_", catbases)
    if len(bases) == 1:
        category.__doc__ = bases[0].__doc__
    else:
        base_list = babelwrap.format_list([base.__name__ for base in catbases])
        category.__doc__ = """A Category derived from
          {bases}""".format(
            bases=base_list
        )
    return category
