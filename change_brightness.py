import sys
import cv2
import numpy as np
import os
import glob
import fileinput
import xml.etree.ElementTree as ET
from PIL import Image
import shutil as st

# Duyet anh
def browserFile(ext=""):
    return [f for f in glob.glob(f"*{ext}")]

#find and replace string in file
def replaceAll(file, searchExp, replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp, replaceExp)
        sys.stdout.write(line)

# Doi do sang
def change_brightness(img, alpha, beta):
    img_new = np.asarray(alpha*img + beta, dtype=int)   # cast pixel values to int
    img_new[img_new>255] = 255
    img_new[img_new<0] = 0
    return img_new


if __name__ == "__main__":
    alpha = sys.argv[1]
    beta = sys.argv[2]
    folder_name = alpha + '_' + beta
    os.mkdir(folder_name)
    for i in browserFile('*.JPG'):
        filename_image = i[:-4] + '_(' + sys.argv[1] + ', ' + sys.argv[2] + ').jpg' # Ten file moi dang file_(x, y).jpg
        filename_xml = i[:-4] + '_(' + sys.argv[1] + ', ' + sys.argv[2] + ').xml' # Ten file moi dang file_(x, y).xml
        if len(sys.argv) == 3:
            alpha = float(sys.argv[1])
            beta = int(sys.argv[2])
        img = cv2.imread(i)       # [height, width, channel]
        
        # change image brightness g(x,y) = alpha*f(x,y) + beta
        img_new = change_brightness(img, alpha, beta)

        cv2.imwrite(filename_image, img_new)
        st.copy(i[:-3]+'xml', filename_xml)
        # Thay doi ten file anh trong file xml moi
        replaceAll(filename_xml, i, filename_image)
        # Di chuyen anh va xml moi vao thu muc moi
        st.move(filename_image, folder_name)
        st.move(filename_xml, folder_name)
        print("Created ", filename_image)
