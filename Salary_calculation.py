staff_name = input("Enter staff name: ")
basic_salary = float(input("Enter basic salary (OMR): "))
allowance = float(input("Enter allowance (OMR): "))

bonus = 100

gross_salary = basic_salary + allowance + bonus

has_loan = input("Does the staff have a loan? (yes/no): ").lower()

if has_loan == "yes":
    loan_repayment = float(input("Enter current loan repayment (OMR): "))
else:
    loan_repayment = 0

other_deductions = float(input("Enter other deductions (OMR): "))

net_salary = gross_salary - other_deductions - loan_repayment

print("\nStaff:", staff_name)
print("Gross Salary:", gross_salary, "OMR")
print("Net Salary:", net_salary, "OMR")
