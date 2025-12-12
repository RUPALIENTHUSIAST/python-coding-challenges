from solution import calculate_taxable_income

print("Running Test Cases for Challenge 12...\n")

# Positive Cases
print("Positive Cases:")
print("Annual Salary 10,00,000 →", calculate_taxable_income(1000000))
print("Annual Salary 60,000 →", calculate_taxable_income(60000))  # Leaves 10k taxable

# Edge Cases
print("\nEdge Cases:")
print("Annual Salary exactly 50,000 →", calculate_taxable_income(50000))  # Taxable = 0
print("Annual Salary 0 →", calculate_taxable_income(0))  # Taxable = 0

# Negative Case
print("\nNegative Case:")
try:
    calculate_taxable_income(-500000)
except ValueError as e:
    print("Negative Salary → Exception:", e)
