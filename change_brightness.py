import sys
import cv2
import numpy as np
import os
import glob
import fileinput
from PIL import Image

# Duyet anh
def browserFile(ext=""):
    return [f for f in glob.glob(f"*{ext}")]

# Doi do sang
def change_brightness(img, alpha, beta):
    img_new = np.asarray(alpha*img + beta, dtype=int)   # cast pixel values to int
    img_new[img_new>255] = 255
    img_new[img_new<0] = 0
    return img_new


if __name__ == "__main__":
    alpha = sys.argv[1]
    beta = sys.argv[2]

    for i in browserFile('*.jpg'):
        filename = i[:-4] + '_(' + sys.argv[1] + ', ' + sys.argv[2] + ').jpg' # Ten file moi dang file_(x, y).jpg
        if len(sys.argv) == 3:
            alpha = float(sys.argv[1])
            beta = int(sys.argv[2])
        img = cv2.imread(i)       # [height, width, channel]
        
        # change image brightness g(x,y) = alpha*f(x,y) + beta
        img_new = change_brightness(img, alpha, beta)
        
        cv2.imwrite(filename, img_new)
        print("Created ", filename)