# testcases.py
from solution import check_minimum_purchase

print("Running Test Cases...\n")

# Positive Case - above minimum
final_amount = 1000
print("Test Case 1: Amount above minimum")
check_minimum_purchase(final_amount)

# Edge Case - exactly minimum
final_amount = 500
print("\nTest Case 2: Amount exactly at minimum")
check_minimum_purchase(final_amount)

# Negative Case - below minimum
final_amount = 250
print("\nTest Case 3: Amount below minimum")
check_minimum_purchase(final_amount)

# Negative Case - negative amount
try:
    final_amount = -100
    print("\nTest Case 4: Negative amount")
    check_minimum_purchase(final_amount)
except ValueError as e:
    print("Caught Error:", e)
