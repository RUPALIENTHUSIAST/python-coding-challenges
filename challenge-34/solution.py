def print_star_pattern(n):
    if n <= 0:
        raise ValueError("Number of rows must be positive.")
    for _ in range(n):
        print("*" * n)

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of rows (N): "))
        print("\nStar Pattern:")
        print_star_pattern(n)
    except ValueError as e:
        print(f"Error: {e}")
