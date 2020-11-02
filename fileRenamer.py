import pathlib
import shutil
import os

data_dir = r"C:\Users\hmzsh\Documents\labels"
classes = ["B",'C','D','E','F','G','H','I','K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
count = 0
for category in classes:  # do dogs and cats
    path = os.path.join(data_dir,category)  # create path to dogs and cats
    #path1 =  os.path.join(data_dir3,category)
    #/content/drive/My Drive/ASL Datasets/kaggle/petimages1/cats1
    for img in os.listdir(path):
        imagepath = os.path.join(path,img)
        #print(imagepath)
        imageName = os.path.splitext(img)[0]
        imageName1 = os.path.splitext(imageName)[0]
        #print(imageName1)
        os.rename(imagepath, r"C:\Users\hmzsh\Documents\labels\{}\{}.txt".format(category,imageName1))


print("\n\nDone!")





#print(img)
#txtpath = r"C:\Users\hmzsh\Documents\labels\{}\{}_Ann_{}.txt".format(category,category,img)
#print(txtpath)
#path = pathlib.Path(txtpath)
#if path.exists() == False:
    #print("Doesn't exist")
    #count = count + 1
    #os.rename(r"C:\Users\hmzsh\Documents\annotatedImages\{}\{}".format(category,img), r"C:\Users\hmzsh\Documents\unlabeled images\{}\{}".format(category,img)")
#print("Number of missing Annotations: ",count)
