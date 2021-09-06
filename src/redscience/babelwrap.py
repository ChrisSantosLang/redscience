#!/usr/bin/env python3
"""
An application-specific wrapper for babel.

(also see http://babel.pocoo.org/en/latest/api/numbers.html,
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

class SetLang:
    """
    Sets-up functions for internationalization. e.g.::
    
      import babelwrap
      setlang = babelwrap.SetLang(globals())

    Args:
      globals_dict (dict): The namespace for the function. 

    Returns: 
      A function for getting/setting the ``babel.core.Locale``.
      
    Assuming the name of the module where you executed the above was
    ``const``, it would set-up the following:

    **const.setlangs(*langs: str) -> babel.core.Locale**
    
    Args:
      *langs (str): locale names (e.g. "en_US") in order of preference. 

    Returns: 
      The ``babel.core.Locale`` associated with whichever language got set. 
      When called with no parameters, the previously set locale remains, so
      ``setlang()`` with no parameters is the getter.
    
    For example, the following would set-up the ``_()`` function and the
    babel functions in ``const`` for the first locale it could match::

      const.setlang("zh_Hans_HK", "zh_HK", "en_CA", "ar_TN")

    That form is useful for testing. Otherwise, it is more typical to set 
    to the default locale by calling with parameter(s) guaranteed to have 
    no match::

      const.setlang("")

    Either way, the babel functions are then used as follows::

      print(const.format_decimal(-12345.6789))
      print(const.format_percent(-12345.6789))
      print(const.format_unit(-12345.6789, "second"))
      print(const.format_datetime(datetime.datetime.now()))
      print(const.format_list(["Alvin", "Simon", "Theodore"]))
      
    """

    _locale: str = ""
    _folder: str = ""

    def __init__(self: "SetLang", globals_dict):
        self.globals_dict = globals_dict

    def _install(self: "SetLang", function):
        """Used by SetLang internally to install each babel function"""
        wrapper = functools.partial(function, locale=SetLang._locale)
        wrapper.__doc__ = "\n".join(
            ["    Default locale from setlang(); otherwise:", function.__doc__],
        )
        self.globals_dict[function.__name__] = wrapper

    def __call__(self: "SetLang", *langs: str) -> babel.core.Locale:        
        if SetLang._locale and not langs:
            return SetLang._locale

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
            self.globals_dict["_"] = gettext.translation(
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
            self.globals_dict.update({"_": lambda x: x})

        try:
            new_locale = babel.core.Locale.parse(lang.replace("-", "_"))
        except (babel.core.UnknownLocaleError, ValueError) as e:
            logging.warning(f"No locale found for '{lang}'")
            new_locale = babel.core.Locale(_SOURCE_LANGUAGE)

        folderisnew = (not SetLang._folder) or (SetLang._folder != folder)
        if (langs and list(langs)[0]) or folderisnew:
            SetLang._locale, SetLang._folder = new_locale, folder
            logging.debug(
                "{locale} {path}".format(
                    path=path,
                    locale=repr(SetLang._locale),
                )
            )

        self._install(babel.lists.format_list)
        self._install(babel.numbers.format_decimal)
        self._install(babel.dates.format_datetime)
        self._install(babel.numbers.format_percent)
        self._install(babel.units.format_unit)
        return SetLang._locale
