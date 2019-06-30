import cv2

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
            cv2.imshow('Face_Detection',img)

    else:
        print('Camera not Working')

capture.release()
cv2.destroyAllWindows()