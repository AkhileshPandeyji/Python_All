import cv2

capture = cv2.VideoCapture("vid1.mp4")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    check,img = capture.read()
    if check:
        if cv2.waitKey(1) == ord('q'):
            break
        else:
            img_r = cv2.resize(img,None,fx=0.7,fy=0.7)
            gray = cv2.cvtColor(img_r,cv2.COLOR_BGR2GRAY)
            # gauss = cv2.GaussianBlur(img_r,(21,21),4)
            faces = face_cascade.detectMultiScale(gray,scaleFactor=1.4)
            for x,y,w,h in faces:
                cv2.rectangle(img_r,(x,y),(x+w,y+h),(0,0,255),4)
            for x,y,w,h in faces:
                cv2.rectangle(img_r,(x,y),(x+w,y+h),(0,0,255),4)

            cv2.imshow("Face Detection Through Video",img_r)
            cv2.imshow("Grayscale",gray)
            # cv2.imshow("GaussianBlur",gauss)

    else:
        print("Video Codec Not Supported!!!")

capture.release()
cv2.destroyAllWindows()