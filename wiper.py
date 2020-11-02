
import os
data_dir2 = r"C:\Users\hmzsh\Pictures\checker\Q"
filelist = [ f for f in os.listdir(data_dir2)]
for f in filelist:
    os.remove(os.path.join(data_dir2, f))
