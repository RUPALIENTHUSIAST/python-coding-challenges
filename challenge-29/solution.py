def calculate_tax(grand_total):
    if grand_total < 0:
        raise ValueError("Grand total cannot be negative")

    if grand_total < 5000:
        tax_rate = 0.05
    elif grand_total <= 20000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15

    tax_amount = grand_total * tax_rate
    final_amount = grand_total + tax_amount

    return tax_rate, tax_amount, final_amount


if __name__ == "__main__":
    try:
        grand_total = float(input("Enter Grand Total (₹): "))

        rate, tax, final = calculate_tax(grand_total)

        print("\n------ Tax Details ------")
        print(f"Grand Total: ₹{grand_total:.2f}")
        print(f"Tax Rate Applied: {int(rate*100)}%")
        print(f"Tax Amount: ₹{tax:.2f}")
        print(f"Final Amount Payable: ₹{final:.2f}")

    except ValueError as e:
        print("Error:", e)
