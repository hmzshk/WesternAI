import shutil, random, os
import pathlib


data_dir = r"C:\Users\hmzsh\Pictures\combined"
classes = ['A','B','C','D','E','F','G','H','I','K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
path = r"C:\Users\hmzsh\Pictures\ASL Hamza\Train_dir"
path1 = r"C:\Users\hmzsh\Pictures\ASL Hamza\Valid_dir"
path2 = r"C:\Users\hmzsh\Pictures\combined"
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
        if jpgCount == 20:
            break
        if fileExt == ".jpg":
            checkpath = r"C:\Users\hmzsh\Pictures\ASL Hamza\Train_dir\{}".format(img)
            checkpath1 = r"C:\Users\hmzsh\Pictures\ASL Hamza\Valid_dir\{}".format(img)
            path = pathlib.Path(checkpath)
            path1 = pathlib.Path(checkpath1)
            if path.exists() == False and path1.exists() == False:
                jpgCount = jpgCount+1
                shutil.copy(r"C:\Users\hmzsh\Pictures\combined\{}\{}.jpg".format(category,imageName),r"C:\Users\hmzsh\Pictures\tester\{}.jpg".format(imageName))

    print("{} ".format(category) + "jpg count: ", jpgCount)
