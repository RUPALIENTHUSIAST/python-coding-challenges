def calculate_taxable_income(annual_gross_salary):
    if annual_gross_salary < 0:
        raise ValueError("Annual gross salary cannot be negative.")

    STANDARD_DEDUCTION = 50000

    taxable_income = annual_gross_salary - STANDARD_DEDUCTION

    if taxable_income < 0:
        taxable_income = 0  # taxable income cannot go negative

    return {
        "annual_gross_salary": annual_gross_salary,
        "standard_deduction": STANDARD_DEDUCTION,
        "taxable_income": taxable_income
    }


if __name__ == "__main__":
    print("Enter Annual Salary Details:")
    annual_salary = float(input("Annual Gross Salary: "))

    result = calculate_taxable_income(annual_salary)

    print("\n------ Taxable Income Report ------")
    print(f"Annual Gross Salary: ₹{result['annual_gross_salary']}")
    print(f"Standard Deduction: ₹{result['standard_deduction']}")
    print(f"Taxable Income: ₹{result['taxable_income']}")
