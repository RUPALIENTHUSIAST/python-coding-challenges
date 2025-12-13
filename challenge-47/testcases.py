from solution import store_elements

print("Running Test Cases...\n")

# Positive Case
print("Positive Case:")
print(store_elements(3, [10, 20, 30]))

# Edge Case
print("\nEdge Case:")
try:
    print(store_elements(0, []))
except Exception as e:
    print("Caught Error:", e)

# Negative Case
print("\nNegative Case:")
try:
    print(store_elements(3, [1, 2]))
except Exception as e:
    print("Caught Error:", e)
