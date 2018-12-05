import numpy as np
import cv2 as cv
import math

cap = cv.VideoCapture(0)

while(1):
	ret, frame = cap.read()
	width, height, c = frame.shape
	resultado = frame.copy()
	mask1 = [[1,2,1], [0,0,0], [-1,-2,-1]]
	mask2 = [[2,1,0], [1,0,-1], [0,-1,-2]]
	mask3 = [[1,0,-1], [2,0,-2], [1,0,-1]]
	mask4 = [[0,-1,-2], [1,0,-1], [2,1,0]]
	mask5 = [[-1,-2,-1], [0,0,0], [1,2,1]]
	mask6 = [[-2,-1,0], [-1,0,1], [0,1,2]]
	mask7 = [[-1,0,1], [-2,0,2], [-1,0,1]]
	mask8 = [[0,1,2], [-1,0,1], [-2,-1,0]]
	for i in range(width):
		for j in range(height):
			gray = sum(frame[i][j])
			frame[i][j] = gray/3
			
	for i in range(1, width-1):
		for j in range(1, height-1):
			g1 = 0
			g2 = 0
			g3 = 0
			g4 = 0
			g5 = 0
			g6 = 0
			g7 = 0
			g8 = 0
			for i2 in range(3):
				for j2 in range(3):
					g1 += frame[i+(i2-1)][j+(j2-1)][0] * mask1[i2][j2]
					g2 += frame[i+(i2-1)][j+(j2-1)][0] * mask2[i2][j2]
					g3 += frame[i+(i2-1)][j+(j2-1)][0] * mask3[i2][j2]
					g4 += frame[i+(i2-1)][j+(j2-1)][0] * mask4[i2][j2]
					g5 += frame[i+(i2-1)][j+(j2-1)][0] * mask5[i2][j2]
					g6 += frame[i+(i2-1)][j+(j2-1)][0] * mask6[i2][j2]
					g7 += frame[i+(i2-1)][j+(j2-1)][0] * mask7[i2][j2]
					g8 += frame[i+(i2-1)][j+(j2-1)][0] * mask8[i2][j2]
			g = np.sqrt(g1*g1 + g2*g2 + g3*g3 + g4*g4 + g5*g5 + g6*g6 + g7*g7 + g8*g8)
			resultado[i][j] = g 
					
	cv.imshow('frame', resultado)
	k = cv.waitKey(30) & 0xff
	if k == 27:
		break
				
cap.release()
cv.destroyAllWindows()