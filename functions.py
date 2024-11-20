def largest_and_second_largest(arr)->tuple:
    if not arr:
        return None, None
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return largest, second_largest


def twoSum(arr, target) -> tuple[int, int]:
   
    l = 0;
    r = len(arr) - 1
    
    while arr[l] + arr[r] != target:
        if arr[l] + arr[r] < target:
            l += 1
        elif arr[l] + arr[r] > target:
            r -= 1
    
    return (l+1, r+1)