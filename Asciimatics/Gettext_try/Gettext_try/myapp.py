import locale
import gettext
import os

current_locale, encoding = locale.getdefaultlocale()

language = gettext.translation ('ar', 'locale/', languages=['ar'] )
language.install()

print(_("Text1"))
print(_("Text2"))
print(_("Text3"))
print(_("Text4"))
print(_("Text5"))
print(_("Text6"))
