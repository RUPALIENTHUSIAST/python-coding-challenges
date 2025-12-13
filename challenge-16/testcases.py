from solution import (
    validate_name,
    validate_empid,
    validate_salary,
    validate_bonus
)

print("Running Test Cases...\n")

# Positive Cases
print("Positive Cases:")
validate_name("Rupali")
validate_empid("EMP123")
validate_salary(50000)
validate_salary(0, allow_zero=True)
validate_bonus(25)
print("Positive cases passed ")

# Edge Cases
print("\nEdge Cases:")
validate_salary(1)
validate_bonus(0)
validate_bonus(100)
print("Edge cases passed ")

# Negative Cases
print("\nNegative Cases:")

try:
    validate_name("Rupali123")
except ValueError as e:
    print("Caught:", e)

try:
    validate_empid("E1")
except ValueError as e:
    print("Caught:", e)

try:
    validate_salary(-5000)
except ValueError as e:
    print("Caught:", e)

try:
    validate_bonus(150)
except ValueError as e:
    print("Caught:", e)
