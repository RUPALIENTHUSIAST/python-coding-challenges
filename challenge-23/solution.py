def generate_series(n):
    if n <= 0:
        raise ValueError("N must be a positive integer")

    series = [1]
    diffs = [4, 4, 4, 8, 4, 4, 8]  # correct pattern
    i = 0

    while len(series) < n:
        series.append(series[-1] + diffs[i % len(diffs)])
        i += 1

    return series


if __name__ == "__main__":
    n = int(input("Enter number of terms (N): "))
    print("Series:")
    print(generate_series(n))
