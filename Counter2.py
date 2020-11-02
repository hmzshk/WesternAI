import pathlib
import shutil
import os

dictJpg = {
    "A" : 0,
    'B':0,
    'C':0,
    'D':0,
    'E':0,
    'F':0,
    'G':0,
    'H':0,
    'I':0,
    'K':0,
    "L":0,
    "M":0,
    "N":0,
    "O":0,
    "P":0,
    "Q":0,
    "R":0,
    "S":0,
    "T":0,
    "U":0,
    "V":0,
    "W":0,
    "X":0,
    "Y":0
}
dictTxt = {
    "A" : 0,
    'B':0,
    'C':0,
    'D':0,
    'E':0,
    'F':0,
    'G':0,
    'H':0,
    'I':0,
    'K':0,
    "L":0,
    "M":0,
    "N":0,
    "O":0,
    "P":0,
    "Q":0,
    "R":0,
    "S":0,
    "T":0,
    "U":0,
    "V":0,
    "W":0,
    "X":0,
    "Y":0
}
# function to return key for any value
def get_value(cat):
    for key, value in dictJpg.items():
         if key == cat:
             return value

    return "key doesn't exist"
def get_value1(cat):
    for key, value in dictTxt.items():
         if key == cat:
             return value

    return "key doesn't exist"
path = r"C:\Users\hmzsh\Pictures\Valid_dir"

jpgCountdict = {}
txtCountdict = {}

jpgCount = 0
txtCount=0
for img in os.listdir(path):
    imagepath = os.path.join(path,img)
    imageName = os.path.splitext(img)[0]
    fileExt  = os.path.splitext(img)[1]
    firstLetter = imageName[0]
    if fileExt == ".jpg":
        jpgCount = jpgCount+1
        dictJpgcount = get_value(firstLetter)+1
        #print("dictJpgcount: ",dictJpgcount)
        dictJpg[firstLetter] = dictJpgcount
    if fileExt == ".txt":
        txtCount = txtCount+1
        dictTxtcount = get_value1(firstLetter)+1
        #print("dictTxtcount: ",dictTxtcount)
        dictTxt[firstLetter] = dictTxtcount
print("{} ".format(firstLetter) + "jpg count: ", jpgCount)
print("{} ".format(firstLetter) + "txt count: ", txtCount)

print("jpg: ")
for x, y in dictJpg.items():
  print(x, y)
print("txt: ")
for x, y in dictTxt.items():
  print(x, y)
print("\nDone!")
