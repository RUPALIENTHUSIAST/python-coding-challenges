from solution import calculate_item_total

print("Running Test Cases...\n")

# Positive cases
print("Positive Cases:")
print("Item total (2, 50) →", calculate_item_total(2, 50))   # 100
print("Item total (5, 99.5) →", calculate_item_total(5, 99.5))  # 497.5

# Edge cases
print("\nEdge Cases:")
print("Item total (1, 0) →", calculate_item_total(1, 0))  # 0

# Negative cases
print("\nNegative Cases:")
try:
    calculate_item_total(0, 100)
except ValueError as e:
    print("Quantity 0 → Error:", e)

try:
    calculate_item_total(2, -50)
except ValueError as e:
    print("Negative price → Error:", e)
