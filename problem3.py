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

path = r"C:\Users\hmzsh\Pictures\needsWork\problem3"
for img in os.listdir(path):
    digit = []
    imagepath = os.path.join(path,img)
    imageName = os.path.splitext(img)[0]
    category = imageName[0]
    #print(imageName)
    jpgPath = r"C:\Users\hmzsh\Pictures\needsWork\problem3\{}.jpg".format(imageName)
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
        h = D - B

        area = w * h
        print("Before " + img + " A: {} B: {} C: {} D: {} width: {} height: {} Area: {} num_cols {} num_rows {}".format(int(A),int(B),int(C),int(D),int(w),int(h),int(area),num_cols,num_rows))

        sixthCh = imageName[5]
        print("sixthCh: ",sixthCh)

        if sixthCh == 'R':
            A = 3
            B = B+20
            C = C+40
            D = D+15
        else:
            A = A+20
            B = B+20
            C = C+30
            D = D+10


        print("After " + img + " A: {} B: {} C: {} D: {} width: {} height: {} Area: {} num_cols {} num_rows {}".format(int(A),int(B),int(C),int(D),int(w),int(h),int(area),num_cols,num_rows))

        color = (202, 50, 200) # color of bounding box
        cv2.rectangle(image, (int(A), int(B)), (int(C), int(D)), color, 5) # draws rectangle

        w = C-A
        h = D-B
        cx = A + (w / 2) # center coordinates
        cy = B + (h / 2)
        cx,cy,w,h= normalize(cx,cy,w,h)
        print("Before - ", lines)
        print("normalized - A: {} B: {} C: {} D: {}".format("{:.6f}".format(cx),"{:.6f}".format(cy),"{:.6f}".format(w),"{:.6f}".format(h)))

        pathTosave = r"C:\Users\hmzsh\Pictures\needsWork\problem3_sol\{}.jpg".format(imageName)
        cv2.imwrite(pathTosave,image)
        newTxtpath = r"C:\Users\hmzsh\Pictures\needsWork\problem3_sol\{}.txt".format(imageName)
        string = "{} {} {} {} {}".format(name,"{:.6f}".format(cx),"{:.6f}".format(cy),"{:.6f}".format(w),"{:.6f}".format(h))
        nFile = open(newTxtpath,"a+")
        nFile.truncate(0)
        nFile.write(string)
        nFile.close()
        f.close()


print("done")
