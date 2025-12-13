# testcases.py
from solution import print_number_sequence_pattern

print("Running Test Cases...\n")

# Positive Cases
print("Positive Case: N = 5")
print_number_sequence_pattern(5)

print("\nPositive Case: N = 10")
print_number_sequence_pattern(10)

# Edge Case
print("\nEdge Case: N = 1")
print_number_sequence_pattern(1)

# Large N (first 10 rows only for safety)
print("\nEdge Case: Large N = 1000 (printing only first 10 rows)")
for i in range(1, 11):
    print(''.join(str(num) for num in range(1, i + 1)))

# Negative / Invalid Cases
for invalid in [0, -5, "abc", 10001]:
    try:
        print(f"\nTesting N = {invalid}")
        print_number_sequence_pattern(invalid)
    except Exception as e:
        print("Caught Error:", e)
