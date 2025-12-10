# test_solution.py
from solution import swap_numbers

print("Running Test Cases...\n")

# Positive Cases
print("Positive Cases:")
print(f"Input: 10, 20 → {swap_numbers(10, 20)}")        # (20, 10)
print(f"Input: 5.5, 4.5 → {swap_numbers(5.5, 4.5)}")    # (4.5, 5.5)

# Negative Cases
print("\nNegative Cases:")
print(f"Input: -5, -10 → {swap_numbers(-5, -10)}")      # (-10, -5)
print(f"Input: -3, 7 → {swap_numbers(-3, 7)}")          # (7, -3)

# Edge Cases
print("\nEdge Cases:")
print(f"Input: 0, 0 → {swap_numbers(0, 0)}")            # (0, 0)
print(f"Input: 1e9, -1e9 → {swap_numbers(1e9, -1e9)}")  # (-1e9, 1e9)
