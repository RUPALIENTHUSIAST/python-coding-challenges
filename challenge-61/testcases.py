def test_matrix_multiplication_possible():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    expected = [
        [19, 22],
        [43, 50]
    ]

    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]

    assert result == expected
    print("Test Case 1 Passed")


def test_matrix_multiplication_not_possible():
    r1, c1 = 3, 4
    r2, c2 = 6, 7
    assert c1 != r2
    print("Test Case 2 Passed (Invalid dimensions caught early)")


if __name__ == "__main__":
    test_matrix_multiplication_possible()
    test_matrix_multiplication_not_possible()
