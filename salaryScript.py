def grossSalary(hoursWorked, overtimeWorked):
    print(f"You've worked {hoursWorked} hours this month.")
    print(f"You've worked {overtimeWorked} hours of overtime this month.")

hoursWorked = float(input("Normal hours worked: "))
overtimeWorked = float(input(f"Overtime hours worked: "))
deductions = 4500
rate = 103.14
overtimeRate = rate * 2
totalHours = hoursWorked + overtimeWorked
grossSalary = (hoursWorked * rate) + (overtimeWorked * overtimeRate)
netSalary = grossSalary - deductions



print(f"Hours worked: :{totalHours}")
print(f"Gross salary: {grossSalary}")
print(f"Net salary: {netSalary}")
