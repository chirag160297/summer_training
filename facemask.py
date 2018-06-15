import cv2
from PIL import Image
import numpy as np
import time

maskPath='mask.png'

cascPath=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

faceCascade=cv2.CascadeClassifier(cascPath)
mask=Image.open(maskPath)

def mask(image):
	gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	
	faces=faceCascade.detectMultiScale(
	gray,
	scaleFactor=1.1,
	minNeighbors=5,
	minSize=(30,30)
	)
	
	background=Image.fromarray(image)
	
	for(x,y,w,h) in faces:
		resize_mask=mask.resize((w,h),Image.ANTIALIAS)
		offset=(x,y)
		
		background.paste(resize_mask,offset,mask=resize_mask)
	return np.asarray(background)
	
cap=cv2.VideoCapture(0)

while True:
	ret,frame=cap.read()
	cv2.imshow('image',mask(frame))
	
	if cv2.waitKey(1)==27:
		break
video_capture.release()
cv2.destroyAllWindows()	