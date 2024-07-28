# Declaring variables for salary calculation

print:wq("How much overtime did you work this month? ", end='')
overTime = float(input()) * 2.0
print("How many hours did you work this month? ", end='')
hours = float(input())
deductions = 4700.0
rate = 103.14

# Operations to calculate salary

hoursWorked = hours + overTime
grossSalary = hoursWorked * rate
netSalary = grossSalary - deductions

# Printing outputs in console

print("Hours worked: ", hoursWorked)
print("Gross salary: ", grossSalary)
print("Net salary: ", netSalary)


