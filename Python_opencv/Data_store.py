import cv2
import numpy as np

capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
frames = []

name = input('Enter The name of the Person To store the Data For:')

while True:
    ret,img = capture.read()
    if ret:
        if cv2.waitKey(1) == ord('q') or len(frames) >=50:
            break
        else:
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)

            for x,y,w,h in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(21,67,23),4)
                if len(frames) <= 50:
                    frame = gray[y:y+h,x:x+w]
                    frame = cv2.resize(frame,(50,50))
                    frames.append(frame)

            cv2.imshow('Face_Detection',img)
            print(len(frames))

    else:
        print('Camera not Working')


frames = np.asarray(frames)
np.save("Faces\\{}.npy".format(name),frames)
capture.release()
cv2.destroyAllWindows()

import matplotlib.pyplot as plt
plt.imshow(frames[0])
plt.show()

