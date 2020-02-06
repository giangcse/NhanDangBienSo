import os
import glob
import fileinput
import sys

def xlmBrowser(ext=""):
    return [f for f in glob.glob(f"*{ext}")]

def replaceAll(file, searchExp, replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp, replaceExp)
        sys.stdout.write(line)

x = xlmBrowser("*.xml")
for i in x:
    replaceAll(i, "C:\\Users\\Administrator\\Desktop\\", "D:\\Data\\")
    print("Changed " + i)