# Code tự nghĩ
hello = (input())
num = hello[::-1]
print(num)






























def reverse_integer(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Check if the number is negative
    is_negative = num_str[0] == '-'
    
    # Reverse the digits (excluding the sign if present)
    reversed_str = num_str[::-1] if not is_negative else '-' + num_str[:0:-1]
    
    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)
    
    # Check if the reversed number exceeds the 31-bit signed integer range
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0  # Return 0 if the reversed number is out of range
    
    return reversed_num

# Example usage
num = input()
reversed_num = reverse_integer(num)
print(reversed_num)  # Output: 54321
