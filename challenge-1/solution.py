def sum_and_average(a, b):
    total = a + b
    average = total / 2
    return total, average


if __name__ == "__main__":
    # Input from user
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    total, avg = sum_and_average(x, y)
    print("Sum:", total)
    print("Average:", avg)
