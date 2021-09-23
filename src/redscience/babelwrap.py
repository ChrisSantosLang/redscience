#!/usr/bin/env python3
"""
An application-specific wrapper for babel.

References:
    http://babel.pocoo.org/en/latest/api/numbers.html,
    http://babel.pocoo.org/en/latest/api/units.html,
    http://babel.pocoo.org/en/latest/api/dates.html, and
    http://babel.pocoo.org/en/latest/api/lists.html)
"""

import functools
import gettext
import locale
import logging

import babel.core
import babel.dates
import babel.lists
import babel.numbers
import babel.units

logger = logging.getLogger()

_DOMAIN = "games"
_LANG_DIR = "\\Users\\Chris.santos-lang\\locales"
_SOURCE_LANGUAGE = "en"
_locale: str = ""
_folder: str = ""

    
def _install(function):
    """Used by babelwrap internally to install each babel function"""
    global _locale
    wrapper = functools.partial(function, locale=_locale)
    wrapper.__doc__ = "\n".join(
        ["    Default locale from setlang(); otherwise:", function.__doc__],
    )
    globals()[function.__name__] = wrapper

def setlang(*langs: str) -> babel.core.Locale:   
    """Gets/sets locale for language functions. E.g.::
    
        setlang()  # to get the currenty set locale
        setlang("zh_Hans_HK", "zh_HK")  # to set a language (e.g. for testing)
        setlang("")  # to restore the default language
    
    Args:
        *langs (str): locale names (e.g. "en_US") in order of preference. 

    Returns: 
        The ``babel.core.Locale`` associated with whichever language is set. 
        
    The babel functions can then be used as follows::

      print(format_decimal(-12345.6789))
      print(format_percent(-12345.6789))
      print(format_unit(-12345.6789, "second"))
      print(format_datetime(datetime.datetime.now()))
      print(format_list(["Alvin", "Simon", "Theodore"]))
      print(_("Hello world!"))
      
    """

    global _locale
    if _locale and not langs:
        return _locale

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
    languages.append(str(language_code)[0:2])

    # choose the first language with qualifying .mo file
    folder = ""
    for lang in languages:
        path = gettext.find(_DOMAIN, _LANG_DIR, [lang])
        if path:
            folder = path.split(_LANG_DIR + "\\")[1].split("\\")[0]
            break
    
    try:
        globals()["_"] = gettext.translation(
            _DOMAIN,
            _LANG_DIR,
            [folder],
        ).gettext
    except (FileNotFoundError) as e:
        logging.error(
            "No {domain}.mo found in {dir}".format(
                domain=_DOMAIN,
                dir=_LANG_DIR,
            )
        )
        globals()["_"] = lambda x: x

    try:
        new_locale = babel.core.Locale.parse(lang.replace("-", "_"))
    except (babel.core.UnknownLocaleError, ValueError) as e:
        logging.warning(f"No locale found for '{lang}'")
        new_locale = babel.core.Locale(_SOURCE_LANGUAGE)
        
    global _folder
    folderisnew = (not _folder) or (_folder != folder)
    if (langs and list(langs)[0]) or folderisnew:
        _locale, _folder = new_locale, folder
        logging.debug(
            "{locale} {path}".format(
                path=path,
                locale=repr(_locale),
            )
        )

    _install(babel.lists.format_list)
    _install(babel.numbers.format_decimal)
    _install(babel.dates.format_datetime)
    _install(babel.numbers.format_percent)
    _install(babel.units.format_unit)
    return _locale

setlang()

module_level_variable1 = 12345

module_level_variable2 = 98765
"""int: Module level variable documented inline.

The docstring may span multiple lines. The type may optionally be specified
on the first line, separated by a colon.
"""


