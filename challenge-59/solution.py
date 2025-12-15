def element_exists(matrix, target):
    if not matrix or not isinstance(matrix, list):
        raise ValueError("Invalid 2D array")

    for row in matrix:
        for value in row:
            if value == target:
                return True
    return False


if __name__ == "__main__":
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        if rows <= 0 or cols <= 0:
            raise ValueError("Rows and columns must be positive")

        matrix = []
        print("Enter elements row-wise:")
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(int(input(f"Element [{i}][{j}]: ")))
            matrix.append(row)

        target = int(input("Enter element to search: "))

        if element_exists(matrix, target):
            print("Element exists in the 2D array")
        else:
            print("Element does NOT exist in the 2D array")

    except Exception as e:
        print("Error:", e)
