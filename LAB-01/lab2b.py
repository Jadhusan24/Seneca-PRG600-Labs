'''
Name: Jadhusan M Sadhik
Student ID: 155547227
Description: Lab 2B.
'''

try:
    gross_income = float(input("Enter your gross income: "))
    num_dependents = int(input("Enter the number of dependents: "))

    if gross_income <= 32000:
        tax_rate = 0.10
    elif gross_income <= 64000:
        tax_rate = 0.15
    else:
        tax_rate = 0.25

    standard_deduction = 10000
    dependent_deduction = 2000 * num_dependents
    total_deduction = standard_deduction + dependent_deduction

    taxable_income = gross_income - total_deduction
    income_tax = taxable_income * tax_rate
    income_tax = max(income_tax, 0)
    total_tax = income_tax

    print(f"The income tax is ${total_tax:.2f}")

except KeyboardInterrupt:
    print("\n Don't Forget To Pay Taxes, See you again!")
except ValueError:
    print("NUMBERS ONLY")
