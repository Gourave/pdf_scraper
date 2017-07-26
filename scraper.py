import os, urllib,re, sys

pathName = "~/Desktop/pdfs/"

if len(sys.argv) == 1:
    url = "https://uwaterloo.ca/scholar/ahilal/classes/ece-457a-cooperative-and-adaptive-algorithms/materials/schedule"
elif len(sys.argv) == 2:
    url = sys.argv[1]
else:
    url = sys.argv[1]
    pathName = sys.argv[2]

path = os.path.expanduser(pathName)

print "Downloading PDFs from " + url + " and saving to " + pathName

if not os.path.exists(path):
    os.makedirs(path)

website = urllib.urlopen(url)

html = website.read()
links = re.findall('"((http|ftp)s?://.*?)"', html)
pdflinks = []

for link in links:
    if link[0].endswith(".pdf") and not (link[0] in pdflinks):
        pdflinks.append(link[0])
        fileName = re.sub("^(.*[\\\/])", "", link[0])
        print "Downloading " + fileName + "..."
        filePath = path + fileName
        urllib.urlretrieve(link[0], filePath)
