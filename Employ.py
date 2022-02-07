import csv

employee = open('EmployeePay.csv','r')
employee_file = csv.reader(employee, delimiter =',')


next(employee_file)

for record in employee_file:
    bonus = int(record[3])*float(record[4])
    total = float(record[3])+bonus
    print('ID',record[0])
    print('first name', record[1])
    print('last name', record[2])
    print('total pay', total)

employee.close()
    
    