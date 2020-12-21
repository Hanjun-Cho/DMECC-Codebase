import xlrd
import json

loc = (r"F:/Mothers English/Volunteer Data Tracker.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

total_student_count = 0
index_y = 1

while sheet.cell_value(index_y, 0) != "":
    total_student_count += 1
    index_y += 1

index_x = 0

for y in range(total_student_count):
    index_x = 0

    while sheet.cell_value(y + 1, index_x) != "":
        print(sheet.cell_value(y + 1, index_x))
        index_x += 1

