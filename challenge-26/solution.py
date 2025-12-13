def calculate_item_total(quantity, price):
    if quantity <= 0 or price < 0:
        raise ValueError("Quantity must be > 0 and price cannot be negative")
    return quantity * price


if __name__ == "__main__":
    print("---- Retail Shopping App ----")

    grand_total = 0
    n = int(input("Enter number of items: "))

    for i in range(1, n + 1):
        print(f"\nItem {i}")
        code = input("Item Code: ")
        desc = input("Description: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price per unit: "))

        item_total = calculate_item_total(quantity, price)
        grand_total += item_total

        print(f"Total for {desc}: ₹{item_total:.2f}")

    print("\n-----------------------------")
    print(f"Grand Total: ₹{grand_total:.2f}")
