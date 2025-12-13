def calculate_item_total(item_code, quantity, price):
    """
    Calculates total for an item.
    Applies 10% discount if item_code is PROMO10
    """
    if quantity <= 0 or price <= 0:
        raise ValueError("Quantity and price must be positive")

    total = quantity * price

    if item_code.upper() == "PROMO10":
        discount = total * 0.10
        total -= discount
        return total, discount

    return total, 0


if __name__ == "__main__":
    code = input("Enter Item Code: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    total, discount = calculate_item_total(code, qty, price)

    print("\n------ Bill ------")
    print(f"Item Code: {code}")
    print(f"Discount Applied: ₹{discount:.2f}")
    print(f"Final Item Total: ₹{total:.2f}")
