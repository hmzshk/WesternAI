import pathlib
import shutil
import os

data_dir = r"C:\Users\hmzsh\Pictures\checker1"
classes = ["A","B",'C','D','E','F','G','H','I','K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]


jpgCountdict = {}
txtCountdict = {}
for category in classes:
    path = os.path.join(data_dir,category)
    jpgCount = 0
    txtCount=0
    for img in os.listdir(path):
        imagepath = os.path.join(path,img)
        imageName = os.path.splitext(img)[0]
        fileExt  = os.path.splitext(img)[1]
        if fileExt == ".jpg":
            jpgCount = jpgCount+1
        if fileExt == ".txt":
            txtCount = txtCount+1
    print("{} ".format(category) + "jpg count: ", jpgCount)
    print("{} ".format(category) + "txt count: ", txtCount)
    jpgCountdict[category] = jpgCount
    txtCountdict[category] = txtCount

print("\nDone!")
