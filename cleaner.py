import pathlib
import shutil
import os

data_dir = r"C:\Users\hmzsh\Pictures\combined"
classes = ["A"]
#,"B",'C','D','E','F','G','H','I','K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
count = 0
for category in classes:
    path = os.path.join(data_dir,category)
    for img in os.listdir(path):
        imagepath = os.path.join(path,img)
        print("\nimagepath: ",imagepath)
        imageName = os.path.splitext(img)[0]
        print("imageName: ",imageName)
        txtpath = r"C:\Users\hmzsh\Pictures\combined\{}\{}.txt".format(category,imageName)
        print("txtpath: ",txtpath)
        print("img: ", img)
        path = pathlib.Path(txtpath)
        if path.exists() == False:
            print("\n{}.txt Doesn't exist".format(imageName))
            count = count + 1
            #shutil.move(r"C:\Users\hmzsh\Pictures\combined\{}\{}".format(category,img), r"C:\Users\hmzsh\Documents\unlabeled images\{}\{}".format(category,img))
            print("Moved!")

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
