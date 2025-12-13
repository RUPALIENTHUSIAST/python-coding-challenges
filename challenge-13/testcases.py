# testcases.py
from solution import calculate_tax

print("Running Test Cases for Tax Calculation...\n")

test_cases = [
    ("Income within rebate limit", 6),        # Section 87A rebate
    ("Income just above rebate limit", 700001),
    ("Income in mid slab", 1200000),
    ("Income high", 2000000),
    ("Income at exact slab boundary", 1500000),
    ("Income zero", 0),
]

for description, income in test_cases:
    try:
        tax, cess, total_tax = calculate_tax(income)
        print(f"{description}: ₹{income:,.2f}")
        print(f"  Tax (before cess): ₹{tax:,.2f}")
        print(f"  Health & Education Cess (4%): ₹{cess:,.2f}")
        print(f"  Total Tax Payable: ₹{total_tax:,.2f}\n")
    except ValueError as e:
        print(f"{description}: Error → {e}\n")

# Edge Case: Negative Income
try:
    calculate_tax(-50000)
except ValueError as e:
    print(f"Negative Income Test: Error → {e}\n")
