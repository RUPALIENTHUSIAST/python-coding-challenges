from solution import print_star_pattern
import io
import sys

def capture_output(func, *args):
    """Capture the printed output of a function."""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    func(*args)
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()

# Positive Test Case
print("Positive Test Case (N=3):")
output = capture_output(print_star_pattern, 3)
print(output)

# Edge Case: N=1
print("Edge Case (N=1):")
output = capture_output(print_star_pattern, 1)
print(output)

# Invalid Case: N=0 (should raise ValueError)
print("Invalid Case (N=0):")
try:
    print_star_pattern(0)
except ValueError as e:
    print("Caught Error:", e)

# Larger N
print("Larger N=5:")
output = capture_output(print_star_pattern, 5)
print(output)
