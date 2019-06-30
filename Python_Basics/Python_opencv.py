import cv2

font = cv2.FONT_HERSHEY_COMPLEX

img = cv2.imread('bahubali.jpg')

#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#img, (x,y) , (width,height) (color in bgr) , border_thickness
cv2.rectangle(img,(10,10),(150,150),(255,0,0),4)

#img ,text , (x,y), font face,scale(font size) , color in bgr,thickness
cv2.putText(img,"Bahubali",(20,20),font,1,(255,0,0),2)

while True:
    cv2.imshow('image', img)
    #1 ms of delay for windows switching
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()


capture = cv2.videocapture(0)

i = 0

while True:
    ret,img = capture.read()
    if ret:
        cv2.imshow('result',img)
        i += 1
        cv2.imwrite('img_{}'.format(i),img)
        if cv2.waitkey(1) == 27:
            break
    else:
        print('Camera not Working')

cv2.destroyAllWindows()
capture.release()


capture = cv2.videocapture('Video1.mp4')

while True:
    ret,img = capture.read()
    img = cv2.resize(img,None,fx=0.5,fy=0.5)
    if ret:
        cv2.imshow('result',img)
        if cv2.waitkey(1) == 27:
            break
    else:
        print('Camera not Working')

cv2.destroyAllWindows()
capture.release()