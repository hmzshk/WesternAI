from PIL import Image
import os
import cv2
data_dir = r"D:\ASL Dataset Jesse"
#data_dir2 = "/content/drive/My Drive/Dragomen - Western AI/Datasets/ASL Dataset Jesse"
#data_dir3 = "/content/drive/My Drive/Dragomen - Western AI/Datasets/ASL Dataset Joseph/Photos"

classes = ['K',"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]


for category in classes:  # do dogs and cats
    path1 = os.path.join(data_dir,category)

    path = os.path.join(path1,"jesse")  # create path to dogs and cats
    print(category)
    #path1 =  os.path.join(data_dir3,category)
    #/content/drive/My Drive/ASL Datasets/kaggle/petimages1/cats1
    for img in os.listdir(path):
        imagepath = os.path.join(path,img)
        image = cv2.imread(imagepath)
        imageName = os.path.splitext(img)[0]
        print(imagepath)

        im = Image.open(imagepath)
        im_rotate = im.rotate(270, expand=True)

        pathTosave = r"D:\ASL Dataset Jesse\{}\jesse\{}.jpg".format(category,imageName)
        pathTodelete = r"D:\ASL Dataset Jesse\{}\jesse\{}.png".format(category,imageName)
        im_rotate.save(pathTosave)
        os.remove(pathTodelete)



print("\n\nDone!")
