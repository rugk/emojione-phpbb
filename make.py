
import os, shutil, urllib.request, zipfile, json


# Create temporary and imgput folders
# -----------------------------------

tmp = "tmp"
img = "emojione"

if not os.path.exists(tmp):
	os.makedirs(tmp)

if not os.path.exists(img):
	os.makedirs(img)


# Download and extract Emojione Toolkit archive
# ---------------------------------------------

url = "https://github.com/Ranks/emojione/archive/master.zip"
zip = os.path.join(tmp, "master.zip")

if not os.path.exists(tmp):
	os.makedirs(tmp)

if not os.path.isfile(zip):
	urllib.request.urlretrieve(url, zip)

with zipfile.ZipFile(zip, "r") as z:
    z.extractall(tmp)


# Copy SVG files
# --------------

src = os.path.join(tmp, "emojione-master", "assets", "svg")

for svg in os.listdir(src):
    svg = os.path.join(src, svg)
    if (os.path.isfile(svg)):
        shutil.copy(svg, img)


# Read JSON and export in PAK format
# ----------------------------------

src = os.path.join(tmp, "emojione-master", "emoji.json")

n = 20 # Number of smilies shown
k = 0  # Iteration

d = json.loads(open(src).read())

f = open('emojione.pak', 'w')

# Loop for each smiley
for i in sorted(d.items(), key=lambda x: int(x[1]['emoji_order'])):

	# Count smilies
	k = k+1

	# Loop for each smiley shortcut
	for j in i[1]['aliases_ascii']+i[1]['aliases']+[i[1]['shortname']]:

		# Drop if length exceeds 40 characters
		name = (i[1]['name'][:40] + '...') if len(i[1]['name']) > 40 else i[1]['name']
		code = (j[:40] + j[-2:]) if len(j) > 40 else j

		# Sanitize strings
		code = code.replace("\\","\\\\")
		code = code.replace("'","\'")

		# Write in file
		f.write("'"+img+"/"+i[1]['unicode']+".svg',	'20',	'20',	'"+str(1*(k<n))+"',	'"+name+"',	'"+code+"',\n")

f.close()
