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
jpg_file = browserFile("*.jpg") #browse all jpg file

xml_num = 0 #number of xml file
jpg_num = 0 #number of jpg file
object_class_num = 0 #number of object class
object_num = 0 #number of object

#loop all xml file
for i in xml_file:
    xml_num+=1 #counting xml file
    object_class_num = count(i, "<object>")
    print("{}{}{}{}".format(i, "\t: ", object_class_num, "\tobject(s)"))
    # print(i)

#counting jpg file
for j in jpg_file:
    jpg_num+=1

#print result
print("We have: ")
print ("{}{}{}".format("\t", jpg_num, " image files"))    
print ("{}{}{}".format("\t", xml_num, " xml files"))