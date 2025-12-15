def sum_2d_array(matrix):
    if not matrix or not all(isinstance(row, list) for row in matrix):
        raise ValueError("Invalid 2D array")

    total = 0
    for row in matrix:
        for val in row:
            if not isinstance(val, (int, float)):
                raise ValueError("Array elements must be numbers")
            total += val
    return total


if __name__ == "__main__":
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        if rows <= 0 or cols <= 0:
            raise ValueError("Rows and columns must be > 0")

        matrix = []
        for i in range(rows):
            row = []
            print(f"Enter elements for row {i + 1}:")
            for j in range(cols):
                row.append(int(input(f"Element [{i}][{j}]: ")))
            matrix.append(row)

        result = sum_2d_array(matrix)

        print("\n2D Array:")
        for r in matrix:
            print(r)

        print(f"\nSum of all elements: {result}")

    except Exception as e:
        print("Error:", e)
