def calculate_payroll(name, hours_worked, hourly_rate, tax_rate=0.10):
    gross_pay = hours_worked * hourly_rate
    tax = gross_pay * tax_rate
    net_pay = gross_pay - tax

    return {
        'name': name,
        'hours_worked': hours_worked,
        'hourly_rate': hourly_rate,
        'gross_pay': gross_pay,
        'tax': tax,
        'net_pay': net_pay
    }

def print_payroll(payroll):
    print("\nPayroll Summary:")
    print(f"Employee Name: {payroll['name']}")
    print(f"Hours Worked: {payroll['hours_worked']}")
    print(f"Hourly Rate: ${payroll['hourly_rate']:.2f}")
    print(f"Gross Pay: ${payroll['gross_pay']:.2f}")
    print(f"Tax Deducted: ${payroll['tax']:.2f}")
    print(f"Net Pay: ${payroll['net_pay']:.2f}")

def main():
    print("Welcome to the Employee Payroll Calculator!")
    name = input("Enter employee name: ")
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
   
    payroll = calculate_payroll(name, hours_worked, hourly_rate)
    print_payroll(payroll)

if __name__ == "__main__":
    main()