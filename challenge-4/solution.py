def swap_numbers(a, b):
    return b, a


# Driver code to take input from user
if __name__ == "__main__":
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        a, b = swap_numbers(a, b)
        print(f"After swapping: First = {a}, Second = {b}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")
