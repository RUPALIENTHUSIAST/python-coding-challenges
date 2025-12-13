def check_minimum_purchase(final_amount: float, minimum_amount: float = 500) -> bool:
    """
    Checks if the final amount meets the minimum purchase requirement.
    Returns True if purchase is valid, False otherwise.
    """
    if final_amount < 0:
        raise ValueError("Final amount cannot be negative.")
    
    if final_amount < minimum_amount:
        print(f"Minimum purchase amount of ₹{minimum_amount} not met. "
              f"Your total is ₹{final_amount:.2f}. Cannot generate invoice.")
        return False
    else:
        print(f"Purchase amount ₹{final_amount:.2f} meets the minimum requirement. Invoice can be generated.")
        return True


if __name__ == "__main__":
    try:
        final_amount = float(input("Enter Final Grand Total (₹): "))
        check_minimum_purchase(final_amount)
    except ValueError as e:
        print("Error:", e)
