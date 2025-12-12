from solution import is_leap_year

print("Running Test Cases...\n")

# Positive Normal Cases
print("Positive Cases:")
print("Year 2024 →", is_leap_year(2024))  # True
print("Year 2023 →", is_leap_year(2023))  # False
print("Year 2000 →", is_leap_year(2000))  # True
print("Year 1900 →", is_leap_year(1900))  # False

# Edge Cases
print("\nEdge Cases:")
print("Year 0 →", is_leap_year(0))        # True (0 % 400 == 0)
print("Year 1 →", is_leap_year(1))        # False

# Error Case
print("\nError Case:")
try:
    is_leap_year(-2024)
except ValueError as e:
    print("Negative year → Exception:", e)
