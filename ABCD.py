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

# function to return key for any value
def get_value(cat):
    for key, value in dict.items():
         if key == cat:
             return value

    return "key doesn't exist"

data_dir = r"C:\Users\hmzsh\Pictures\newLabels"
classes = ["K"]
#,"B","C",'D','E','F','G','H','I','K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
count = 0
overSized = []
for category in classes:
    path = os.path.join(data_dir,category)
    print(category)
    # data_dir2 = r"C:\Users\hmzsh\Pictures\newLabels\{}".format(category)
    # filelist = [ f for f in os.listdir(data_dir2)]
    # for f in filelist:
    #     os.remove(os.path.join(data_dir2, f))
    for img in os.listdir(path):
        digit = []
        imagepath = os.path.join(path,img)
        imageName = os.path.splitext(img)[0]
        #print(imageName)
        jpgPath = r"C:\Users\hmzsh\Pictures\newLabels\{}\{}.jpg".format(category,imageName)
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
                number = float("NaN")
            name = category

            num_rows, num_cols = image.shape[:2]
            cx = term2*(num_cols - 1.)
            cy = term3*(num_rows - 1.)
            w = term4*(num_cols - 1.)
            h = term5*(num_rows - 1.)

            #for old images
            # A = term2 - ((term4-200)/2)-75
            # B = term3 - ((term5)/2)
            # C = (A+75) + (term4-125)
            # D = B + term5

            #recent
            # A = term2
            # B = term3
            # C = term4
            # D = term5

            A = cx - (w/2)
            B = cy - ((h)/2)
            C = A + w
            D = B + h

            area = w * h
            print(img + " A: {} B: {} C: {} D: {} width: {} height: {} Area: {}".format(int(A),int(B),int(C),int(D),int(w),int(h),int(area)))



print(overSized)
print("Number of oversized bounding boxes: ", len(overSized))
print("done")
