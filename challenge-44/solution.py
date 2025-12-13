def generate_series(n: int):
    if not isinstance(n, int):
        raise TypeError("N must be an integer")
    if n <= 0:
        raise ValueError("N must be greater than 0")

    series = []
    for i in range(1, n + 1):
        val = 4 * i - 3
        if i % 2 == 0:
            val = -val
        series.append(val)

    return series


if __name__ == "__main__":
    try:
        n = int(input("Enter number of terms (N): "))
        result = generate_series(n)
        print("Series:")
        print(result)
    except Exception as e:
        print("Error:", e)
