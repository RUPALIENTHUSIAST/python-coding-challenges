def fibonacci_series(n):
    if n <= 0:
        raise ValueError("N must be a positive integer")

    series = []

    a, b = 1, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series


if __name__ == "__main__":
    try:
        n = int(input("Enter number of terms (N): "))
        result = fibonacci_series(n)
        print("Series:")
        print(result)
    except ValueError as e:
        print("Error:", e)
