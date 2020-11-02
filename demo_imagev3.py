import cv2 as cv
import numpy as np
import time

imageToread = "\\Users\\hmzsh\\Pictures\\Final Folder\\demoImage\\d_jpg00081.jpg"
img = cv.imread(imageToread)
cv.imshow('window',  img)
cv.waitKey(1)

# Give the configuration and weight files for the model and load the network.
config_path = "/Users/hmzsh/Documents/yolo/cross-hands.cfg"
weights_path = "/Users/hmzsh/Documents/yolo/cross-hands.weights"
net = cv.dnn.readNetFromDarknet(config_path, weights_path)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
# net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

ln = net.getLayerNames()
print(len(ln), ln)

# construct a blob from the image
blob = cv.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)
r = blob[0, 0, :, :]

cv.imshow('blob', r)
text = f'Blob shape={blob.shape}'
cv.displayOverlay('blob', text)
cv.waitKey(1)

net.setInput(blob)
t0 = time.time()
outputs = net.forward(ln)
t = time.time()

cv.displayOverlay('window', f'forward propagation time={t-t0}')
cv.imshow('window',  img)
cv.waitKey(0)
cv.destroyAllWindows()

net.setInput(blob)
t0 = time.time()
outputs = net.forward(ln)
t = time.time()

net.setInput(blob)
outputs = net.forward(ln)
