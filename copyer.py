import os
import shutil

data_dir = r"C:\Users\hmzsh\Documents\unlabeled images"
classes = ["A","B","C","D"]
#'E','F','G','H','I','K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]

for category in classes:
    path = os.path.join(data_dir,category)
    dest = r"C:\Users\hmzsh\Pictures\combined\{}".format(category)
    for img in os.listdir(path):
        imagepath = os.path.join(path,img)
        shutil.move(imagepath, dest)
print("\nDone")
