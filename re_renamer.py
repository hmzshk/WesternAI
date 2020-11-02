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

# data_dir2 = r"C:\Users\hmzsh\Pictures\new folder"
# filelist = [ f for f in os.listdir(data_dir2)]
# for f in filelist:
#     os.remove(os.path.join(data_dir2, f))

data_dir = r"C:\Users\hmzsh\Pictures\fitToImage"
classes = ['A','B','C','D','E','F','G','H','I','K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
counter = 0
corrected = []

for category in classes:
    path = os.path.join(data_dir,category)
    print(category)
    for img in os.listdir(path):
        digit = []
        imagepath = os.path.join(path,img)
        print("\nimagepath: ",imagepath)
        imageName = os.path.splitext(img)[0]
        print("imageName: ",imageName)
        fileExt  = os.path.splitext(img)[1]
        print("file extension", fileExt)
        counter=counter+2
        checkReSplit = os.path.splitext(imageName)[1]
        checkReSplit1 = os.path.splitext(imageName)[0]
        print("CheckReSplit: {} , CheckReSplit1: {}".format(checkReSplit,checkReSplit1))
        print("imageName again:",imageName)
        if fileExt == ".txt":
            oldtxtpath  = r"C:\Users\hmzsh\Pictures\checker1\{}\{}.txt".format(category,imageName)
            oldJpgPath = r"C:\Users\hmzsh\Pictures\checker1\{}\{}.jpg".format(category,imageName)
            newTxtpath = r"C:\Users\hmzsh\Pictures\fitToImage\{}\{}.txt".format(category,imageName)
            pathTosave = r"C:\Users\hmzsh\Pictures\fitToImage\{}\{}.jpg".format(category,imageName)
            shutil.copy(newTxtpath,oldtxtpath)
            shutil.copy(pathTosave,oldJpgPath)
            # if checkReSplit == ".txt_re":
            #     # shutil.move(r"C:\Users\hmzsh\Pictures\checker1\{}\{}.jpg".format(category,imageName),r"C:\Users\hmzsh\Pictures\fitToImage\{}\{}.jpg".format(category,imageName))
            #     # print("Moved")
            #     # shutil.move(r"C:\Users\hmzsh\Pictures\checker1\{}\{}.txt".format(category,imageName),r"C:\Users\hmzsh\Pictures\fitToImage\{}\{}.txt".format(category,imageName))
            #     # print("Moved both!")
            #     textPath =r"C:\Users\hmzsh\Pictures\fitToImage\{}\{}.txt".format(category,imageName)
            #
            #     jpgPath =  r"C:\Users\hmzsh\Pictures\fitToImage\{}\{}.jpg".format(category,imageName)
            #     # image = cv2.imread(jpgPath)
            #     # imageName = "{}RE".format(checkReSplit1)
            #     #
            #     # newTxtpath = r"C:\Users\hmzsh\Pictures\fitToImage\{}\{}.txt".format(category,imageName)
            #     # print("new imageName: {}".format(imageName))
            #     #
            #     # pathTosave = r"C:\Users\hmzsh\Pictures\fitToImage\{}\{}.jpg".format(category,imageName)
            #     # cv2.imwrite(pathTosave,image)
            #     # f = open(textPath,'r')
            #     # lines = f.readline()
            #     # nFile = open(newTxtpath,"a+")
            #     # nFile.truncate(0)
            #     # nFile.write(lines)
            #     # nFile.close()
            #     # f.close()
            #     os.remove(textPath)
            #     os.remove(jpgPath)
        # jpgPath = r"C:\Users\hmzsh\Pictures\newLabels\{}\{}.jpg".format(category,imageName)
        # image = cv2.imread(jpgPath)
        # if fileExt == ".txt":
        #     textPath = r"C:\Users\hmzsh\Pictures\combined\{}\{}.txt".format(category,imageName)
        #     path = pathlib.Path(textPath)
        #     if path.exists() == False:
        #         textPath = r"C:\Users\hmzsh\Pictures\newLabels\{}\{}.txt".format(category,imageName)
        #     f = open(textPath,'r')
        #     lines = f.readline()
        #     #print("img " + img + "Line: " + lines)
        #     try:
        #          clas, term2, term3, term4, term5 = lines.split()
        #     except ValueError as err:
        #         print("failed to process line:", lines)
        #         print(err)
        #         continue  # skip to the next line
        #     try:
        #         term2 = float(term2)
        #         digit.append(term2)
        #         term3 = float(term3)
        #         digit.append(term3)
        #         term4 = float(term4)
        #         digit.append(term4)
        #         term5 = float(term5)
        #         digit.append(term5)
        #
        #     except ValueError:
        #         number = float("NaN")
        #     name = category
        #
        #     #turn txt values into pixel values from normalized
        #     num_rows, num_cols = image.shape[:2]
        #     term2 = term2*(num_cols - 1.)
        #     term3 = term3*(num_rows - 1.)
        #     term4 = term4*(num_cols - 1.)
        #     term5 = term5*(num_rows - 1.)
        #
        #     A = term2 - ((term4-200)/2)-75
        #     B = term3 - ((term5)/2)
        #     C = (A+75) + (term4-125)
        #     D = B + term5
        #
        #     w = C - A
        #     h = D-B
        #     area = w*h
        #
        #     w = C-A
        #     h = D-B
        #     cx = A + (w / 2) # center coordinates
        #     cy = B + (h / 2)
        #     cx,cy,w,h= normalize(cx,cy,w,h)
        #
        #     color = (0, 0, 0) # color of bounding box
        #     cv2.rectangle(image, (int(A), int(B)), (int(C), int(D)), color, 5) # draws rectangle
        #     print(img + "A: {} B: {} C: {} D: {}".format(int(A),int(B),int(C),int(D))
        #
        #     pathTosave = r"C:\Users\hmzsh\Pictures\checker1\{}\{}.jpg".format(category,imageName)
        #     cv2.imwrite(pathTosave,image)
        #     newTxtpath = r"C:\Users\hmzsh\Pictures\checker1\{}\{}.txt".format(category,imageName)
        #     string = "{} {} {} {} {}".format(name,"{:.6f}".format(cx),"{:.6f}".format(cy),"{:.6f}".format(w),"{:.6f}".format(h))
        #     nFile = open(newTxtpath,"a+")
        #     nFile.truncate(0)
        #     nFile.write(string)
        #     nFile.close()
        #     f.close()
print(corrected)
print("Number of Corrections: ",len(corrected))
print("done")
