import json
import xlrd

loc = (r"Volunteer Data Tracker.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

total_student_count = 0
index_y = 1

data = {
    "Volunteer" : [
        
    ]
}

with open(r"Volunteer Data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

while sheet.cell_value(index_y, 0) != "":
    total_student_count += 1
    index_y += 1

index_x = 0

for y in range(total_student_count):
    index_x = 0
    y += 1

    dataAppend = {
        sheet.cell_value(y, index_x) : {
            sheet.cell_value(0, 1) : sheet.cell_value(y, 1),
            sheet.cell_value(0, 2) : sheet.cell_value(y, 2),
            sheet.cell_value(0, 3) : int(sheet.cell_value(y, 3)),
            sheet.cell_value(0, 4) : sheet.cell_value(y, 4),
            sheet.cell_value(0, 5) : str(sheet.cell_value(y, 5)),
            sheet.cell_value(0, 6) : sheet.cell_value(y, 6),
            sheet.cell_value(0, 7) : sheet.cell_value(y, 7),
            sheet.cell_value(0, 8) : sheet.cell_value(y, 8),
            sheet.cell_value(0, 9) : str(sheet.cell_value(y, 9)),
            sheet.cell_value(0, 10) : sheet.cell_value(y, 10),
            sheet.cell_value(0, 11) : sheet.cell_value(y, 11)
        }
    }

    with open('Volunteer Data.json') as json_file: 
        data = json.load(json_file) 
        
        temp = data['Volunteer'] 
        temp.append(dataAppend) 

    with open('Volunteer Data.json','w') as f: 
        json.dump(data, f, indent=4) 