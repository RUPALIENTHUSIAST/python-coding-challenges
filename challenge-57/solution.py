def create_2d_array(rows, cols, elements):
    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and columns must be positive")

    if len(elements) != rows * cols:
        raise ValueError("Number of elements does not match matrix size")

    matrix = []
    idx = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(elements[idx])
            idx += 1
        matrix.append(row)

    return matrix


def display_row_wise(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        elements = []
        for i in range(rows * cols):
            elements.append(int(input(f"Enter element {i + 1}: ")))

        matrix = create_2d_array(rows, cols, elements)

        print("\n2D Array (Row-wise):")
        display_row_wise(matrix)

    except Exception as e:
        print("Error:", e)
