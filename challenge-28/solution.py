def calculate_final_total(grand_total, total_quantity, is_member):
    """
    Apply discounts:
    1. 10% discount if grand total > 10,000
    2. Additional 5% discount if total quantity > 20
    3. Additional 2% discount if customer is a member
    """

    if grand_total < 0 or total_quantity < 0:
        raise ValueError("Total and quantity cannot be negative")

    original_total = grand_total

    # Discount 1: Grand total > 10,000
    if grand_total > 10000:
        grand_total *= 0.90  # 10% discount

    # Discount 2: Quantity > 20
    if total_quantity > 20:
        grand_total *= 0.95  # extra 5% discount

    # Discount 3: Membership
    if is_member:
        grand_total *= 0.98  # extra 2% discount

    return round(original_total, 2), round(grand_total, 2)


if __name__ == "__main__":
    total = float(input("Enter Grand Total (₹): "))
    quantity = int(input("Enter Total Quantity: "))
    member = input("Are you a member? (y/n): ").lower() == "y"

    original, final = calculate_final_total(total, quantity, member)

    print("\n------ Final Bill ------")
    print(f"Original Total: ₹{original}")
    print(f"Final Payable Amount: ₹{final}")
