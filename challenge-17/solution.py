def print_series(n):
    if n <= 0:
        raise ValueError("N must be a positive number")

    for i in range(1, n + 1):
        print(i, end=" ")


if __name__ == "__main__":
    try:
        n = int(input("Enter the value of N: "))
        print_series(n)
    except ValueError as e:
        print("Error:", e)
