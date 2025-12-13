def calculate_loyalty_points(grand_total):
    if grand_total < 0:
        raise ValueError("Grand total cannot be negative.")
    points = int(grand_total // 100)
    return points

if __name__ == "__main__":
    try:
        grand_total = float(input("Enter Final Grand Total (₹): "))
        points = calculate_loyalty_points(grand_total)
        print(f"\n------ Loyalty Points ------")
        print(f"Grand Total: ₹{grand_total:,.2f}")
        print(f"Loyalty Points Earned: {points} point(s)")
    except ValueError as e:
        print(f"Error: {e}")
