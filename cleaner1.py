import pathlib
import shutil
import os

path = r"C:\Users\hmzsh\Pictures\Valid_dir"
classes = ["A","B",'C','D','E','F','G','H','I','K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
count = 0
filesMoved = []
# for category in classes:
#     path = os.path.join(data_dir,category)
#     print(category)
for img in os.listdir(path):
    imagepath = os.path.join(path,img)
    #print("\nimagepath: ",imagepath)
    imageName = os.path.splitext(img)[0]
    #print("imageName: ",imageName)
    fileExt  = os.path.splitext(img)[1]
    #print("file extension", fileExt)
    if fileExt == ".jpg":
        #print("file extension is jpg")
        txtpath = r"C:\Users\hmzsh\Pictures\Valid_dir\{}.txt".format(imageName)
        #print("txtpath: ",txtpath)
        path = pathlib.Path(txtpath)
        if path.exists() == False:
            print("\n{}.txt Doesn't exist".format(imageName))
            filesMoved.append("{}.txt".format(imageName))
            count = count + 1
            shutil.move(r"C:\Users\hmzsh\Pictures\Valid_dir\{}".format(img), r"C:\Users\hmzsh\Pictures\needsWork\{}.jpg".format(imageName))
            print("Moved!")
    if fileExt == ".txt":
        #print("file extension is txt")
        imPath = r"C:\Users\hmzsh\Pictures\Valid_dir\{}.jpg".format(imageName)
        #print("imPath: ",imPath)
        path = pathlib.Path(imPath)
        if path.exists() == False:
            print("\n{}.jpg Doesn't exist".format(imageName))
            filesMoved.append("{}.jpg".format(imageName))
            count = count + 1
            shutil.move(r"C:\Users\hmzsh\Pictures\Valid_dir\{}".format(img), r"C:\Users\hmzsh\Pictures\needsWork\{}.txt".format(imageName))
            print("Moved!")


        #print("txtpath: ",txtpath)
        #print("img: ", img)
        #path = pathlib.Path(txtpath)
        #if path.exists() == False:
            #print("\n{}.txt Doesn't exist".format(imageName))
            #count = count + 1
            #shutil.move(r"C:\Users\hmzsh\Pictures\combined\{}\{}".format(category,img), r"C:\Users\hmzsh\Documents\unlabeled images\{}\{}".format(category,img))

print("files moved: ", filesMoved)            #print("Moved!")
print("\nNumber of missing Annotations: ",count)
print("\nDone!")





#print(img)
#txtpath = r"C:\Users\hmzsh\Documents\labels\{}\{}_Ann_{}.txt".format(category,category,img)
#print(txtpath)
#path = pathlib.Path(txtpath)
#if path.exists() == False:
    #print("Doesn't exist")
    #count = count + 1
    #os.rename(r"C:\Users\hmzsh\Documents\annotatedImages\{}\{}".format(category,img), r"C:\Users\hmzsh\Documents\unlabeled images\{}\{}".format(category,img)")
#print("Number of missing Annotations: ",count)
