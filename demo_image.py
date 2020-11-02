
import argparse
import cv2
import os
from matplotlib import image
from matplotlib import pyplot as plt
from yolo import YOLO
from PIL import Image

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


for category in classes:
    i = 0
    path = os.path.join(data_dir,category)  # create path to dogs and cats
    #path1 = os.path.join(data_dir3, category)

    for img in os.listdir(path):
        img = os.path.join(path, img)
        if i >5:
            break
        else:
            print(img) #img = d0005.png
            img1 = Image.open(img)
            print(img1.size)
            i=i+1






"""
i = i+1
if i>5:
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
        pathTosave = "\\Users\\hmzsh\\Documents\\annotatedImages\\%s_%s" % (category,i)
        cv2.imwrite(path,img)
"""""""""
