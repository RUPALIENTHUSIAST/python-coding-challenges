def apply_payment_surcharge(grand_total: float, payment_method: str) -> float:
    """
    Applies payment mode rules:
    - Cash: no surcharge
    - Credit Card: 2% surcharge
    Returns final payable amount
    """
    if grand_total < 0:
        raise ValueError("Grand total cannot be negative.")
    
    payment_method = payment_method.lower()
    
    if payment_method == "cash":
        surcharge = 0
    elif payment_method == "credit card":
        surcharge = 0.02 * grand_total
    else:
        raise ValueError("Invalid payment method. Choose 'Cash' or 'Credit Card'.")
    
    final_amount = grand_total + surcharge
    return surcharge, final_amount


if __name__ == "__main__":
    try:
        grand_total = float(input("Enter Grand Total (₹): "))
        payment_method = input("Enter Payment Method (Cash/Credit Card): ")

        surcharge, final_amount = apply_payment_surcharge(grand_total, payment_method)

        print("\n------ Payment Summary ------")
        print(f"Payment Method: {payment_method.title()}")
        print(f"Surcharge Amount: ₹{surcharge:.2f}")
        print(f"Final Payable Amount: ₹{final_amount:.2f}")
        print("-----------------------------")
    except ValueError as e:
        print("Error:", e)
