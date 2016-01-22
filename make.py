
# Downloading and extracting Emojione Toolkit archive

import os, urllib.request, zipfile

tmp = "tmp"
url = "https://github.com/Ranks/emojione/archive/master.zip"
zip = os.path.join(tmp, "master.zip")

if not os.path.exists(tmp):
	os.makedirs(tmp)

if not os.path.isfile(zip):
	urllib.request.urlretrieve(url, zip)

with zipfile.ZipFile(zip, "r") as z:
    z.extractall(tmp)
