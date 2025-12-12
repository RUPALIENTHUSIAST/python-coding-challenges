def calculate_salary(name, emp_id, basic_salary, allowances, bonus_percentage):
    # ---- VALIDATIONS ----
    if basic_salary <= 0:
        raise ValueError("Basic Salary must be greater than 0.")
    if allowances < 0:
        raise ValueError("Allowances cannot be negative.")
    if bonus_percentage < 0:
        raise ValueError("Bonus percentage cannot be negative.")

    # ---- CALCULATIONS ----
    gross_monthly = basic_salary + allowances
    annual_gross = (gross_monthly * 12) + (gross_monthly * bonus_percentage / 100)

    return {
        "name": name,
        "emp_id": emp_id,
        "gross_monthly": gross_monthly,
        "annual_gross": annual_gross
    }


if __name__ == "__main__":
    print("Enter Employee Details:")

    name = input("Employee Name: ")
    emp_id = input("Employee ID: ")

    basic_salary = float(input("Basic Monthly Salary: "))
    allowances = float(input("Special Allowances (Monthly): "))
    bonus_percentage = float(input("Bonus Percentage (%): "))

    result = calculate_salary(name, emp_id, basic_salary, allowances, bonus_percentage)

    print("\n------ Employee Salary Report ------")
    print(f"Name: {result['name']}")
    print(f"Employee ID: {result['emp_id']}")
    print(f"Gross Monthly Salary: {result['gross_monthly']}")
    print(f"Annual Gross Salary: {result['annual_gross']}")
