def student_report(name, s1, s2, s3):
    if s1 < 0 or s2 < 0 or s3 < 0:
        raise ValueError("Scores cannot be negative")
    
    total = s1 + s2 + s3
    avg = total / 3

    if avg >= 60:
        grade = "1st Class"
    elif avg >= 50:
        grade = "2nd Class"
    elif avg >= 35:
        grade = "Pass Class"
    else:
        grade = "Fail"

    return total, avg, grade


if __name__ == "__main__":
    print("Enter Student Details:")
    name = input("Name: ")
    s1 = float(input("Subject 1 Score: "))
    s2 = float(input("Subject 2 Score: "))
    s3 = float(input("Subject 3 Score: "))

    total, avg, grade = student_report(name, s1, s2, s3)

    print("\n--- Report Card ---")
    print(f"Name: {name}")
    print(f"Total: {total}")
    print(f"Average: {avg:.2f}")
    print(f"Class: {grade}")
