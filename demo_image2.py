
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


data_dir = "\\Users\\hmzsh\\Pictures\\Fingerspelling Dataset"
#data_dir2 = "/content/drive/My Drive/Dragomen - Western AI/Datasets/ASL Dataset Jesse"
#data_dir3 = "/content/drive/My Drive/Dragomen - Western AI/Datasets/ASL Dataset Joseph/Photos"

classes = ["D","E","F","G"]


for category in classes:  # do dogs and cats
    path = os.path.join(data_dir,category)  # create path to dogs and cats
    #path1 =  os.path.join(data_dir3,category)
    #/content/drive/My Drive/ASL Datasets/kaggle/petimages1/cats1
    for img in os.listdir(path):  # iterate over each image per dogs and cats
        img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
        plt.imshow(img_array, cmap='gray')  # graph it
        plt.show()  # display!

        break  # we just want one for now so break
    break  #...and one more!

img = cv2.imread("\\Users\\hmzsh\\Pictures\\Fingerspelling Dataset\\A\\A00727.png")

i = 0
width, height, inference_time, results = yolo.inference(img)
for detection in results:
    id, name, confidence, x, y, w, h = detection
    cx = x + (w / 2) # center coordinates
    cy = y + (h / 2)
    name = " A "
    # draw a bounding box rectangle and label on the image
    color = (0, 255, 255) # color of bounding box
    cv2.rectangle(img, (x - 25, y), (x + w + 25, y + h), color, 2) # draws rectangle
    text = "%s (%s)" % (name, round(confidence, 2)) # name of object and confidence
    cv2.putText(img, text, (x-25, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, color, 2)
    i=i+1
plt.imshow(img, cmap='gray')
plt.show()


pathTosave = "/Users/hmzsh/Documents/annotatedImages/A_Ann_{}.jpg".format(date_string)
cv2.imwrite(pathTosave,img)






"""
for category in classes:
    i = 0
    path = os.path.join(data_dir,category)  # create path to dogs and cats
    #path1 = os.path.join(data_dir3, category)

    for img in os.listdir(path):
        img = os.path.join(path, img)
        i = i+1
        if i>4:
            break
        else:
            width, height, inference_time, results = yolo.inference(img) #gets the width, height, inference time and results from the yolo class.
            for detection in results:
                id, name, confidence, x, y, w, h = detection
                cx = x + (w / 2) # center coordinates
                cy = y + (h / 2)

                # draw a bounding box rectangle and label on the image
                color = (0, 255, 255) # color of bounding box
                cv2.rectangle(img, (x - 100, y), (x + w + 100, y + h), color, 2) # draws rectangle
                text = "%s (%s)" % (name, round(confidence, 2)) # name of object and confidence
                cv2.putText(img, text, (x-100, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, color, 2)
                print("Saving!")
                pathTosave = "/Users/hmzsh/Documents/annotatedImages/"
                cv2.imwrite(path,img)
"""
