import csv
import numpy as np
from rapidfuzz import fuzz
import xlsxwriter
from ss_table_data import ss_table
from ext_table_data import ext_table

unique_gst_no = []
fuzz_name_record_list = []
f_unique_gst = open('unique_gst_no.csv',encoding = "utf-8")

csv_1 = csv.reader(f_unique_gst)

next(csv_1)
for i in csv_1:
    unique_gst_no.append(i[0])

ss_table_data = ss_table()
#SS_table_data Formate: Sequence_no, GST_no, SS_name, SS_add


#for i in range(0,len(ss_table_data)):
#    print(ss_table_data[i])

ext_table_data = ext_table()
# ext_table_data Fromate : Seq_No,Gst_No,ext_name,ext_add
full_name_match = []
name_match = []
count =0

for j in range(0,len(ss_table_data)):
    max_score = 0
    max_score_index = 0
    name_match = []
    for k in range(0,len(ext_table_data)):
        if ss_table_data[j][1] == ext_table_data[k][1]:
            score = fuzz.ratio((ss_table_data[j][3]),(ext_table_data[k][2]))
            print(fuzz.ratio((ss_table_data[j][3]),(ext_table_data[k][2])))
            count = count + 1
            if score > max_score:
                max_score = score
                max_score_index = k
    if max_score_index != 0:
        name_match.append(ss_table_data[j][1])                #GST_no_ss
        name_match.append(ss_table_data[j][0])                #SEQ_ss
        name_match.append(ext_table_data[max_score_index][0]) #SEQ_ext
        name_match.append(ss_table_data[j][2])                #ss_table_name
        name_match.append(ext_table_data[max_score_index][2]) #ext_table_name
        name_match.append(max_score)                          #Max score
        full_name_match.append(name_match)                    #Full row Updation


        
print(count)
print(len(full_name_match))


workbook = xlsxwriter.Workbook('Address_match.xlsx')
worksheet = workbook.add_worksheet("My sheet") 
row = 0
col = 0
for unique_gst,ss_seq,ext_seq,ss_name,ext_name,f_score in full_name_match:
    worksheet.write(row, col, unique_gst)
    worksheet.write(row, col + 1, ss_seq) 
    worksheet.write(row, col + 2, ext_seq)
    worksheet.write(row, col + 3, ss_name)
    worksheet.write(row, col + 4, ext_name)
    worksheet.write(row, col + 5, f_score)
    row = row + 1
workbook.close()

      
            





#print(f"The Length of unique GST : {len(unique_gst_no)}")
#print(f"The Length of unique SS_TABLE : {len(ss_table_data)}")
#print(f"The Length of unique EXT_TABLE : {len(ext_table_data)}")


