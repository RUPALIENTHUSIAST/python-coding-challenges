# testcases.py
from solution import print_number_increasing_pattern

print("Running Test Cases...\n")

# Positive cases
print("Positive Cases:")
print("\nN = 5")
print_number_increasing_pattern(5)

print("\nN = 10")
print_number_increasing_pattern(10)

# Edge cases
print("\nEdge Case: N = 1")
print_number_increasing_pattern(1)

print("\nEdge Case: Maximum allowed N = 1000 (only first 10 rows printed for safety)")
for i in range(1, 11):
    print(str(i) * i)

# Negative / invalid cases
print("\nNegative / Invalid Cases:")
for invalid in [0, -5, "abc", 10001]:
    try:
        print(f"\nTesting N = {invalid}")
        print_number_increasing_pattern(invalid)
    except Exception as e:
        print("Caught Error:", e)
