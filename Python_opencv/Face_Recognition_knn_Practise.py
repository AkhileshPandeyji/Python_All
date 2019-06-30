import numpy as np
import cv2

# Face Recognition Code Through KNN

face_1 = np.load('akhilesh.npy').reshape(50,50*50)
face_2 = np.load('akhilesh.npy').reshape(50,50*50)

users = {0:'akhilesh_1',1:'akhilesh_2'}

data = np.concatenate((face_1,face_2))
labels = np.zeros((100,1))
labels[50:,:] = 1.0

# temp = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
# temp_1d = temp.flatten()
# print(temp.shape[0])
# print(temp_1d)
# print(np.argsort(temp_1d))
# temp_ind = np.argsort(temp_1d)[:5]
# print(temp_ind)
# temp_labels = labels[temp_ind]
# print(temp_labels)
# temp_count = np.unique(temp_labels,return_counts=True)
# print(temp_count)
# print(temp_count[0][np.argmax(temp_count[1])])


def distance(x2,x1):
    return np.sqrt(sum((x2-x1)**2))

# np.argsort(),np.unique(),np.argmax()


def KNN(x,train,k=5):
    # no of sample points in training data (calculate distance)
    n = train.shape[0]
    d = []
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
            faces = face_cascade.detectMultiScale(gray,scaleFactor=1.2)
            for x,y,w,h in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
                frame = gray[y:y+h,x:x+w]
                frame = cv2.resize(frame,(50,50))
                frame_n = np.asarray(frame).reshape(-1,1)
                result = KNN(frame_n.flatten(),data)
                name = users[int(result)]
                cv2.putText(img,name,(x+int(w/4),y-5),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,0),1)

            cv2.imshow("Face Recognition",img)
    else:
        print('Camera is not working')


capture.release()
cv2.destroyAllWindows()












