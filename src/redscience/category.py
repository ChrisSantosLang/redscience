#!/usr/bin/env python3
"""
Class and functions for Category (a kind of Enum)
"""

import collections
import enum
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


def _(message: str) -> str:
    """temporary for type hints (to be redefined for localization)"""
    return message


def format_list(items: List[Any]) -> str:
    """temporary for type hints (to be redefined for localization)"""
    return str(items)


class Category(enum.EnumMeta):
    """MetaClass for Categorized (not for public use)."""

    _catbases_: List["Category"] = []

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


def category(*members: Iterable[Categorized], name: str = "Categorized") -> type:
    """Generate Category from members of other Categories. e.g.:

    category(Color.BLACK, Marker.CIRCLE)
    """

    members = (members[0],) if len(members) == 1 else members
    classdict = Category.__prepare__(name, (Categorized,))
    for member in members:
        if not isinstance(member, Categorized):
            raise TypeError(
                """'{member}' object cannot be interpreted as a Categorized""".format(
                    member=type(member).__name__
                )
            )
        if member.name in classdict:
            if classdict[member.name] != member.value:
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
        base_list = format_list([base.__name__ for base in catbases])
        category.__doc__ = """A Category derived from
          {bases}""".format(
            bases=base_list
        )
    return category
