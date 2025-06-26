# find two nums in the sorted array whose average is the target

arr = [1,3,5,7,9,11,13,15]
avg = 8

def solution(arr, avg):
    target = avg * 2
    i, j = 0, len(arr) - 1

    while i <= j:
        if arr[i] + arr[j] == target:
            return True
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j -= 1
    return False

print(solution(arr, avg))