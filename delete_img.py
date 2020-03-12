import os
import glob
import fileinput
import sys

#browser all file with option extention
def browserFile(ext=""):
    return [f for f in glob.glob(f"*{ext}")]

#find and replace string in file
def replaceAll(file, searchExp, replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp, replaceExp)
        sys.stdout.write(line)

#count an object in xml file
def count(f, str):
    i = 0
    with open(f) as f:
        data = f.readlines()
    for line in data:
        if str in line:
            i+=1
    return i

xml_file = browserFile("*.xml") #browse all xml file
png_file = browserFile("*.png") #browse all jpg file

deleted = 0

for i in png_file: 
    jpg_name = i[:-4] + ".jpg" 
    if os.path.exists(jpg_name):
        os.remove(jpg_name)
        print("{}{}".format(jpg_name, " has been delete!"))
        deleted += 1

print("{}{}".format(deleted, " files have been deleted!"))