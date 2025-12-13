from solution import calculate_final_total

print("Running Test Cases...\n")

# Positive Case
print("Positive Case:")
print(calculate_final_total(15000, 25, True))
# Expected: discounts applied

# Edge Case
print("\nEdge Case:")
print(calculate_final_total(10000, 20, False))
# Expected: no discount

# Quantity Discount Only
print("\nQuantity Discount Only:")
print(calculate_final_total(8000, 30, False))

# Member Discount Only
print("\nMember Discount Only:")
print(calculate_final_total(8000, 10, True))

# Negative Case
print("\nNegative Case:")
try:
    calculate_final_total(-5000, 10, True)
except ValueError as e:
    print("Caught Error:", e)
