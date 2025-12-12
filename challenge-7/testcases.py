from solution import check_tax_eligibility

print("Running Test Cases...\n")

# Positive Cases
print("Positive Cases:")
print(check_tax_eligibility("Rupali", 500000))  # tax
print(check_tax_eligibility("Aman", 200000))    # no tax

# Negative Case (should raise error)
print("\nNegative Case:")
try:
    check_tax_eligibility("Test", -50000)
except ValueError as e:
    print("Exception:", e)

# Edge Cases
print("\nEdge Cases:")
print(check_tax_eligibility("Meena", 0))
print(check_tax_eligibility("Rohan", 300000))   # exactly 3L → no tax
print(check_tax_eligibility("Priya", 300001))   # just above threshold
