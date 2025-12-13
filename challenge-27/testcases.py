from solution import apply_discounts

print("Running Test Cases...\n")

# Positive Case
print("Positive Case:")
final_total, details = apply_discounts(15000, 25)
print("Final Total:", final_total)
print("Details:", details)

# Edge Case (exact threshold)
print("\nEdge Case:")
final_total, details = apply_discounts(10000, 20)
print("Final Total:", final_total)
print("Details:", details)

# Only amount discount
print("\nOnly Amount Discount:")
final_total, details = apply_discounts(12000, 10)
print("Final Total:", final_total)
print("Details:", details)

# Only quantity discount
print("\nOnly Quantity Discount:")
final_total, details = apply_discounts(9000, 30)
print("Final Total:", final_total)
print("Details:", details)

# Negative Case
print("\nNegative Case:")
try:
    apply_discounts(-5000, 10)
except ValueError as e:
    print("Caught Error:", e)
