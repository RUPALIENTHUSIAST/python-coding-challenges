def generate_series(n):
    
    if n <= 0:
        raise ValueError("N must be positive.")

    series = []
    current = 1
    increment = 1

    for _ in range(n):
        series.append(current)
        current += increment
        increment += 1

    return series

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of terms (N): "))
        result = generate_series(n)
        print("Series up to", n, "terms:")
        print(result)
    except ValueError as e:
        print("Error:", e)
