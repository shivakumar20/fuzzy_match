import csv
#import xlsxwriter
ss_table_data_here = []
def ss_table():
    f_read_ss_table = open('ss_table_grt_1_match_distinct.csv',encoding="utf-8")
    csv_2 = csv.reader(f_read_ss_table)

    print(csv_2)

    next(csv_2)

    for i in csv_2:
        ss_table_data_here.append(i)

    #for i in range(0,len(ss_table_data_here)):
       #print(f"Sequence_no : {ss_table_data_here[i][0]}")
       #print(f"GST_no : {ss_table_data_here[i][1]}")
       #print(f"SS_name : {ss_table_data_here[i][2]}")
       #print(f"SS_add : {ss_table_data_here[i][3]}")

    #print(len(ss_table_data))
    

    #workbook = xlsxwriter.Workbook('ss_table_out.xlsx')
    #worksheet = workbook.add_worksheet("My sheet")
    #row = 0
    #col = 0
    #for gst_seq, gst_cust_name, ss_cust_name,ss_address in (ss_table_data):
    #    worksheet.write(row, col, gst_seq)
    #    worksheet.write(row, col + 1, gst_cust_name)
    #    worksheet.write(row, col + 2, ss_cust_name)
    #    worksheet.write(row, col + 3, ss_address)
    #    row = row + 1
    #workbook.close()

    return ss_table_data_here


