# testcases.py

from solution import number_to_words

print("Running Test Cases...\n")

# Positive cases
print(number_to_words(270176))   # Two Seven Zero One Seven Six
print(number_to_words(0))        # Zero
print(number_to_words(905))      # Nine Zero Five

# Edge case
print(number_to_words(10))       # One Zero

# Negative case
try:
    number_to_words(-123)
except ValueError as e:
    print("Caught Error:", e)

# Invalid type
try:
    number_to_words("123")
except TypeError as e:
    print("Caught Error:", e)
