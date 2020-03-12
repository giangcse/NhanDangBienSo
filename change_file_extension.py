import os
import glob
import fileinput
import sys
from PIL import Image

def browserFile(ext=""):
    return [f for f in glob.glob(f"*{ext}")]

if __name__ == "__main__":
       for i in browserFile('*.png'):
              filename = i[:-4]
              img = Image.open(filename+'.png')
              img = img.convert('RGB')
              img.save(filename+'.jpg')
              print("{}{}".format(filename, " has been changed!"))