
'''Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2'''


def single_digit_sum(n: int) -> int:
    # Convert n to a string, then to a list of characters
    digits = list(str(n))
    # Convert each character back to an integer and sum them
    total = sum(int(d) for d in digits)
    # If the sum has more than one digit, repeat the process
    while total >= 10:
        digits = list(str(total))
        total = sum(int(d) for d in digits)
    return total


print(single_digit_sum(16))  # 7
print(single_digit_sum(942))  # 6
print(single_digit_sum(132189))  # 6
print(single_digit_sum(493193))  # 2