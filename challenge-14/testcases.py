from solution import calculate_net_salary

print("Running Test Cases...\n")

# Positive cases
print("Positive Cases:")
print(calculate_net_salary(1000000, 100000))   # 900000
print(calculate_net_salary(800000, 0))         # 800000

# Edge cases
print("\nEdge Cases:")
print(calculate_net_salary(0, 0))               # 0
print(calculate_net_salary(500000, 500000))     # 0

# Negative case
print("\nNegative Case:")
try:
    calculate_net_salary(-100000, 5000)
except ValueError as e:
    print("Exception:", e)
