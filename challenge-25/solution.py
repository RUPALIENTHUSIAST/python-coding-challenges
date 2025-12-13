def calculate_item_total(code, description, quantity, price):
    if not code or not description:
        raise ValueError("Item code and description cannot be empty")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    if price <= 0:
        raise ValueError("Price must be greater than zero")

    total = quantity * price

    return {
        "code": code,
        "description": description,
        "quantity": quantity,
        "price": price,
        "total": total
    }


if __name__ == "__main__":
    print("Enter Item Details")

    code = input("Item Code: ")
    description = input("Description: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per item: "))

    item = calculate_item_total(code, description, quantity, price)

    print("\n----- Item Invoice -----")
    print(f"Code: {item['code']}")
    print(f"Description: {item['description']}")
    print(f"Quantity: {item['quantity']}")
    print(f"Price: ₹{item['price']:.2f}")
    print(f"Total Cost: ₹{item['total']:.2f}")
