import cv2
import numpy as np
from time import sleep
import os
import sys

#cap = cv2.VideoCapture(2)
#img_width = cap.get(3)
#img_height = cap.get(4)
img = cv2.imread('testimage.jpg')
img_width = 278
img_height = 181
print("img width: %d" %img_width)
print("img height: %d" %img_height)

#reading splits
n_splits = int(os.environ['N_SPLITS'])
print("n_splits: %i" %n_splits) 



img_split = img.copy()
fragment_height = img_height/n_splits

for i in range(n_splits):

	fragment = img_split[int(i*fragment_height):int((i+1)*fragment_height),:]

	#modify fragment to find most present color
	average_color = [0.0,0.0,0.0]
	pixel_count = 0
	
	for u in range(img_width):
		for v in range(int(fragment_height)):
			
			average_color += fragment[v,u]
			pixel_count += 1

	average_color = (average_color / pixel_count)
	average_color = average_color.astype(int)
	print("average color in segment %i: " %i, average_color)

	for u in range(img_width):
		for v in range(int(fragment_height)):
			
			fragment[v,u] = average_color
	
	img_split[int(i*fragment_height):int((i+1)*fragment_height),:] = fragment


cv2.namedWindow("original")
cv2.namedWindow("split")
cv2.imshow("original", img)
cv2.imshow("split", img_split)
cv2.waitKey(0)


sys.exit()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if (ret == false):
    	print("No image captured!")
    	continue


    #Put here your code!
    # You can now treat output as a normal numpy array
    # Do your magic here

    sleep(1)