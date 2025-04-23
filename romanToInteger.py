# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.



def romanToInt(s: str) -> int:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):  # Iterate from right to left
        curr_value = roman_values[char]
        if curr_value < prev_value:
            total -= curr_value  # Subtract for cases like IV, IX, etc.
        else:
            total += curr_value
        prev_value = curr_value  # Update previous value for next iteration

    return total

# Test cases
# print(romanToInt("III"))       # Output: 3
print(romanToInt("LVIII"))     # Output: 58
# print(romanToInt("MCMXCIV"))   # Output: 1994