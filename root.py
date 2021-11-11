points = []
def find_point(img,x,height):
    y_up = height //2
    y_down = height // 2
    
    while img[y_up][x]%2 == 0 and img[y_down][x]%2 == 0 and y_up < height-1 and y_down>=0:
        y_up += 1
        y_down -= 1
    if img[y_up][x]%2 == 0: 
        print(x,y_up)
    elif img[y_down][x]%2 ==0:
        print(x,y_down)
    else:
        print("Can't find a root")
def find_root(img,x,width,height,i=1):
    global points
    points.append(find_point(img,x,height))
    if i > width // 50:
        return 
    else:
        i += 1
        find_root(img,x//2,width,height,i)
        find_root(img,x//2+x,width, height,i)
import cv2 as cv
import numpy as np
img = cv.imread('1.jpg')
color_border = 255//2
black = np.array([color_border,color_border,color_border])
white = np.array([255,255,255])
mask = cv.inRange(img, black, white)
cv.imshow("Display window", mask)
print(mask[100][100]%2)
height, width, channels = img.shape
find_root(mask,width//2, width, height)
k = cv.waitKey(0)

