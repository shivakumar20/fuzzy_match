import csv
import numpy as np
from thefuzz import fuzz, process
import xlsxwriter


f = open('ext_data.csv',encoding = "utf-8")
csv_1 = csv.reader(f)
next(csv_1)

ext_syspk = []
ext_name_list = []
sec_syspk = []
sec_name_list = []
address = []
new_address = []
final = []

for i in csv_1:
    #print(i[1])
    ext_syspk.append(i[0])
    ext_name_list.append(i[1])

f2 = open('sec_data.csv',encoding = "utf-8")
csv_2 = csv.reader(f2)
next(csv_2)

for i in csv_2:
    sec_syspk.append(i[0])
    sec_name_list.append(i[1])

print(len(ext_syspk))
print(len(ext_name_list))
print(len(sec_syspk))
print(len(sec_name_list))

score = 0
# for i in range(0,len(sec_name_list)):
#     x = process.extract(sec_name_list[i],ext_name_list,limit = 1,scorer=fuzz.token_set_ratio)
#     print(f"Print sec_name : {sec_name_list[i]}")
#     print(f"Print ext_match : {x[0]}")

sec_name_list = np.asarray(sec_name_list)
sec_syspk = np.asarray(sec_syspk)
ext_syspk = np.asarray(ext_syspk)
ext_name_list = np.asarray(ext_name_list)
result = []

for i in range(0,len(sec_name_list)):
    max_score = 0
    ext_name_index_num = 0
    for j in range(0,len(ext_name_list)):
        score = fuzz.token_sort_ratio(sec_name_list[i],ext_name_list[j])
        if max_score < score:
            uppend = []
            max_score = score
            ext_name_index_num = j
            # print(sec_name_list[i])
            # print(max_score)
            # print(ext_name_list[ext_name_index_num])
            uppend.append(sec_syspk[i])
            uppend.append(sec_name_list[i])
            uppend.append(max_score)
            uppend.append(ext_name_list[ext_name_index_num])
            uppend.append(ext_syspk[ext_name_index_num])
    result.append(uppend)
    print(result[i])

workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet("My sheet")
row = 0
col = 0
worksheet.write(0,0,"sec_syspk")
worksheet.write(0,1,"sec_name")
worksheet.write(0,2,"ext_name")
worksheet.write(0,3,"ext_syspk")
for a,b,c,d,e in result:
    worksheet.write(row+1, col, a)
    worksheet.write(row+1, col+1,b)
    worksheet.write(row+1, col+2,c)
    worksheet.write(row+1, col+3,d)
    worksheet.write(row+1, col+4,e)
    row = row + 1
workbook.close()


    

