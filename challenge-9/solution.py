def is_leap_year(year):
    if year < 0:
        raise ValueError("Year cannot be negative")

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


if __name__ == "__main__":
    year = int(input("Enter a year: "))
    result = is_leap_year(year)
    print(f"{year} is a leap year? {result}")
