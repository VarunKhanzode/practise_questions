# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def longestCommonPrefix(strs: list[str]):
    if not strs:
        return ""
    for i in range(len(strs[0])): # Loop through each character of the first word in the list (strs[0]).
        char = strs[0][i] # i is the index of the character, and char is the actual character at that index.
        for word in strs[1:]:
            if i > len(word) or word[i] != char:
                return strs[0][:i]
    return strs[0]


print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