def function_with_types_in_docstring(param1, param2):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """


def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    """Example function with PEP 484 type annotations.

    Args:
        param1: The first parameter.
        param2: The second parameter.

    Returns:
        The return value. True for success, False otherwise.

    """


def module_level_function(param1, param2=None, *args, **kwargs):
    """This is an example of a module level function.

    Function parameters should be documented in the ``Args`` section. The name
    of each parameter is required. The type and description of each parameter
    is optional, but should be included if not obvious.

    If ``*args`` or ``**kwargs`` are accepted,
    they should be listed as ``*args`` and ``**kwargs``.

    The format for a parameter is::

        name (type): description
            The description may span multiple lines. Following
            lines should be indented. The "(type)" is optional.

            Multiple paragraphs are supported in parameter
            descriptions.

    Args:
        param1 (int): The first parameter.
        param2 (:obj:`str`, optional): The second parameter. Defaults to None.
            Second line of description should be indented.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: True if successful, False otherwise.

        The return type is optional and may be specified at the beginning of
        the ``Returns`` section followed by a colon.

        The ``Returns`` section may span multiple lines and paragraphs.
        Following lines should be indented to match the first line.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.

    """
    if param1 == param2:
        raise ValueError('param1 may not be equal to param2')
    return True


def example_generator(n):
    """Generators have a ``Yields`` section instead of a ``Returns`` section.

    Args:
        n (int): The upper limit of the range to generate, from 0 to `n` - 1.

    Yields:
        int: The next number in the range of 0 to `n` - 1.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]

    """
    for i in range(n):
        yield i


class ExampleError(Exception):
    """Exceptions are documented in the same way as classes.

    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

    Either form is acceptable, but the two should not be mixed. Choose one
    convention to document the __init__ method and be consistent with it.

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        msg (str): Human readable string describing the exception.
        code (:obj:`int`, optional): Error code.

    Attributes:
        msg (str): Human readable string describing the exception.
        code (int): Exception error code.

    """

    def __init__(self, msg, code):
        self.msg = msg
        self.code = code


class ExampleClass:
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """

    def __init__(self, param1, param2, param3):
        """Example of docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1 (str): Description of `param1`.
            param2 (:obj:`int`, optional): Description of `param2`. Multiple
                lines are supported.
            param3 (list(str)): Description of `param3`.

        """
        self.attr1 = param1
        self.attr2 = param2
        self.attr3 = param3  #: Doc comment *inline* with attribute

        #: list(str): Doc comment *before* attribute, with type specified
        self.attr4 = ['attr4']

        self.attr5 = None
        """str: Docstring *after* attribute, with type specified."""

    @property
    def readonly_property(self):
        """str: Properties should be documented in their getter method."""
        return 'readonly_property'

    @property
    def readwrite_property(self):
        """list(str): Properties with both a getter and setter
        should only be documented in their getter method.

        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        return ['readwrite_property']

    @readwrite_property.setter
    def readwrite_property(self, value):
        value

    def example_method(self, param1, param2):
        """Class methods are similar to regular functions.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1: The first parameter.
            param2: The second parameter.

        Returns:
            True if successful, False otherwise.

        """
        return True

    def __special__(self):
        """By default special members with docstrings are not included.

        Special members are any methods or attributes that start with and
        end with a double underscore. Any special member with a docstring
        will be included in the output, if
        ``napoleon_include_special_with_doc`` is set to True.

        This behavior can be enabled by changing the following setting in
        Sphinx's conf.py::

            napoleon_include_special_with_doc = True

        """
        pass

    def __special_without_docstring__(self):
        pass

    def _private(self):
        """By default private members are not included.

        Private members are any methods or attributes that start with an
        underscore and are *not* special. By default they are not included
        in the output.

        This behavior can be changed such that private members *are* included
        by changing the following setting in Sphinx's conf.py::

            napoleon_include_private_with_doc = True

        """
        pass

    def _private_without_docstring(self):
        pass

class ExamplePEP526Class:
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. If ``napoleon_attr_annotations``
    is True, types can be specified in the class body using ``PEP 526``
    annotations.

    Attributes:
        attr1: Description of `attr1`.
        attr2: Description of `attr2`.

    """

    attr1: str
    attr2: int
