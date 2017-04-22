
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('sheet 1')


my_list = list(range(2, 501))

for numbers in my_list:
    if numbers % 2 == 0:
        sheet1.write(numbers, 0, numbers)


wb.save('500 exercise.xls')
