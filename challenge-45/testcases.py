from solution import separate_whole_fraction

print("Running Test Cases...\n")

# Test Case 1: Normal decimal
w, f = separate_whole_fraction(123.456)
print("Input: 123.456")
print("Whole:", w, "Fraction:", f)

# Test Case 2: Integer input
w, f = separate_whole_fraction(50)
print("\nInput: 50")
print("Whole:", w, "Fraction:", f)

# Test Case 3: Negative value
w, f = separate_whole_fraction(-78.25)
print("\nInput: -78.25")
print("Whole:", w, "Fraction:", f)

# Test Case 4: Zero
w, f = separate_whole_fraction(0.0)
print("\nInput: 0.0")
print("Whole:", w, "Fraction:", f)

# Test Case 5: Invalid input
try:
    separate_whole_fraction("abc")
except Exception as e:
    print("\nInvalid Input Test Passed:", e)
