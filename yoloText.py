import argparse
import cv2
import os
from matplotlib import image
from matplotlib import pyplot as plt
from yolo import YOLO
from PIL import Image
import time

date_string = time.strftime("%Y-%m-%d-%H %M")

ap = argparse.ArgumentParser()
ap.add_argument('-n', '--network', default="normal", help='Network Type: normal / tiny / prn')
ap.add_argument('-d', '--device', default=0, help='Device to use')
ap.add_argument('-s', '--size', default=416, help='Size for yolo')
ap.add_argument('-c', '--confidence', default=0.2, help='Confidence for yolo')
args = ap.parse_args()

if args.network == "normal":
    print("loading yolo...")
    yolo = YOLO("models/cross-hands.cfg", "models/cross-hands.weights", ["hand"])
elif args.network == "prn":
    print("loading yolo-tiny-prn...")
    yolo = YOLO("models/cross-hands-tiny-prn.cfg", "models/cross-hands-tiny-prn.weights", ["hand"])
else:
    print("loading yolo-tiny...")
    yolo = YOLO("models/cross-hands-tiny.cfg", "models/cross-hands-tiny.weights", ["hand"])

yolo.size = int(args.size)
yolo.confidence = float(args.confidence)

#data_dir = "\\Users\\hmzsh\\Pictures\\Fingerspelling Dataset"
data_dir = r"C:\Users\hmzsh\Pictures\ASL Dataset Jon\ASL Dataset Jonatan\Right Hand"
#data_dir2 = "/content/drive/My Drive/Dragomen - Western AI/Datasets/ASL Dataset Jesse"
#data_dir3 = "/content/drive/My Drive/Dragomen - Western AI/Datasets/ASL Dataset Joseph/Photos"

classes = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]

i=-1
for category in classes:  # do dogs and cats
    i=i+1
    path = os.path.join(data_dir,category)  # create path to dogs and cats
    #path1 =  os.path.join(data_dir3,category)
    #/content/drive/My Drive/ASL Datasets/kaggle/petimages1/cats1
    for img in os.listdir(path):
        imagepath = os.path.join(path,img)
        image = cv2.imread(imagepath)

        width, height, inference_time, results = yolo.inference(image)
        for detection in results:
            id, name, confidence, x, y, w, h = detection
            cx = x + (w / 2) # center coordinates
            cy = y + (h / 2)
            # draw a bounding box rectangle and label on the image
            #cv2.rectangle(image, (x - 75, y), (x + w + 75, y + h), color, 2) # draws rectangle

            xbox = cx
            ybox = cy
            wbox = w + 200
            hbox = h
            num_rows, num_cols = image.shape[:2]
            xbox = xbox/(num_cols - 1.)
            ybox = ybox/(num_rows - 1.)
            wbox = wbox/(num_cols - 1.)
            hbox = hbox/(num_rows - 1.)

        """
        print("y = ", y)
        print("cx = ",x)
        print("cy = ",x)
        print("w+200 = ",w+200)
        """
        file1 = open(r"C:\Users\hmzsh\Documents\labels\{}\{}_Ann_{}.txt".format(category,category,img),"a+")
        file1.truncate(0)
        str1 = "{} {} {} {} {}".format(i,"{:.6f}".format(xbox),"{:.6f}".format(ybox),"{:.6f}".format(wbox),"{:.6f}".format(hbox) )
        file1.write(str1)
        file1.close()
