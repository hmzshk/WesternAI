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

data_dir = r"C:\Users\hmzsh\Pictures\combined"
classes = ["B","C",'D','E','F','G','H','I','K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
count = 0
underSized = []
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
                number = float("NaN")
            name = category

            num_rows, num_cols = image.shape[:2]
            term2 = term2*(num_cols - 1.)
            term3 = term3*(num_rows - 1.)
            term4 = term4*(num_cols - 1.)
            term5 = term5*(num_rows - 1.)

            A = term2 - ((term4-200)/2)-75
            B = term3 - ((term5)/2)
            C = (A+75) + (term4-125)
            D = B + term5

            w = C - A
            h = D - B

            area = w * h
            #print(img + "width: {} height: {} Area: {}".format(int(w),int(h),int(area)))
            color = (0, 0, 255) # color of bounding box
            cv2.rectangle(image, (int(A), int(B)), (int(C), int(D)), color, 3) # draws rectangle

            underSized.append(img)
            pathTosave = r"C:\Users\hmzsh\Pictures\newLabels\{}\{}.jpg".format(category,imageName)
            cv2.imwrite(pathTosave,image)
            newTxtpath = r"C:\Users\hmzsh\Pictures\newLabels\{}\{}.txt".format(category,imageName)
            cFile = open(imagepath,"r")
            string = cFile.readline()
            nFile = open(newTxtpath,"a+")
            nFile.truncate(0)
            nFile.write(string)
            nFile.close()
            cFile.close()


print("done")
