import os
import numpy as np
import cv2
import matplotlib.pyplot as plt


def getFolders(path):
    folders_ = []
    for root,folders,files in os.walk(path):
        for folder in folders:
            folders_.append(folder)
    return folders_


def readImgPath(path):
    imgPaths = []
    for root,folders,files in os.walk(path):
        for file in files:
            imgPaths.append(root+'\\'+file)

    return imgPaths


def convertImg(imgPaths):
    imgArray = []
    for imgPath in imgPaths:
        img = cv2.imread(imgPath)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        imgArray.append(gray)
    return imgArray


def saveImg(imgArray,folder):
    np.save('Objects/{}.npy'.format(folder),imgArray)


folders = getFolders('C:\\Users\\Akhilesh Kr. Pandey\\Desktop\\dataset\\Training')

for i in range(len(folders)):
    imgPaths = readImgPath('C:\\Users\\Akhilesh Kr. Pandey\\Desktop\\dataset\\Training'+'\\'+folders[i])
    imgPaths_n = np.asarray(imgPaths)
    imgArray = convertImg(imgPaths)
    imgArray_n = np.asarray(imgArray)
    saveImg(imgArray,folders[i])

for i in range(len(folders)):
    limg = np.load('Objects/{}.npy'.format(folders[i]))
    n = len(limg)
    print(n)
    plt.imshow(limg[n-1])
    plt.show()

