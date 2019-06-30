import os
import cv2
import numpy as np


def readPath(path):
    imgPath = []
    labels_length = []
    for root,folders,files in os.walk(path):
        labels_length.append(len(files))
        for file in files :
            imgPath.append(root+'\\'+file)
    return imgPath

def convertImg(imgPath):
    imgArray = []
    for img in imgPath:
        frame = cv2.imread(img)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        imgArray.append(gray)
    imgArray = np.asarray(imgArray)
    #imgArray = np.vstack(imgArray)
    return imgArray

def saveImg(name,imgArray):
    curr = os.getcwd()
    os.chdir(curr+"\\"+"Objects")
    np.save(name,imgArray)
    os.chdir(curr)

imgPath = readPath(r'C:\Users\Akhilesh Kr. Pandey\Desktop\dataset\Training')

print(imgPath)

# l1 = [imgPath[0]]
# imgArray = convertImg(l1)
# print(np.asarray(imgArray).shape)

# 491 - apples (492)
# 941 - bananas (449)
# 1420 - oranges (479)

imgArray = convertImg(imgPath)
print(imgArray.shape)
saveImg("Objects.npy",imgArray)

import matplotlib.pyplot as plt
limg = np.load("Objects/Objects.npy")
plt.imshow(limg[491])
plt.show()