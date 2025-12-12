from solution import calculate_salary

print("Running Test Cases...\n")

# Positive Cases
print("Positive Case 1:")
print(calculate_salary("Riya", "E101", 30000, 5000, 10))

print("\nPositive Case 2:")
print(calculate_salary("Amit", "E102", 45000, 8000, 20))

# Edge Cases
print("\nEdge Case: Zero Allowance & Zero Bonus")
print(calculate_salary("Sam", "E103", 25000, 0, 0))

# Negative Case
try:
    print("\nNegative Case: Negative Salary")
    calculate_salary("John", "E104", -30000, 5000, 10)
except ValueError as e:
    print("Error:", e)
