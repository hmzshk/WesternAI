import pathlib
import shutil
import os

data_dir = r"C:\Users\hmzsh\Pictures\combined"
classes = ["A","B",'C','D','E','F','G','H','I','K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
count = 0
filesMoved = []

data_dir2 = r"C:\Users\hmzsh\Pictures\staging"
filelist = [ f for f in os.listdir(data_dir2)]
for f in filelist:
    os.remove(os.path.join(data_dir2, f))

path = r"C:\Users\hmzsh\Pictures\needsWork"
for img in os.listdir(path):
    imagepath = os.path.join(path,img)
    #print("\nimagepath: ",imagepath)
    imageName = os.path.splitext(img)[0]
    category = imageName[0]
    #print("img: {} category: {}".format(img,category))
    print("imageName: ",imageName)
    fileExt  = os.path.splitext(img)[1]
    #print("file extension", fileExt)
    if fileExt == ".jpg":
        #print("file extension is jpg")
        txtpath = r"C:\Users\hmzsh\Pictures\needsWork\{}.txt".format(category,imageName)
        #print("txtpath: ",txtpath)
        path = pathlib.Path(txtpath)
        if path.exists() == False:
            print("\n{}.txt Doesn't exist".format(imageName))
            filesMoved.append("{}.txt".format(imageName))
            count = count + 1
            shutil.copy(r"C:\Users\hmzsh\Pictures\combined\{}\{}.txt".format(category,imageName), r"C:\Users\hmzsh\Pictures\staging")
            print("Moved!")
    if fileExt == ".txt":
        #print("file extension is txt")
        imPath = r"C:\Users\hmzsh\Pictures\needsWork\{}.jpg".format(category,imageName)
        #print("imPath: ",imPath)
        path = pathlib.Path(imPath)
        if path.exists() == False:
            print("\n{}.jpg Doesn't exist".format(imageName))
            filesMoved.append("{}.jpg".format(imageName))
            count = count + 1
            shutil.copy(r"C:\Users\hmzsh\Pictures\combined\{}\{}.jpg".format(category,imageName), r"C:\Users\hmzsh\Pictures\staging")
            print("Moved!")


print("files moved: ", filesMoved)            #print("Moved!")
print("\nNumber of missing Annotations: ",count)
print("\nDone!")
