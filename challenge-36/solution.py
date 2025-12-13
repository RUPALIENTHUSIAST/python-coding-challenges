def print_incremental_number_pattern(n: int):
    """
    Prints a number pattern for N rows.
    Each row contains numbers 1 to 5.

    Args:
        n (int): Number of rows (must be positive)
    """
    if not isinstance(n, int):
        raise TypeError("N must be an integer.")
    if n <= 0:
        raise ValueError("N must be a positive integer.")
    if n > 1000:
        raise ValueError("N is too large. Maximum allowed is 1000.")

    row = ''.join(str(i) for i in range(1, 6))
    for _ in range(n):
        print(row)


if __name__ == "__main__":
    try:
        n = int(input("Enter number of rows (N): "))
        print("\nNumber Pattern:")
        print_incremental_number_pattern(n)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
