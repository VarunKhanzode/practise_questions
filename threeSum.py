def threeSum(arr):
    target = arr[0]             # Step 1: First element is the target
    nums = arr[1:]              # Step 2: Slice rest of the array
    n = len(nums)               # Total numbers to consider

    for i in range(n):          # Step 3: Loop through the first number
        for j in range(i + 1, n):  # Step 4: Second number (after i)
            for k in range(j + 1, n):  # Step 5: Third number (after j)
                if nums[i] + nums[j] + nums[k] == target:  # Step 6: Check sum
                    return True    # Step 7: Found a match
    return False                   # Step 8: No match found

print(threeSum([10, 2, 3, 1, 5, 3, 1, 4, -4, -3, -2]))

class Solution:
    def threeSum(self, nums):
        n = len(nums) - 1
        if n+1 < 3:
            return []
        elif n+1 == 3:
            return [nums] if sum(nums) == 0 else []
        sorted_list = sorted(nums)
        i,j,k = 0,1,n
        check_repeated = {}
        result = []
        while (i != n-2):
            # print(i,j,k)
            if j==k:
                i += 1
                j = i + 1
                k = n
            if sorted_list[i] + sorted_list[j] + sorted_list[k] == 0:
                ans = tuple([sorted_list[i],sorted_list[j],sorted_list[k]])
                if ans not in check_repeated:
                    check_repeated[ans] = '*'
                    result.append(list(ans))
                j += 1
            elif sorted_list[i] + sorted_list[j] + sorted_list[k] < 0:
                j += 1
            else:
                k -= 1
        return result
            
            
print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([0,1,1]))
print(Solution().threeSum([0,0,0]))
print(Solution().threeSum([0,0,0,0]))