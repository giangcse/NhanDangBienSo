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

#List of element can be exist, do not have plate!!
eList = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L',
    'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V', 'X', 'Y',
    'Z', 'LD'
]

# e0 = e1 = e2 = e3 = e4 = e5 = e6 = e7 = e8 = e9 = eA = eB = eC = eD = eE = eF = eG = eH = eK = eL = eM = eN = eP = eR = eS = eT = eU = eV = eX = eY = eZ = 0
#Dictonary of number of element
numOfElement = {
    "0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0,
    "A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "K":0, "L":0,
    "M":0, "N":0, "P":0, "R":0, "S":0, "T":0, "U":0, "V":0, "X":0, "Y":0,
    "Z":0, "LD":0
}

for i in xml_file:
    for j in eList:
        numOfElement[j] += count(i, "<name>"+j+"</name>")

for i in numOfElement:
    print("{}{}{}".format(i, ": ", numOfElement[i]))