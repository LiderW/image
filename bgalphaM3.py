import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
frames = []
while(1):
	ret, frame = cap.read()
	size = np.asarray(frame)
	w = len(size)
	h = len(size[0])
	img = np.ones([w,h,3], dtype=np.uint8)*255
	if len(frames) > 1:
		dst = frame
		dst = cv.addWeighted(img,0.05, frames[0],0.95,0)
		frames.pop(0)
		resultado = cv.subtract(frame, dst)
		cv.imshow('frame', resultado)
		k = cv.waitKey(30) & 0xff
		if k == 27:
			break
	frames.append(frame)
cap.release()
cv.destroyAllWindows()