from solution import find_largest

print("Running Test Cases...\n")

# Positive Cases
print("Positive Cases:")
print("Input: 10, 20, 30 →", find_largest(10, 20, 30))  
print("Input: 5, 15, 10 →", find_largest(5, 15, 10))

# Edge Cases
print("\nEdge Cases:")
print("Input: -5, -10, -3 →", find_largest(-5, -10, -3))
print("Input: 7, 7, 7 →", find_largest(7, 7, 7))
print("Input: 1.5, 2.5, 0.5 →", find_largest(1.5, 2.5, 0.5))

# Mixed Cases
print("\nMixed Cases:")
print("Input: -1, 0, 1 →", find_largest(-1, 0, 1))
print("Input: 100, 50, 100 →", find_largest(100, 50, 100))
