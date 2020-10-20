import cv2
import numpy as np
from time import sleep
import os

cap = cv2.VideoCapture(2)

#reading splits
n_splits = int(os.environ['N_SPLITS'])
print("n_splits: %i" %n_splits) 

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #Put here your code!
    # You can now treat output as a normal numpy array
    # Do your magic here

    sleep(1)