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

def getABCD(num2,num3,num4,num5):
    D1 = num2 - ((num4-200)/2)-75
    D2 = num3 - ((num5)/2)
    D3 = (D1+75) + (num4-125)
    D4 = D2 + num5
    return D1,D2,D3,D4

def normalize(dig1,dig2,dig3,dig4):
    dig1 = dig1/(num_cols - 1.)
    dig2 = dig2/(num_rows - 1.)
    dig3 = dig3/(num_cols - 1.)
    dig4 = dig4/(num_rows - 1.)
    return dig1,dig2,dig3,dig4


data_dir = r"C:\Users\hmzsh\Pictures\fitToImage"
classes = ["A","B",'C','D','E','F','G','H','I','K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
count = 0
corrected = []

for category in classes:
    path = os.path.join(data_dir,category)
    print(category)
    for img in os.listdir(path):
        digit = []
        imagepath = os.path.join(path,img)
        #print("\nimagepath: ",imagepath)
        imageName = os.path.splitext(img)[0]
        #print("imageName: ",imageName)
        fileExt  = os.path.splitext(img)[1]
        #print("file extension", fileExt)
        jpgPath = r"C:\Users\hmzsh\Pictures\fitToImage\{}\{}.jpg".format(category,imageName)
        image = cv2.imread(jpgPath)
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

            #turn txt values into pixel values from normalized
            num_rows, num_cols = image.shape[:2]
            term2 = term2*(num_cols - 1.)
            term3 = term3*(num_rows - 1.)
            term4 = term4*(num_cols - 1.)
            term5 = term5*(num_rows - 1.)

            #take the whole values and turn them into x1,y1,x2,y2 to draw rectangle
            

            print("Before " + img + " A: {} B: {} C: {} D: {} num_cols {} num_rows {}".format(int(A),int(B),int(C),int(D),num_cols,num_rows))

            color = (0, 0, 0) # color of bounding box
            cv2.rectangle(image, (int(A), int(B)), (int(C), int(D)), color, 5) # draws rectangle

            pathTosave = r"C:\Users\hmzsh\Pictures\checker\{}\{}.jpg".format(category,imageName)
            cv2.imwrite(pathTosave,image)
            f.close()


print(corrected)
print("Number of Corrections: ",len(corrected))
print("done")
