from solution import calculate_item_total

print("Running Test Cases...\n")

# Positive Case
print("Positive Case:")
item = calculate_item_total("A101", "Pen", 10, 5)
print(item)

# Edge Case
print("\nEdge Case:")
item = calculate_item_total("B202", "Notebook", 1, 50)
print(item)

# Negative Cases
print("\nNegative Cases:")

try:
    calculate_item_total("", "Book", 2, 100)
except ValueError as e:
    print("Error:", e)

try:
    calculate_item_total("C303", "Pencil", 0, 10)
except ValueError as e:
    print("Error:", e)

try:
    calculate_item_total("D404", "Eraser", 5, -2)
except ValueError as e:
    print("Error:", e)
