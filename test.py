import xlrd
loc = ("data.xls")
book = xlrd.open_workbook(loc)
sheet = book.sheet_by_index(0)
for i in range(sheet.nrows):
    print(sheet.row(i))