# testcases.py
from solution import calculate_item_total

print("Running Test Cases...\n")

# Positive Case – Promo Applied
print("Positive Case (PROMO10):")
total, discount = calculate_item_total("PROMO10", 2, 500)
print("Expected Discount: 100")
print("Total:", total, "Discount:", discount)

# Positive Case – No Promo
print("\nPositive Case (No Promo):")
total, discount = calculate_item_total("ITEM01", 3, 200)
print("Expected Discount: 0")
print("Total:", total, "Discount:", discount)

# Edge Case
print("\nEdge Case:")
total, discount = calculate_item_total("promo10", 1, 100)
print("Total:", total, "Discount:", discount)

# Negative Case
print("\nNegative Case:")
try:
    calculate_item_total("PROMO10", -1, 100)
except ValueError as e:
    print("Caught Error:", e)
