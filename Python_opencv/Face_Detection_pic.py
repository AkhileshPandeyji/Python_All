#viola jones algorithm
#haar features
#sliding window
#Haar features selection
#Integral image
#Boosting
#Cascade classifier


import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("bahubali.jpg")

faces = face_cascade.detectMultiScale(img,1.2)

for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

cv2.imwrite('im-res.jpg',img)