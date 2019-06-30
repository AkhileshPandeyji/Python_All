import os
import cv2
import numpy as np

# Dynamicalization code:

curr = os.getcwd()
faces_path = curr + '\\' + 'Faces'
faces_list = os.listdir(faces_path)
os.chdir(faces_path)
datas = []

for i in range(len(faces_list)):
    face = np.load(faces_list[i])
    face_r = face.reshape(face.shape[0],-1)
    datas.append(face_r)

datas = np.asarray(datas)
datas = np.vstack(datas)

users = {}

for i in range(len(faces_list)):
    users[i] = faces_list[i].split('.')[0]

labels = np.zeros((datas.shape[0],1))
n = len(datas) // len(faces_list)

for i in range(len(faces_list)):
    labels[i*n:,:] = float(i)

# Face Recognition Through KNN code :

os.chdir(curr)
def distance(x2,x1):
    return np.sqrt(sum((x2-x1)**2))


def KNN(x,train,k=5):
    dist = []
    n = train.shape[0]
    for i in range(n):
        d = distance(x,train[i])
        dist.append(d)
    dist =  np.asarray(dist)
    indexes = np.argsort(dist)
    sortedlabels = labels[indexes][:k]
    count = np.unique(sortedlabels,return_counts=True)
    result = count[0][np.argmax(count[1])]
    return result


# Face Detection code:

capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    check,img = capture.read()
    if check:
        if cv2.waitKey(1) == 27:
            break
        else:
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,scaleFactor=1.3)
            for x,y,w,h in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4,lineType=cv2.LINE_4)
                frame = gray[y:y+h,x:x+w]
                frame_r = cv2.resize(frame,(50,50))
                #frame_r = np.asarray(frame_r).reshape(-1, 1)
                result = KNN(frame_r.flatten(),datas)
                name = users[int(result)]
                cv2.putText(img,name,(x, y - 5),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

            cv2.imshow("Dynamic Face Recognition",img)
    else:
        print('Camera is not Working!!!')

capture.release()
cv2.destroyAllWindows()
