
# Downloading and extracting Emojione Toolkit archive

import os, urllib.request

tmp = "tmp"
url = "https://github.com/Ranks/emojione/archive/master.zip"
zip = os.path.join(tmp, "master.zip")

if not os.path.exists(tmp):
	os.makedirs(tmp)

if not os.path.isfile(zip):
	urllib.request.urlretrieve(url, zip)
