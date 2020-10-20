import cv2
import numpy as np
from time import sleep
import os

cap = cv2.VideoCapture(2)
img_width = int(cap.get(3))
img_height = int(cap.get(4))
print("img width: %d" % img_width)
print("img height: %d" % img_height)

# environment variables
print("Reading environment variable 'N_SPLITS' ...")
n_splits = int(os.environ['N_SPLITS'])
print("n_splits: %i" % n_splits)

fragment_height = img_height/n_splits


def hueToString(hue_value):
    if (0 <= hue_value <= 30) or (330 < hue_value <= 360):
        return "red"
    elif 30 < hue_value <= 90:
        return "yellow"
    elif 90 < hue_value <= 150:
        return "green"
    elif 150 < hue_value <= 210:
        return "cyan"
    elif 210 < hue_value <= 270:
        return "blue"
    elif 270 < hue_value <= 330:
        return "purple"


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if(ret == False):
        print("could not capture image!")
        continue

    raw_frame = frame.copy()

    for i in range(n_splits):

        fragment = raw_frame[int(i*fragment_height):int((i+1)*fragment_height), :]

        average_per_row = np.average(fragment, axis=0)
        average = np.average(average_per_row, axis=0)
        bgr_average_color = np.uint8([[[average[0], average[1], average[2]]]]) #actuall this is a 1x1 image with channels b,g,r
        hsv_average_color = cv2.cvtColor(bgr_average_color, cv2.COLOR_BGR2HSV_FULL) #actuall this is a 1x1 image with channels h,s,v

        #print("average bgr color in segment %i: " % i, bgr_average_color[0][0])
        #print("average hsv color in segment %i: " % i, hsv_average_color[0][0])
        color_string = hueToString(hsv_average_color[0][0][0])
        print("Dominant color of segment %i: " %i, color_string, "hue value: ", hsv_average_color[0][0][0])
    
    print("\n")


    sleep(1)
