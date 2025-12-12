from soluution import student_report

print("Running Test Cases...\n")

# Positive Cases
print("Positive Test Cases:")
print("Case 1 →", student_report("A", 70, 80, 60))   # 1st Class
print("Case 2 →", student_report("B", 55, 52, 50))   # 2nd Class
print("Case 3 →", student_report("C", 35, 40, 38))   # Pass Class
print("Case 4 →", student_report("D", 20, 30, 10))   # Fail

# Edge Cases
print("\nEdge Cases:")
print("Edge Case 1 →", student_report("E", 60, 60, 60))  # Exactly 60 → 1st Class
print("Edge Case 2 →", student_report("F", 50, 50, 50))  # Exactly 50 → 2nd Class
print("Edge Case 3 →", student_report("G", 35, 35, 35))  # Exactly 35 → Pass

# Error Case
print("\nError Test Case:")
try:
    student_report("H", 70, -5, 60)
except ValueError as e:
    print("Negative score → Exception:", e)
