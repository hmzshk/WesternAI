import shutil, random, os
import pathlib

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

path = r"C:\Users\hmzsh\Pictures\jesseValid"

def checkNum(letter):
    jpgCount = 0
    path = r"C:\Users\hmzsh\Pictures\jesseValid"

    for img in os.listdir(path):
        imagepath = os.path.join(path,img)
        imageName = os.path.splitext(img)[0]
        fileExt  = os.path.splitext(img)[1]
        firstLetter = imageName[0]
        if fileExt == ".jpg":
            jpgCount = jpgCount+1
            dictJpgcount = get_value(firstLetter)+1
            dictJpg[firstLetter] = dictJpgcount

    return dictJpg[letter]
count = 0
# data_dir2 = r"C:\Users\hmzsh\Pictures\final"
# filelist = [ f for f in os.listdir(data_dir2)]
# for f in filelist:
#     os.remove(os.path.join(data_dir2, f))

jpgCount = 0
txtCount=0

for img in os.listdir(path):
    imagepath = os.path.join(path,img)
    imageName = os.path.splitext(img)[0]
    fileExt  = os.path.splitext(img)[1]
    fileCount = checkNum(imageName[0])
    if fileCount == 90:
        break
    if fileExt == ".txt":
        checkPath = r"C:\Users\hmzsh\Pictures\train_dir\{}.txt".format(imageName)
        path = pathlib.Path(checkPath)
        if path.exists() == False:
            jpgCount = jpgCount+1
            count=count+1
            shutil.copy(r"C:\Users\hmzsh\Pictures\jesseValid\{}.jpg".format(imageName),r"C:\Users\hmzsh\Pictures\validJesse\{}.jpg".format(imageName))
            newTxtpath = r"C:\Users\hmzsh\Pictures\validJesse\{}.txt".format(imageName)
            textPath = r"C:\Users\hmzsh\Pictures\jesseValid\{}.txt".format(imageName)
            cFile = open(textPath,"r")
            string = cFile.readline()
            nFile = open(newTxtpath,"a+")
            nFile.truncate(0)
            nFile.write(string)
            nFile.close()
            cFile.close()
    # category = imageName[0]
    # print("{} ".format(category) + "jpg count: ", jpgCount)
    # print("Total: ",count)
print("Total images: ",count)
    #print("{} ".format(category) + "txt count: ", txtCount)
