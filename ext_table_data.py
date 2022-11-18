import csv
#import xlsxwriter

ext_table_data_here = []

def ext_table():
    f_ext_table = open('ext_table_grt_1_match_distinct.csv',encoding = "utf-8")
    csv_3 =csv.reader(f_ext_table)
    next(csv_3)

    for i in csv_3:
        ext_table_data_here.append(i)

    #for i in range(0,len(ext_table_data_here)):
    #    print(f"Sequence No : {ext_table_data_here[i][0]}")
    #    print(f"Gst No : {ext_table_data_here[i][1]}")
    #    print(f"ext_name No : {ext_table_data_here[i][2]}")
    #    print(f"ext_add No : {ext_table_data_here[i][3]}")
        #ext_table_data_here[i][0] = "ext_" + ext_table_data_here[i][0]
        #print(ext_table_data_here[i][0])

    #workbook = xlsxwriter.Workbook('ext_table_out.xlsx')
    #worksheet = workbook.add_worksheet("My sheet")
    #row = 0
    #col = 0
    #for gst_seq, ext_gst_number, ext_cust_name,ext_address in (ext_table_data):
    #    worksheet.write(row, col, gst_seq)
    #    worksheet.write(row, col + 1, ext_gst_number)
    #    worksheet.write(row, col + 2, ext_cust_name)
    #    worksheet.write(row, col + 3, ext_address)
    #    row = row + 1
    #workbook.close()
    

    
    #print(len(ext_table_data))
    return ext_table_data_here

