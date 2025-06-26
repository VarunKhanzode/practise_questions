# Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

def add_binary(a, b):
    i, j = len(a) - 1, len(b) - 1
    result = []
    carry = 0

    while i >= 0 or j >= 0 or carry:
        num_a = int(a[i]) if i >= 0 else 0
        num_b = int(b[j]) if j >= 0 else 0
        ans = num_a + num_b + carry
        result.append(str(ans % 2))
        carry = ans // 2

        i -= 1
        j -= 1
    return ''.join(reversed(result))

print(add_binary('11', '1'))
print(add_binary('1010', '1011'))