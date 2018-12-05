import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
frames = []

while(1):
	ret, frame = cap.read()
	
	if len(frames) > 1:
		if len(frames) > 10:
			frames.pop(0)

		media = 0
		for i in frames:
			media += i.astype('float')
		
		media = media/10
		resultado = cv.subtract(frame, media.astype('uint8'))

		cv.imshow('frame', resultado)
		k = cv.waitKey(30) & 0xff
		if k == 27:
			break
	frames.append(frame)
cap.release()
cv.destroyAllWindows()