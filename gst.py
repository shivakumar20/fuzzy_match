import csv
import xlsxwriter
import xlwt
from thefuzz import fuzz, process
import numpy
import pandas as pd

gst_no = []
ext_sub_data = []
ext_data = []

f = open('book1.csv',encoding="utf-8")
csv_1 = csv.reader(f)

print(csv_1)
next(csv_1)
for i in csv_1:
    gst_no.append(i[0])
    



f2 = open('book2.csv',encoding="utf-8")
csv_2 = csv.reader(f2)

print(csv_2)
next(csv_2)

for j in csv_2:
    for z in j:
        ext_sub_data.append(z)
    ext_data.append(ext_sub_data)
j = 0
for i in ext_data:
    for j in i:
        print(j)
print(len(ext_data))
print(len(gst_no))


    