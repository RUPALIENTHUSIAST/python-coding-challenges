# testcases.py
from solution import apply_payment_surcharge

print("Running Test Cases...\n")

# Positive Case - Cash
grand_total = 10000
payment_method = "Cash"
surcharge, final_amount = apply_payment_surcharge(grand_total, payment_method)
print(f"Cash Payment: Surcharge={surcharge}, Final Amount={final_amount}")

# Positive Case - Credit Card
grand_total = 10000
payment_method = "Credit Card"
surcharge, final_amount = apply_payment_surcharge(grand_total, payment_method)
print(f"Credit Card Payment: Surcharge={surcharge}, Final Amount={final_amount}")

# Edge Case - Zero Grand Total
grand_total = 0
payment_method = "Cash"
surcharge, final_amount = apply_payment_surcharge(grand_total, payment_method)
print(f"Zero Total (Cash): Surcharge={surcharge}, Final Amount={final_amount}")

# Negative Case - Invalid Payment Method
try:
    apply_payment_surcharge(1000, "Bitcoin")
except ValueError as e:
    print("Invalid Payment Method Error:", e)

# Negative Case - Negative Grand Total
try:
    apply_payment_surcharge(-500, "Cash")
except ValueError as e:
    print("Negative Grand Total Error:", e)
