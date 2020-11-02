
import argparse
import cv2
import os
from matplotlib import image
from matplotlib import pyplot as plt
from yolo import YOLO
from PIL import Image
import time
import shutil
#data_dir = "\\Users\\hmzsh\\Pictures\\Fingerspelling Dataset"
data_dir = r"D:\ASL Dataset Jesse"
#data_dir2 = "/content/drive/My Drive/Dragomen - Western AI/Datasets/ASL Dataset Jesse"
#data_dir3 = "/content/drive/My Drive/Dragomen - Western AI/Datasets/ASL Dataset Joseph/Photos"

classes = ["A","B",'C','D','E','F','G','H','I','K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]


for category in classes:  # do dogs and cats
    path1 = os.path.join(data_dir,category)

    path = os.path.join(path1,"jesse")  # create path to dogs and cats
    print(category)

    for img in os.listdir(path):
        imagepath = os.path.join(path,img)
        image = cv2.imread(imagepath)
        imageName = os.path.splitext(img)[0]
        fileExt  = os.path.splitext(img)[1]
        if fileExt == ".png":
            pathTosave = r"D:\ASL Dataset Jesse\{}\jesse\{}.jpg".format(category.lower(),imageName)
            shutil.copy(imagepath,pathTosave)

print("\n\nDone!")
