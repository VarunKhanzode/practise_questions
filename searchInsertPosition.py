# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4


class Solution:
    def searchInsert(self, nums: list[int], target: int):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

sol = Solution()

print(sol.searchInsert([1, 3, 5, 6], 5))  # Output: 2
print(sol.searchInsert([1, 3, 5, 6], 2))  # Output: 1
print(sol.searchInsert([1, 3, 5, 6], 7))  # Output: 4
print(sol.searchInsert([1, 3, 5, 6], 0))  # Output: 0