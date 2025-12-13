def generate_employee_report(
    name,
    emp_id,
    gross_monthly_salary,
    annual_gross_salary,
    taxable_income,
    tax_payable,
    net_salary
):
    if gross_monthly_salary < 0 or annual_gross_salary < 0:
        raise ValueError("Salary values cannot be negative")

    if tax_payable < 0:
        raise ValueError("Tax payable cannot be negative")

    if net_salary < 0:
        raise ValueError("Net salary cannot be negative")

    print("\n========== Employee Tax Report ==========")
    print(f"{'Name':25}: {name}")
    print(f"{'EmpID':25}: {emp_id}")
    print(f"{'Gross Monthly Salary':25}: ₹{gross_monthly_salary:,.2f}")
    print(f"{'Annual Gross Salary':25}: ₹{annual_gross_salary:,.2f}")
    print(f"{'Taxable Income':25}: ₹{taxable_income:,.2f}")
    print(f"{'Tax Payable':25}: ₹{tax_payable:,.2f}")
    print(f"{'Annual Net Salary':25}: ₹{net_salary:,.2f}")
    print("========================================")


if __name__ == "__main__":
    try:
        name = input("Employee Name: ")
        emp_id = input("Employee ID: ")
        gross_monthly_salary = float(input("Gross Monthly Salary (₹): "))
        annual_gross_salary = float(input("Annual Gross Salary (₹): "))
        taxable_income = float(input("Taxable Income (₹): "))
        tax_payable = float(input("Tax Payable (₹): "))

        net_salary = annual_gross_salary - tax_payable

        generate_employee_report(
            name,
            emp_id,
            gross_monthly_salary,
            annual_gross_salary,
            taxable_income,
            tax_payable,
            net_salary
        )

    except ValueError as e:
        print("Error:", e)
