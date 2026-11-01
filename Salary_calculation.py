staff_name = input("Enter staff name: ")
basic_salary = float(input("Enter basic salary (OMR): "))
allowance = float(input("Enter allowance (OMR): ")

bonus = 100

gross_salary = basic_salary + allowance + bonus

print("\nStaff:", staff_name)
print("Bonus:", bonus, "OMR")
print("Gross Salary:", gross_salary, "OMR")
