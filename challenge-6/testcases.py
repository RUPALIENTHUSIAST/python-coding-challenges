from solution import is_even_or_odd

print("Running Test Cases...\n")

# Positive Cases
print("Positive Cases:")
print(f"Input: 10 → {is_even_or_odd(10)}")  # Even
print(f"Input: 7 → {is_even_or_odd(7)}")    # Odd

# Edge Cases
print("\nEdge Cases:")
print(f"Input: 0 → {is_even_or_odd(0)}")    # Even
print(f"Input: -4 → {is_even_or_odd(-4)}")  # Even
print(f"Input: -9 → {is_even_or_odd(-9)}")  # Odd

# Invalid Input
print("\nInvalid Cases:")
try:
    is_even_or_odd(5.5)
except ValueError as e:
    print(f"Input: 5.5 → Exception: {e}")
