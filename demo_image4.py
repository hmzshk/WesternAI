
import argparse
import cv2
import os
from matplotlib import image
from matplotlib import pyplot as plt
from yolo import YOLO
from PIL import Image
import time

date_string = time.strftime("%Y-%m-%d-%H-%M-%S")

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
#data_dir = r"D:\ASL Dataset Jesse"
#data_dir2 = "/content/drive/My Drive/Dragomen - Western AI/Datasets/ASL Dataset Jesse"
#data_dir3 = "/content/drive/My Drive/Dragomen - Western AI/Datasets/ASL Dataset Joseph/Photos"
path = r"C:\Users\hmzsh\Pictures\validImages"
classes = ["U","V","W","X","Y"]
# "A","B",'C','D','E','F','G','H','I','K',"L","M","N","O","P","Q","R","S","T",
#
# for category in classes:  # do dogs and cats
#     path1 = os.path.join(data_dir,category)
#
#     path = os.path.join(path1,"jesse")  # create path to dogs and cats
#     print(category)
#
#     # data_dir2 = r"C:\Users\hmzsh\Pictures\jesseValid"
#     # filelist = [ f for f in os.listdir(data_dir2)]
#     # for f in filelist:
#     #     os.remove(os.path.join(data_dir2, f))
for img in os.listdir(path):
    imagepath = os.path.join(path,img)
    image = cv2.imread(imagepath)
    imageName = os.path.splitext(img)[0]
    print(imagepath)
    i = 0
    width, height, inference_time, results = yolo.inference(image)
    for detection in results:
        id, name, confidence, x, y, w, h = detection
        cx = x + (w / 2) # center coordinates
        cy = y + (h / 2)
        category = imageName[0]
        name = category

        xbox = cx
        ybox = cy
        wbox = w + 200
        hbox = h
        num_rows, num_cols = image.shape[:2]
        xbox = xbox/(num_cols - 1.)
        ybox = ybox/(num_rows - 1.)
        wbox = wbox/(num_cols - 1.)
        hbox = hbox/(num_rows - 1.)
        # draw a bounding box rectangle and label on the image
        color = (0, 255, 255) # color of bounding box
        cv2.rectangle(image, (x - 75, y), (x + w + 75, y + h), color, 2) # draws rectangle
        text = "%s (%s)" % (name, round(confidence, 2)) # name of object and confidence
        cv2.putText(image, text, (x-100, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, color, 2)
        i=i+1
    pathTosave = r"C:\Users\hmzsh\Pictures\jesseValid\{}_Ann_{}.jpg".format(category,imageName)
    cv2.imwrite(pathTosave,image)
    file1 = open(r"C:\Users\hmzsh\Pictures\jesseValid\{}_Ann_{}.txt".format(category,imageName),"a+")
    file1.truncate(0)
    str1 = "{} {} {} {} {}".format(i,"{:.6f}".format(xbox),"{:.6f}".format(ybox),"{:.6f}".format(wbox),"{:.6f}".format(hbox) )
    file1.write(str1)
    file1.close()


print("\n\nDone!")




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
