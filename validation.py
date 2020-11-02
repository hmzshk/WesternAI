import os
import shutil

data_dir = r"D:\ASL Dataset Jesse"
classes = ["A","B","C","D",'E','F','G','H','I','K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]

for category in classes:
    path1 = os.path.join(data_dir,category)
    path = os.path.join(path1,"jesse")
    dest = r"C:\Users\hmzsh\Pictures\Valid_dir"
    for img in os.listdir(path):
        imagepath = os.path.join(path,img)
        shutil.copy(imagepath, dest)
print("\nDone")
