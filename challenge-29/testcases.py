from solution import calculate_tax

print("Running Test Cases...\n")

# Positive Cases
print("Positive Cases:")
print("₹3000 →", calculate_tax(3000))     # 5%
print("₹10000 →", calculate_tax(10000))  # 10%
print("₹25000 →", calculate_tax(25000))  # 15%

# Edge Cases
print("\nEdge Cases:")
print("₹5000 →", calculate_tax(5000))     # 10%
print("₹20000 →", calculate_tax(20000))   # 10%

# Negative Case
print("\nNegative Case:")
try:
    calculate_tax(-1000)
except ValueError as e:
    print("Exception:", e)
