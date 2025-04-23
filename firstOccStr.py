# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


def solution(haystack: str, needle: str):
    needle_len = len(needle)
    if needle_len == 0:
        return 0
    for i in range(len(haystack) - needle_len + 1):
        if haystack[i:i+needle_len] == needle:
            return i
    return -1


import unittest


class TestSolution(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(solution("sadbutsad", "sad"), 0)  # "sad" found at index 0
        self.assertEqual(solution("leetcode", "leeto"), -1)  # "leeto" not found

    def test_edge_cases(self):
        self.assertEqual(solution("hello", "ll"), 2)  # "ll" found at index 2
        self.assertEqual(solution("aaaaa", "bba"), -1)  # "bba" not in "aaaaa"
        self.assertEqual(solution("mississippi", "issip"), 4)  # "issip" starts at 4
        self.assertEqual(solution("abc", "c"), 2)  # "c" found at index 2
        self.assertEqual(solution("abc", "d"), -1)  # "d" not found

    def test_single_character_cases(self):
        self.assertEqual(solution("a", "a"), 0)  # Single character match
        self.assertEqual(solution("a", "b"), -1)  # Single character mismatch
        self.assertEqual(solution("", "a"), -1)  # Empty haystack
        self.assertEqual(solution("a", ""), 0)  # Empty needle should return 0

    def test_large_input(self):
        self.assertEqual(solution("a" * 1000 + "b", "ab"), 999)  # "ab" at index 999

# Run the tests
if __name__ == "__main__":
    unittest.main()
