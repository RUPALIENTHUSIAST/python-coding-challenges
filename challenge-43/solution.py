# solution.py

def number_to_words(num: int) -> str:
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")

    if num < 0:
        raise ValueError("Number must be non-negative")

    digit_words = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    # Special case: number is 0
    if num == 0:
        return digit_words[0]

    words = []

    while num > 0:
        digit = num % 10
        words.append(digit_words[digit])
        num //= 10

    # reverse because digits were extracted from end
    return " ".join(reversed(words))


if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        print(number_to_words(n))
    except Exception as e:
        print("Error:", e)
