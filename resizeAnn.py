import pathlib
import shutil
import os
import cv2

dict = {
    "A" : 0,
    'B':1,
    'C':2,
    'D':3,
    'E':4,
    'F':5,
    'G':6,
    'H':7,
    'I':8,
    'K':9,
    "L":10,
    "M":11,
    "N":12,
    "O":13,
    "P":14,
    "Q":15,
    "R":16,
    "S":17,
    "T":17,
    "U":18,
    "V":19,
    "W":20,
    "X":21,
    "Y":22
}
mydir = r"C:\Users\hmzsh\Pictures\newLabels\A"
filelist = [ f for f in os.listdir(mydir)]
for f in filelist:
    os.remove(os.path.join(mydir, f))
# function to return key for any value
def get_value(cat):
    for key, value in dict.items():
         if key == cat:
             return value

    return "key doesn't exist"

data_dir = r"C:\Users\hmzsh\Pictures\combined"
classes = ['K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
count = 0
overSized = []
for category in classes:
    path = os.path.join(data_dir,category)
    print(category)
    for img in os.listdir(path):
        digit = []
        imagepath = os.path.join(path,img)
        imageName = os.path.splitext(img)[0]
        #print(imageName)
        jpgPath = r"C:\Users\hmzsh\Pictures\combined\{}\{}.jpg".format(category,imageName)
        image = cv2.imread(jpgPath)
        fileExt  = os.path.splitext(img)[1]
        if fileExt == ".txt":
            f = open(imagepath,'r')
            lines = f.readline()
            #print("img " + img + "Line: " + lines)
            try:
                 clas, term2, term3, term4, term5 = lines.split()
            except ValueError as err:
                print("failed to process line:", lines)
                print(err)
                continue  # skip to the next line
            try:
                term2 = float(term2)
                digit.append(term2)
                term3 = float(term3)
                digit.append(term3)
                term4 = float(term4)
                digit.append(term4)
                term5 = float(term5)
                digit.append(term5)

            except ValueError:
                # We expected a numeric string like -0.234 or 0.123, but got
                # something else. We could skip this line, or replace it
                # with an out-of-bounds value. I'm going to use an IEEE-754
                # "Not A Number" value as the out-of-bounds value.
                number = float("NaN")
            #print("The digits are", digit)

            if term4 > 1.0:
                f.close()
                os.remove(imagepath)
                os.remove(jpgPath)



print(overSized)
print("Number of oversized bounding boxes: ", len(overSized))
print("done")
