import numpy as np
import cv2


face_1 = np.load("akhilesh.npy").reshape(50,50*50)
face_2 = np.load("akhilesh.npy").reshape(50,50*50)


users = {0:"akhilesh",1:"wall"}

labels = np.zeros((100,1))
labels[50:,:] = 1.0

print(face_1.shape)
print(face_2.shape)

data = np.concatenate((face_1,face_2))


def distance(x2,x1):
    return np.sqrt(sum((x2-x1)**2))


def knn(x,train,k=5):
    n = train.shape[0]
    d= []
    for i in range(n):
        d.append(distance(x,train[i]))
    d = np.asarray(d)
    indexes = np.argsort(d)
    sortedlabel = labels[indexes][:k]
    count = np.unique(sortedlabel,return_counts=True)

    # count = (array([0,1]),array([2,3]),dtype=int)
    result = count[0][np.argmax(count[1])]
    return result


capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


while True:
    ret,img = capture.read()
    if ret:
        if cv2.waitKey(1) == ord('q'):
            break
        else:
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)

            for x,y,w,h in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(21,67,23),4)
                frame = gray[y:y+h,x:x+w]
                frame = cv2.resize(frame,(50,50))
                frame = np.asarray(frame).reshape(2500,-1)
                index = knn(frame.flatten(), data)
                name = users[int(index)]
                cv2.putText(img, name, (x, y),cv2.FONT_HERSHEY_COMPLEX, 0.8,(255, 0, 0), 4)

            cv2.imshow('Face_Recognition',img)


    else:
        print('Camera not Working')

capture.release()
cv2.destroyAllWindows()