import os
import glob
import sys
import xml.etree.ElementTree as ET
import shutil as st

#browser all file with option extention
def browserFile(ext=""):
    return [f for f in glob.glob(f"*{ext}")]

xml_file = browserFile("*.xml") #browse all xml file

def _find(str):
    file_name = []
    for i in xml_file:
        f = ET.parse(i)
        root = f.getroot()
        name = []
        for j in f.findall('object'):
            name.append((j.find("name").text))        
        if (str in name):
            file_name.append(i[:-4])
    return file_name

def _file(str):
    new_folder = "C:\\Users\\Giang\\Desktop\\plate\\" + str
    os.mkdir(new_folder)
    for i in _find(str):
        src_file_xml = i + ".xml"
        src_file_jpg = i + ".jpg"
        st.copy2(src_file_xml, new_folder)
        st.copy2(src_file_jpg, new_folder)
        print("Copied "+i)

if __name__ == "__main__":
    args = sys.argv[1:]
    for i in args:
        _file(i)