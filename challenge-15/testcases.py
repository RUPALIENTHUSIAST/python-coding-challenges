from solution import generate_employee_report

print("Running Test Cases...\n")

# Positive Case
print("Positive Case:")
generate_employee_report(
    name="John Doe",
    emp_id="E12345",
    gross_monthly_salary=85000,
    annual_gross_salary=1020000,
    taxable_income=970000,
    tax_payable=76800,
    net_salary=943200
)

# Edge Case
print("\nEdge Case:")
generate_employee_report(
    name="Alice",
    emp_id="E00001",
    gross_monthly_salary=50000,
    annual_gross_salary=600000,
    taxable_income=550000,
    tax_payable=0,
    net_salary=600000
)

# Negative Case
print("\nNegative Case:")
try:
    generate_employee_report(
        name="Bob",
        emp_id="E999",
        gross_monthly_salary=-1000,
        annual_gross_salary=500000,
        taxable_income=450000,
        tax_payable=20000,
        net_salary=480000
    )
except ValueError as e:
    print("Caught Error:", e)
