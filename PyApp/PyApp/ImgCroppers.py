 
import numpy as np
import cv2
import uuid

image_lst = []
directory = r'D:/Library/Desktop/gkio/tables/'

while len(image_lst) < 35 :
    image_lst.append('{0}table ({1}).jpg'.format(directory, len(image_lst) + 1))

for image in image_lst:
    img = cv2.imread(image)
    
    height, width, dept = img.shape
    
    dh = int(height / 2)
    dw = int(width / 3)
     
    for x in range(3):
        out_img = img[dh * 0: dh - 87, dw * x:dw * (x + 1)]
        #cv2.imshow('image',out_img)
        #cv2.waitKey(0)
        tmpFileName = uuid.uuid4()
        cv2.imwrite('{0}{1}.jpg'.format(directory,tmpFileName),out_img)
