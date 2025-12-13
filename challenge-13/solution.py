def calculate_tax(taxable_income):
    if taxable_income < 0:
        raise ValueError("Taxable income cannot be negative.")

    tax = 0
    remaining_income = taxable_income

    # Tax slabs
    slabs = [
        (300000, 0.00),   # 0 - 3,00,000: 0%
        (300000, 0.05),   # 3,00,001 - 6,00,000: 5%
        (300000, 0.10),   # 6,00,001 - 9,00,000: 10%
        (300000, 0.15),   # 9,00,001 - 12,00,000: 15%
        (300000, 0.20),   # 12,00,001 - 15,00,000: 20%
        (float('inf'), 0.30)  # Above 15,00,000: 30%
    ]

    # Apply Section 87A rebate
    if taxable_income <= 700000:
        tax = 0
    else:
        for slab_amount, rate in slabs:
            if remaining_income <= 0:
                break
            income_in_slab = min(remaining_income, slab_amount)
            tax += income_in_slab * rate
            remaining_income -= income_in_slab

    cess = tax * 0.04  # 4% Health & Education Cess
    total_tax = tax + cess

    return tax, cess, total_tax

# Main program
if __name__ == "__main__":
    try:
        taxable_income = float(input("Enter taxable income (₹): "))

        tax, cess, total_tax = calculate_tax(taxable_income)

        print("\n------ Tax Breakdown ------")
        print(f"Taxable Income: ₹{taxable_income:,.2f}")
        print(f"Tax (before cess): ₹{tax:,.2f}")
        print(f"Health & Education Cess (4%): ₹{cess:,.2f}")
        print(f"Total Tax Payable: ₹{total_tax:,.2f}")
        print("----------------------------")

    except ValueError as e:
        print(f"Error: {e}")
