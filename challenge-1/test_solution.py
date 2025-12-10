from solution import sum_and_average

def run_tests():
    print("Running Test Cases...\n")

    # Positive test cases
    print("Positive Cases:")
    print("Input: 10, 20  →", sum_and_average(10, 20))    
    print("Input: 5.5, 4.5 →", sum_and_average(5.5, 4.5)) 

    # Negative test cases
    print("\nNegative Cases:")
    print("Input: -5, -10  →", sum_and_average(-5, -10))   # Expected: (-15, -7.5)
    print("Input: -3, 7    →", sum_and_average(-3, 7))     # Expected: (4, 2)

    # Edge cases
    print("\nEdge Cases:")
    print("Input: 0, 0        →", sum_and_average(0, 0))    # Expected: (0, 0)
    print("Input: 1e9, 1e9    →", sum_and_average(1e9, 1e9)) # Very large numbers

run_tests()
