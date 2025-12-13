def print_number_pattern(n: int):
    """
    Prints a number pattern for N rows.
    Each row i contains the number i repeated 5 times.

    Args:
        n (int): Number of rows (must be positive)
    """
    if not isinstance(n, int):
        raise TypeError("N must be an integer.")
    if n <= 0:
        raise ValueError("N must be a positive integer.")
    if n > 1000:
        raise ValueError("N is too large. Maximum allowed is 1000.")

    for i in range(1, n + 1):
        print(str(i) * 5)


if __name__ == "__main__":
    try:
        n = int(input("Enter number of rows (N): "))
        print("\nNumber Pattern:")
        print_number_pattern(n)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
