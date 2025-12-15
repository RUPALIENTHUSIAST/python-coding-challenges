def read_matrix(rows, cols, name):
    matrix = []
    print(f"Enter elements for {name}:")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"{name}[{i}][{j}]: ")))
        matrix.append(row)
    return matrix


def multiply_matrices(A, B, r1, c1, c2):
    result = [[0] * c2 for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    return result


def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    try:
        r1 = int(input("Enter rows of Matrix A: "))
        c1 = int(input("Enter columns of Matrix A: "))
        r2 = int(input("Enter rows of Matrix B: "))
        c2 = int(input("Enter columns of Matrix B: "))

        # EARLY VALIDATION
        if c1 != r2:
            print("Error: Matrix multiplication not possible")
            exit()

        A = read_matrix(r1, c1, "A")
        B = read_matrix(r2, c2, "B")

        result = multiply_matrices(A, B, r1, c1, c2)

        print("Resultant Matrix:")
        display_matrix(result)

    except ValueError:
        print("Error: Invalid input")
