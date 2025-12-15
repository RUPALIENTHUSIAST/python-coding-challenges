def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []

    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        transpose.append(row)

    return transpose


def read_matrix(m, n):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(int(input(f"Enter element [{i}][{j}]: ")))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    try:
        m = int(input("Enter number of rows (M): "))
        n = int(input("Enter number of columns (N): "))

        if m <= 0 or n <= 0:
            raise ValueError("Rows and columns must be positive")

        matrix = read_matrix(m, n)

        print("\nOriginal Matrix:")
        print_matrix(matrix)

        t = transpose_matrix(matrix)

        print("\nTranspose Matrix:")
        print_matrix(t)

    except ValueError as e:
        print("Error:", e)
