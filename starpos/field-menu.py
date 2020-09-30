#-*- coding: utf-8 -*
import openpyxl



filename = 'G:\starpos\강남BBQ\Gangnam BBQ.xlsx'
output_file = 'G:\starpos\강남BBQ\edit.txt'
book = openpyxl.load_workbook(filename)

sheet = book.active

with open(output_file, 'w', -1, 'utf-8', newline='') as filewriter:
    for i in range(0, 118):

        ta = sheet["A" + str(i+1)].value
        sb = sheet["B" + str(i+1)].value
        ea = sheet["C" + str(i+1)].value
        img = sheet["D" + str(i+1)].value
        filewriter.write('(' + str(i+1) + ',' + str(ta) + ',' + "'0845742'" + ',') # pt_id, cate_id, branch_id
        filewriter.write("'")
        filewriter.write('{')
        filewriter.write('"ko"')
        filewriter.write(':')
        filewriter.write('"')
        filewriter.write(str(sb) + '"')
        filewriter.write( ',')
        filewriter.write('"en":"", "vn":""')
        filewriter.write('}')
        filewriter.write("'")
        filewriter.write(', 1, 0,')
        filewriter.write(str(ea))
        filewriter.write(', 0, 10,0, 1,')
        filewriter.write("'ea'")
        filewriter.write(",'")
        filewriter.write('[1,')
        filewriter.write('"","","","",""]')
        filewriter.write("'")        
        filewriter.write(', ')
        filewriter.write("'")
        filewriter.write('["","","","","",""]')
        filewriter.write("'")
        filewriter.write(', ')
        filewriter.write("'")
        filewriter.write(str(img))
        filewriter.write("'")
        filewriter.write(', 1, 0, ')
        filewriter.write("'{}',")
        filewriter.write('0, ')
        filewriter.write("'0'")
        filewriter.write(')')
        filewriter.write(',' +'\n')

print ('OK')        