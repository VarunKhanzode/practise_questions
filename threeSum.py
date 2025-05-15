


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