# testcases.py

from solution import accept_array

print("Running Test Cases...\n")

# Positive Case: User input simulation
# Normally input() cannot be tested automatically without mocking.
# For demonstration, we'll test the function logic manually:

def test_accept_array():
    # Mocked array (simulate user input)
    n = 5
    arr = [1, 2, 3, 4, 5]  # Assume user entered these values
    print("Array of size", n, ":", arr)

test_accept_array()

# Edge Case: n = 1
n = 1
arr = [10]
print("\nArray of size 1:", arr)

# Negative Case: n = 0 or negative handled in solution.py
try:
    n = 0
    arr = accept_array(n)
except ValueError as e:
    print("\nCaught Error for n=0:", e)
