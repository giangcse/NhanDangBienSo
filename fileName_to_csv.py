import pandas as pd
import os
import glob
import fileinput
import sys
# from collections import _DefaultDictT

# Duyet toan bo file theo dinh dang dua vao
def browserFile(ext=""):
    return [f for f in glob.glob(f"*{ext}")]

image = browserFile("*.jpg")
image_name = []
text = {'image_name': []}

for i in image:
    image_name.append(i[:-4])

text['image_name'] = image_name

df = pd.DataFrame(text, columns=['image_name'])
df.to_csv(r'ketqua.csv', index=False, header=True)
