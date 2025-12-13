from solution import reverse_number

print("Running Test Cases...\n")

# Positive number
print("Test 1:", reverse_number(12345))   # Expected: 54321

# Number with trailing zero
print("Test 2:", reverse_number(1200))    # Expected: 21

# Negative number
print("Test 3:", reverse_number(-987))    # Expected: -789

# Zero
print("Test 4:", reverse_number(0))       # Expected: 0

# Single digit
print("Test 5:", reverse_number(7))       # Expected: 7
