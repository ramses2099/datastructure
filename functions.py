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


def maxSumFirstKElement(arr, K) -> int:
    """The sum of the first {K} in an array or n elements

    Args:
        arr (List): list of element
        K (int): K element

    Returns:
        res int: sum of the first {K} element
    """
    n = len(arr)
    res = 0
    
    for i in range(K):
        res += arr[i]
    
    curr_sum = res
    for i in range(K,n):
        curr_sum += arr[i] - arr[i-K]
        res = max(res, curr_sum)
     
    return res


def rolling_hash_search(text, pattern):
    base = 256
    mod = 101
    
    n, m = len(text), len(pattern)
    if m > n:
        return -1
    
    hash_pattern = 0
    hash_window = 0
    for i in range(m):
        hash_pattern = (hash_pattern * base + ord(pattern[i])) % mod
        hash_window = (hash_window * base + ord(text[i])) % mod
        
    for i in range(n - m + 1):
        if hash_pattern == hash_window:
            if text[i:i+m] == pattern:
                return i
        
        if i < n - m:
            hash_window = (hash_window - ord(text[i]) * pow(base,m-1, mod)) % mod
            hash_window = (hash_window * base + ord(text[i+m])) % mod
            hash_window = (hash_window + mod) % mod
    
    return -1
