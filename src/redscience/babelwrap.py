#!/usr/bin/env python3
"""Application-specific wrapper for babel.

To use this module, execute the following in the module where you
want your internationalization to happen (after setting enums):

  import babelwrap
  setlang = babelwrap.SetLang(globals())
  setlang("")

Assuming the name of the module where you executed the above was
"const", a call to setlang() as follows sets the first locale it
can match:

  const.setlang("zh_CN", "es_MX", "ar_TN", "en_US")

... however, it is more typical to restore the default like this:

  const.setlang("")

Either call to setlang() sets the locale for these babel functions
described at http://babel.pocoo.org/en/latest/api/numbers.html,
http://babel.pocoo.org/en/latest/api/units.html,
http://babel.pocoo.org/en/latest/api/dates.html, and
http://babel.pocoo.org/en/latest/api/lists.html:

  print(const.format_decimal(-12345.6789))
  print(const.format_percent(-12345.6789))
  print(const.format_unit(-12345.6789, "second"))
  print(const.format_datetime(datetime.datetime.now()))
  chipmunks = const.format_list(["Alvin", "Simon", "Theodore"])
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

# for mypy
# _ = format_list = format_decimal = format_percent = format_datetime = format_unit = None


class SetLang:
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

    _locale: str = ""
    _folder: str = ""

    def __init__(self: "SetLang", globals_dict):
        self.globals_dict = globals_dict

    def install(self: "SetLang", function):
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

        self.install(babel.lists.format_list)
        self.install(babel.numbers.format_decimal)
        self.install(babel.dates.format_datetime)
        self.install(babel.numbers.format_percent)
        self.install(babel.units.format_unit)
        return SetLang._locale
