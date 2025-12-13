def generate_selected_squares(n):
    """
    Generate the series: 1, 4, 9, 25, 36, 49, 81 ... up to N terms
    (skipping 16, 64 based on pattern)
    """
    if n <= 0:
        raise ValueError("N must be positive.")

    series = []
    num = 1

    while len(series) < n:
        square = num * num
        # Skip squares where num is 4, 8, 12 ... (pattern observation)
        if num % 4 != 0:
            series.append(square)
        num += 1

    return series

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of terms (N): "))
        result = generate_selected_squares(n)
        print("Series up to", n, "terms:")
        print(result)
    except ValueError as e:
        print("Error:", e)
