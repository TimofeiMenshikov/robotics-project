
from math import * 
start_angle = 0
def angle (x0,y0,x,y):
	x0, y0 , x , y = int(x0), int(y0), int(x), int (y)
	global start_angle
	
	angle = atan((x-x0)/(y-y0)) - start_angle
	start_angle = atan((x-x0)/(y-y0))
	return angle
with open('input.txt','r') as l:
	f = l.readlines()
	h = []
	for i in range (len(f)):
		if f[i].find('\n') == True:
			f[i] = f[i][:-1:] 
		f[i] = f[i].split()
		h.append(f[i])
	print(h)
for i in range(len(h)-1):
	print(angle(h[i][0],h[i][1],h[i+1][0],h[i+1][1]))
print(start_angle)

