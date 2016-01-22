
import os, shutil, urllib.request, zipfile, json

# Create temporary and imgput folders

tmp = "tmp"
img = "emojione"

if not os.path.exists(tmp):
	os.makedirs(tmp)

if not os.path.exists(img):
	os.makedirs(img)


# Download and extract Emojione Toolkit archive

url = "https://github.com/Ranks/emojione/archive/master.zip"
zip = os.path.join(tmp, "master.zip")

if not os.path.exists(tmp):
	os.makedirs(tmp)

if not os.path.isfile(zip):
	urllib.request.urlretrieve(url, zip)

with zipfile.ZipFile(zip, "r") as z:
    z.extractall(tmp)


# Copy SVG

src = os.path.join(tmp, "emojione-master", "assets", "svg")

for svg in os.listdir(src):
    svg = os.path.join(src, svg)
    if (os.path.isfile(svg)):
        shutil.copy(svg, img)


# Read JSON

src = os.path.join(tmp, "emojione-master", "emoji.json")

n = 20 # Number of smilies shown
k = 0

d = json.loads(open(src).read())

f = open('emojione.pak', 'w')

def export(path, name, code):
	global k
	k = k+1
	code = code.replace("\\","\\\\")  # sanitize strings
	code = code.replace("'","\'")
	f.write("'"+img+"/"+path+".svg',	'20',	'20',	'"+str(1*(k<n))+"',	'"+name+"',	'"+code+"',\n")

for i in sorted(d.items(), key=lambda x: int(x[1]['emoji_order'])):
	for j in i[1]['aliases_ascii']+i[1]['aliases']+[i[1]['shortname']]:
		name = (i[1]['name'][:40] + '...') if len(i[1]['name']) > 40 else i[1]['name']
		code = (j[:40] + j[-2:]) if len(j) > 40 else j
		export(i[1]['unicode'], name, code)

f.close()
