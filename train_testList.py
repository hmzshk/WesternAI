import shutil, random, os
import pathlib


data_dir = r"C:\Users\hmzsh\Pictures\checker1"
classes = ['A','B','C','D','E','F','G','H','I','K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
count = 0
# data_dir2 = r"C:\Users\hmzsh\Pictures\final"
# filelist = [ f for f in os.listdir(data_dir2)]
# for f in filelist:
#     os.remove(os.path.join(data_dir2, f))
for category in classes:
    path = os.path.join(data_dir,category)
    jpgCount = 0
    txtCount=0

    for img in os.listdir(path):
        imagepath = os.path.join(path,img)
        imageName = os.path.splitext(img)[0]
        fileExt  = os.path.splitext(img)[1]
        if jpgCount == 100:
            break
        if fileExt == ".txt":
            checkPath = r"C:\Users\hmzsh\Pictures\train_dir\{}.txt".format(imageName)
            path = pathlib.Path(checkPath)
            if path.exists() == False:
                jpgCount = jpgCount+1
                count=count+1
                shutil.copy(r"C:\Users\hmzsh\Pictures\checker1\{}\{}.jpg".format(category,imageName),r"C:\Users\hmzsh\Pictures\jesseValid\{}.jpg".format(imageName))
                newTxtpath = r"C:\Users\hmzsh\Pictures\jesseValid\{}.txt".format(imageName)
                textPath = r"C:\Users\hmzsh\Pictures\checker1\{}\{}.txt".format(category,imageName)
                cFile = open(textPath,"r")
                string = cFile.readline()
                nFile = open(newTxtpath,"a+")
                nFile.truncate(0)
                nFile.write(string)
                nFile.close()
                cFile.close()

    print("{} ".format(category) + "jpg count: ", jpgCount)
    print("Total: ",count)
print("Total images: ",count)
    #print("{} ".format(category) + "txt count: ", txtCount)
