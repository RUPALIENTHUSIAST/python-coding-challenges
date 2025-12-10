def calculate_discount(total_amount, discount_percent):
    if total_amount < 0 or discount_percent < 0:
        raise ValueError("Total amount and discount percent must be non-negative")
    if discount_percent > 100:
        raise ValueError("Discount percent cannot exceed 100")
    
    discount_value = (total_amount * discount_percent) / 100
    discounted_price = total_amount - discount_value
    return discounted_price
# code to take input
if __name__ == "__main__":
    try:
        total_amount = float(input("Enter total amount: "))
        discount_percent = float(input("Enter discount percent: "))
        final_price = calculate_discount(total_amount, discount_percent)
        print(f"Discounted Price: {final_price}")
    except ValueError as e:
        print(f"Error: {e}")
