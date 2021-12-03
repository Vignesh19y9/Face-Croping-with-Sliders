import cv2
import numpy as np

def nothing(x):
  pass

def find_face(img):
    
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) !=0:
        for (x,y,w,h) in faces:
           
            roi_color = img[y:y+h, x:x+w]

    return x,y,w,h



img = cv2.imread('input.jpg')
r,c,ch=img.shape
x,y,w,h=find_face(img)

    
cv2.namedWindow('CROP',cv2.WINDOW_NORMAL)
cv2.resizeWindow('CROP', 600,600)
 

cv2.createTrackbar("Bottom ", "CROP",0,r-(y+h+1),nothing)
cv2.createTrackbar("Top ", "CROP",0,y,nothing)
cv2.createTrackbar("Right ", "CROP",0,c-(x+w+1),nothing)
cv2.createTrackbar("Left ", "CROP",0,x,nothing)


while(1):
    
   hb=cv2.getTrackbarPos("Bottom ", "CROP")
   ht=cv2.getTrackbarPos("Top ", "CROP")   
   wb=cv2.getTrackbarPos("Right ", "CROP")
   wt=cv2.getTrackbarPos("Left ", "CROP")

   
#   
   x1=img[y-ht:y+h+hb,x-wt:x+w+wb]
   
   cv2.imshow("thresh5",x1)
   
   k = cv2.waitKey(1) & 0xFF
   if k == ord('q'):
      cv2.imwrite("output.jpg",x1)
     break
cv2.destroyAllWindows()
