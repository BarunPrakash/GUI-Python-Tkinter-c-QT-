# designed by Barun
# 28/9/2019
# objective :- to test the lib utility
# xlrd is a stable library utility .



import xlrd 
  
attri = ("test.xlsx") # read val from col
  
openSheet = xlrd.open_workbook(attri) 
sheet = openSheet.sheet_by_index(0) 
  
# For row 0 and column 0 
sheet.cell_value(0, 0) 
  
for i in range(sheet.ncols): 
    print(sheet.cell_value(0, i)) 
