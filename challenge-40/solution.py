def print_fibonacci_pattern(n: int) -> None:
    if not isinstance(n, int):
        raise TypeError("N must be an integer")

    if n <= 0:
        raise ValueError("N must be greater than 0")

    a, b = 1, 1  # First two Fibonacci numbers

    for row in range(1, n + 1):
        current_row = []
        for _ in range(row):
            current_row.append(str(a))
            a, b = b, a + b
        print(" ".join(current_row))


if __name__ == "__main__":
    try:
        n = int(input("Enter number of rows (N): "))
        print_fibonacci_pattern(n)
    except Exception as e:
        print("Error:", e)
