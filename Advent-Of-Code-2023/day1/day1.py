"""
Day 1 Stoof
"""


def convert_calibration(calibration_value: str) -> str:
    _digits = {
        "zero":   "0",
        "one":    "1",
        "two":    "2",
        "three":  "3",
        "four":   "4",
        "five":   "5",
        "six":    "6",
        "seven":  "7",
        "eight":  "8",
        "nine":   "9",
    }
    output = ""
    i = 0
    while i < len(calibration_value):
        for word, digit in _digits.items():
            if calibration_value[i:].startswith(word):
                output += digit
                i += len(word)
                continue
        if i >= len(calibration_value):
            break
        output += calibration_value[i]
        i += 1
    return output


def get_digits(calibration_value: str) -> int:
    digits = [c for c in calibration_value if c.isdigit()]
    if len(digits) == 1:
        [digit] = digits
        return int(f"{digit}{digit}")
    try:
        return int(f"{digits[0]}{digits[-1]}")
    except Exception:
        breakpoint()


def main():
    # Part 1
    total = 0
    print("Test data for part1:")
    with open("test1.txt", "r") as handle:
        for line in handle:
            tmp = get_digits(line)
            total += tmp
            print(f"  {line.strip()}: {total}")
    print(f"  {total}")

    print("Real part1:")
    total = 0
    with open("input.txt", "r") as handle:
        for line in handle:
            total += get_digits(line)
    print(f"  {total}")

    # Part 2
    total = 0
    print("Test for part2:")
    with open("test2.txt", "r") as handle:
        for line in handle:
            tmp = get_digits(convert_calibration(line.strip()))
            print(f"  {line.strip()} : {tmp}")
            total += tmp
    print(f"  {total}")

    total = 0
    print("Real part2:")
    with open("input.txt", "r") as handle:
        for line in handle:
            tmp = get_digits(convert_calibration(line.strip()))
            total += tmp
    print(f"  {total}")


if __name__ == "__main__":
    main()
