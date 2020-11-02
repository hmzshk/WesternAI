import pathlib
import shutil
import os
import cv2

#fixer for problems in needwork
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

def normalize(dig1,dig2,dig3,dig4):
    dig1 = dig1/(num_cols - 1.)
    dig2 = dig2/(num_rows - 1.)
    dig3 = dig3/(num_cols - 1.)
    dig4 = dig4/(num_rows - 1.)
    return dig1,dig2,dig3,dig4

def denormalize(dig1,dig2,dig3,dig4):
    dig1 = dig1*(num_cols - 1.)
    dig2 = dig2*(num_rows - 1.)
    dig3 = dig3*(num_cols - 1.)
    dig4 = dig4*(num_rows - 1.)
    return dig1,dig2,dig3,dig4

def getABCD(pathfortxt):
    f = open(pathfortxt,'r')
    lines = f.readline()
    #print("img " + img + "Line: " + lines)
    try:
         clas, term2, term3, term4, term5 = lines.split()
    except ValueError as err:
        print("failed to process line:", lines)
        print(err)
        pass  # skip to the next line
    try:
        term2 = float(term2)
        term3 = float(term3)
        term4 = float(term4)
        term5 = float(term5)
    except ValueError:
        number = float("NaN")
    num_rows, num_cols = image.shape[:2]
    cx = term2*(num_cols - 1.)
    cy = term3*(num_rows - 1.)
    w = term4*(num_cols - 1.)
    h = term5*(num_rows - 1.)

    #take the whole values and turn them into x1,y1,x2,y2 to draw rectangle
    A = cx - (w/2)
    B = cy - ((h)/2)
    C = A + w
    D = B + h
    return A,B,C,D

data_dir = r"C:\Users\hmzsh\Pictures\newLabels"
classes = ["K"]
#,"B",'C','D','E','F','G','H','I','K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
count = 0
corrected = []

# data_dir2 = r"D:\checker2\{}".format("K")
# filelist = [ f for f in os.listdir(data_dir2)]
# for f in filelist:
#     os.remove(os.path.join(data_dir2, f))

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
        jpgPath = r"C:\Users\hmzsh\Pictures\combined\{}\{}.jpg".format(category,imageName)
        image = cv2.imread(jpgPath)
        if fileExt == ".txt":
            newTextpath = r"C:\Users\hmzsh\Pictures\combined\{}\{}.txt".format(category,imageName)
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
            A = term2 - ((term4-200)/2)-75
            B = term3 - ((term5)/2)
            C = (A+75) + (term4-125)
            D = B + term5

            w = C - A
            h = D-B
            area = w*h

            print("Before " + img + " A: {} B: {} C: {} D: {} w: {} h: {} area: {} num_cols {} num_rows {}".format(int(A),int(B),int(C),int(D),int(w),int(h),int(area),num_cols,num_rows))
            prob1Let = imageName[7]
            print("prob1Let : ",prob1Let)
            if A<-25 and prob1Let == 'S':
                print("{} needs correction".format(img))
                A = 135
                B = 400
                C = 605
                D = 1270
            #
            # if A < 50:
            #     print("{} needs correction".format(img))
            #     sixthCh = imageName[5]
            #     print("sixthCh: ",sixthCh)
            #     if sixthCh == 'R':
            #         A = 3
            #         B = 275
            #         C = 175
            #         D = 565
            #     else:
            #         A = 120
            #         B = 230
            #         C = 420
            #         D = 620
            w = C-A
            h = D-B
            cx = A + (w / 2) # center coordinates
            cy = B + (h / 2)
            cx,cy,w,h= normalize(cx,cy,w,h)

            newTxtpath = r"C:\Users\hmzsh\Pictures\checker1\{}\{}.txt".format(category,imageName)
            color = (0, 0, 0) # color of bounding box
            cv2.rectangle(image, (int(A), int(B)), (int(C), int(D)), color, 5) # draws rectangle

            pathTosave = r"C:\Users\hmzsh\Pictures\checker1\{}\{}.jpg".format(category,imageName)
            cv2.imwrite(pathTosave,image)
            string = "{} {} {} {} {}".format(name,"{:.6f}".format(cx),"{:.6f}".format(cy),"{:.6f}".format(w),"{:.6f}".format(h))
            nFile = open(newTxtpath,"a+")
            nFile.truncate(0)
            nFile.write(string)
            nFile.close()
            f.close()

print(corrected)
print("Number of Corrections: ",len(corrected))
print("done")
