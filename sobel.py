import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(1):
	ret, frame = cap.read()
	width, height, c = frame.shape
	resultado = frame.copy()
	maskX = [[-1,0,1], [-2,0,2], [-1,0,1]]
	maskY = [[1,2,1], [0,0,0], [-1,-2,-1]]
	for i in range(width):
		for j in range(height):
			gray = sum(frame[i][j])
			frame[i][j] = gray/3
			
	for i in range(1, width-1):
		for j in range(1, height-1):
			gx = 0
			gy = 0
			for i2 in range(3):
				for j2 in range(3):
					gx += frame[i+(i2-1)][j+(j2-1)][0] * maskX[i2][j2]
					gy += frame[i+(i2-1)][j+(j2-1)][0] * maskY[i2][j2]
			g = np.sqrt(gx*gx + gy*gy)
			resultado[i][j] = g 
					
	cv.imshow('frame', resultado)
	k = cv.waitKey(30) & 0xff
	if k == 27:
		break
				
cap.release()
cv.destroyAllWindows()