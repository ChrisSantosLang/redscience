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
    
        setlang("zh_Hans_HK", "zh_HK", "en_CA", "ar_TN")
    
    Args:
        *langs (str): locale names (e.g. "en_US") in order of preference. 

    Returns: 
        The ``babel.core.Locale`` associated with whichever language got set. 
        When called with no parameters, the previously set locale remains, so
        ``setlang()`` with no parameters is the getter.
    
    Tip:
        Passing actual locales is ueful for testing, but it is otherwise 
        more typical to set to the default locale by calling with parameter(s) 
        guaranteed to have no match. E.g. ``setlang("")``.
        
    The babel functions are then used as follows::

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
