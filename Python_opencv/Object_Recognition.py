import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

objects_ = []
folders = []

for root, folders_, files in os.walk('C:\\Users\\Akhilesh Kr. Pandey\\Desktop\\dataset\\Training'):
    for folder in folders_:
        folders.append(folder)

for i in range(len(folders)):
    objectArray = np.load("Objects/{}.npy".format(folders[i]))
    objectArray = objectArray.reshape(-1,100*100)
    print(objectArray.shape)
    objects_.append(objectArray)

objects = np.vstack(objects_)
print(objects.shape)
print(len(objects))

labels = np.zeros((len(objects), 1))
n = [len(objects_[i]) for i in range(len(folders))]
n.insert(0, 0)
print(n)

slice1 = 0
slice2 = 0

for i in range(len(folders)):
    slice1 += n[i]
    slice2 += n[i+1]
    labels[slice1:slice2, :] = float(i)

objectdict = {}
for i in range(len(folders)):
    objectdict[i] = "{}".format(folders[i])

print(objectdict)


def distance(x2, x1):
    return np.sqrt(sum((x2-x1)**2))


def KNN(test, train, k=20):
    dist = []
    for j in range(len(objects)):
        dist.append(distance(test, train[j]))
    indexes = np.argsort(dist)
    sortedlabels = labels[indexes][:k]
    count = np.unique(sortedlabels, return_counts=True)
    res = count[0][np.argmax(count[1])]
    return res


test_img = cv2.imread("Apple_test.jpg")
gray_test = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
gray_test = np.asarray(gray_test)


while True:
    if cv2.waitKey(1) == 27:
        break
    else:
        result = KNN(gray_test.flatten(), objects)
        name = objectdict[int(result)]
        cv2.putText(test_img,name,(10,10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
        cv2.imshow("Object Recognition",test_img)

cv2.destroyAllWindows()
