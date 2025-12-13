def separate_whole_fraction(value: float):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a number")

    whole_part = int(value)
    fractional_part = abs(value - whole_part)

    return whole_part, fractional_part


if __name__ == "__main__":
    try:
        num = float(input("Enter a number: "))
        whole, fraction = separate_whole_fraction(num)

        print("\n--- Result ---")
        print(f"Whole Part: {whole}")
        print(f"Fractional Part: {fraction}")
    except Exception as e:
        print("Error:", e)
