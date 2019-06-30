# 1.Face Recognition Code - Algorithm KNN
# 2.Face Detection Code
# 3.Make it Dynamic


import cv2

import numpy as np

import os


current_dir = os.getcwd()
facespath = current_dir + '/Faces'
os.chdir(facespath)
faces_list = os.listdir(facespath)
faces = []

print(faces_list)

for i in range(len(faces_list)):
    face = np.load(faces_list[i])
    face = face.reshape(face.shape[0],-1)
    faces.append(face)


os.chdir(current_dir)

faces = np.asarray(faces)
print(faces.shape)

# np.vstack(faces) -> transforms this array [[[1,---,2500],[1,----,2500]----,[1,-----,2500]]
# to [[1,---,2500]
#    [1,----,2500]
#     .
#     .
#    [1,----,2500]] one dimension is reduced in n dimensions to n-1 dimensions
faces = np.vstack(faces)
print(faces.shape)

username = {}

for i in range(len(faces_list)):
    name = faces_list[i].split('.')[0]
    username[i] = name

labels = np.zeros((faces.shape[0], 1))

# temp_labels = np.zeros((150, 1))

for i in range(3):
    labels[(i*faces.shape[0])//len(faces_list):, :] = float(i)

# print(temp_labels[100:150])


def distance(x2,x1):
    return np.sqrt(sum((x2-x1)**2))

# np.argsort(),np.unique(),np.argmax()


def KNN(x,train,k=5):
    # no of sample points in training data (calculate distance)
    n = train.shape[0]
    d = []
    print(train.shape)
    for i in range(n):
        d.append(distance(x,train[i]))
    indexes = np.argsort(d)

    # indexes = indexes[:k]
    # labels[indexes]

    sortedlabels = labels[indexes][:k]
    count = np.unique(sortedlabels,return_counts=True)
    result = count[0][np.argmax(count[1])]
    return result


# Face Detection Code

capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    check,img = capture.read()
    if check:
        if cv2.waitKey(1) == 27:
            break
        else:
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            face = face_cascade.detectMultiScale(gray,scaleFactor=1.2)
            for x,y,w,h in face:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
                frame = gray[y:y+h,x:x+w]
                frame = cv2.resize(frame,(50,50))
                frame_n = np.asarray(frame).reshape(-1,1)
                print(faces.shape)
                result = KNN(frame_n.flatten(),faces)
                name = username[int(result)]
                cv2.putText(img,name,(x+int(w/4),y-5),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,0),1)

            cv2.imshow("Face Recognition",img)

    else:
        print('Camera is not working')


capture.release()
cv2.destroyAllWindows()

