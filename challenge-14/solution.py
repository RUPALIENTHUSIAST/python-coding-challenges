def calculate_net_salary(annual_gross_salary, total_tax_payable):
    if annual_gross_salary < 0:
        raise ValueError("Annual gross salary cannot be negative.")

    if total_tax_payable < 0:
        raise ValueError("Tax payable cannot be negative.")

    if total_tax_payable > annual_gross_salary:
        raise ValueError("Tax payable cannot be greater than gross salary.")

    net_salary = annual_gross_salary - total_tax_payable
    return net_salary


if __name__ == "__main__":
    try:
        gross_salary = float(input("Enter Annual Gross Salary (₹): "))
        tax_payable = float(input("Enter Total Tax Payable (₹): "))

        net_salary = calculate_net_salary(gross_salary, tax_payable)

        print("\n------ Net Salary Report ------")
        print(f"Annual Gross Salary: ₹{gross_salary:,.2f}")
        print(f"Total Tax Payable: ₹{tax_payable:,.2f}")
        print(f"Annual Net Salary: ₹{net_salary:,.2f}")

    except ValueError as e:
        print("Error:", e)
