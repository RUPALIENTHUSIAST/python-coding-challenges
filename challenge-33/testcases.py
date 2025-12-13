# testcases.py
from solution import calculate_loyalty_points

print("Running Test Cases...\n")

# Positive Cases
print("Positive Cases:")
print("Grand Total: 1050 → Points:", calculate_loyalty_points(1050))  # 10
print("Grand Total: 999 → Points:", calculate_loyalty_points(999))    # 9
print("Grand Total: 0 → Points:", calculate_loyalty_points(0))        # 0

# Edge Cases
print("\nEdge Cases:")
print("Grand Total: 100 → Points:", calculate_loyalty_points(100))    # 1
print("Grand Total: 99 → Points:", calculate_loyalty_points(99))      # 0

# Negative Case
print("\nNegative Case:")
try:
    calculate_loyalty_points(-500)
except ValueError as e:
    print("Grand Total -500 → Error:", e)
