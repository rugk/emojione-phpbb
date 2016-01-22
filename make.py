
import os, shutil, urllib.request, zipfile

# Create temporary and output folders

tmp = "tmp"
out = "output"

if not os.path.exists(tmp):
	os.makedirs(tmp)

if not os.path.exists(out):
	os.makedirs(out)

# Download and extract Emojione Toolkit archive

url = "https://github.com/Ranks/emojione/archive/master.zip"
zip = os.path.join(tmp, "master.zip")

if not os.path.exists(tmp):
	os.makedirs(tmp)

if not os.path.isfile(zip):
	urllib.request.urlretrieve(url, zip)

with zipfile.ZipFile(zip, "r") as z:
    z.extractall(tmp)

# Copy images

src = os.path.join(tmp, "emojione-master", "assets", "svg")

for svg in os.listdir(src):
    svg = os.path.join(src, svg)
    if (os.path.isfile(svg)):
        shutil.copy(svg, out)
