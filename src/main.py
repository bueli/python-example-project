import os
import gettext

locale_folder = 'locale'
gettext.bindtextdomain('example', locale_folder)

tr = gettext.gettext


print(tr("This section is empty."))

os.exit(0)