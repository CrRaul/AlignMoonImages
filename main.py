import cv2
import numpy as np
import sys
import os


inImages = []
inImagesBW = []
outImages = []
centerObj = []


def importImages():
	global images, inImagesBW

	path = sys.argv[1]

	imgNameList = []
	for imgName in os.listdir(path):
		if imgName.endswith('.jpg'):
			imgNameList.append(imgName)

	imgNameList.sort()

	for imgName in imgNameList:
			img = cv2.imread(path+'/'+imgName)
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

			inImages.append(img)
			inImagesBW.append(gray)

def findCenterObj():
    global inImagesBW, centerObj, inImages

    for image in inImagesBW:
        img = cv2.medianBlur(image,5)
        
        #ret,thresh1 = cv2.threshold(img,57,255,cv2.THRESH_BINARY)
        #edges = cv2.Canny(thresh1,100,200)
        #cv2.imshow("cropped", img)
        #cv2.waitKey(0)	
        #cv2.destroyAllWindows()

        circle = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=70,maxRadius=600)
        centerObj.append(circle[0][0])

def cropImages(h, w):
	global inImagesBW, centerObj

	i = 0
	for img in inImagesBW:
		cenObj = centerObj[i]
		cenObj = cenObj.astype(int)
		crop_img = img[cenObj[1]-h:cenObj[1]+h, cenObj[0]-w:cenObj[0]+w]
		i=i+1
		outImages.append(crop_img)


def exportCrop():
	global outImages

	i = 0
	for img in outImages:
		cv2.imwrite('output/out'+str(i)+'.png',img)
		i=i+1

importImages("input")
print("import")
findCenterObj()
print("center")
cropImages(500,500)
print("crop")
exportCrop()
