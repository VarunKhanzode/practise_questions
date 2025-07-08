# Given the list numbers, for each numbers find out how many numbers in the list are smaller than it. 
numbers = [9,2,3,3,4,6]
# Output: [5,0,1,1,3,4]

def smaller_numbers_than_current(nums):
    sorted_nums = sorted(nums)
    rank = {}
    for i, num in enumerate(sorted_nums):
        if num not in rank:
            rank[num] = i
    return [rank[num] for num in nums]

numbers = [9, 2, 3, 3, 4, 6]
print(smaller_numbers_than_current(numbers))