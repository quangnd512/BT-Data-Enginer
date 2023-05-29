def reverse(x):
    # Check if the number is negative
    is_negative = x < 0

    # Convert the number to positive for reversing the digits
    x = abs(x)

    # Reverse the digits by converting the number to a string and reversing it
    reversed_str = str(x)[::-1]

    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)

    # Check if the reversed number exceeds the 32-bit signed integer range
    if reversed_num > 2**31 - 1:
        return 0

    # Return the reversed number with the appropriate sign
    return -reversed_num if is_negative else reversed_num

# if number bigger than 32-bit signed integer will be 0
print(reverse(-210))