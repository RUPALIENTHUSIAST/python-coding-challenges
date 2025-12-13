def apply_discounts(grand_total, total_quantity):
    if grand_total < 0 or total_quantity < 0:
        raise ValueError("Total and quantity must be non-negative")

    discount_details = []
    final_total = grand_total

    # Rule 1: 10% discount
    if final_total > 10000:
        discount = final_total * 0.10
        final_total -= discount
        discount_details.append(f"10% discount applied: ₹{discount:.2f}")

    # Rule 2: Additional 5% quantity discount
    if total_quantity > 20:
        discount = final_total * 0.05
        final_total -= discount
        discount_details.append(f"5% quantity discount applied: ₹{discount:.2f}")

    return final_total, discount_details


if __name__ == "__main__":
    try:
        grand_total = float(input("Enter Grand Total (₹): "))
        total_quantity = int(input("Enter Total Quantity: "))

        final_amount, discounts = apply_discounts(grand_total, total_quantity)

        print("\n------ Discount Summary ------")
        for d in discounts:
            print(d)

        print(f"\nFinal Payable Amount: ₹{final_amount:.2f}")

    except ValueError as e:
        print("Error:", e)
