import os
from typing import List, Dict, Set, Tuple
from array import array 
from functions import largest_and_second_largest, twoSum

def main():
    os.system("cls")
    arr = [1,7,6,10,23,3,1,0,20]
    K = 4
    output = list([7,6,10,23])
    output_sum = 46
    n = len(arr)
    
    res = 0
    
    for i in range(K):
        res += arr[i]
        
    print(f"The sum of the first {K} elements is: {res}")
    
    curr_sum = res
    for i in range(K,n):
        curr_sum += arr[i] - arr[i-K]
        res = max(res, curr_sum)
     
    print(f"res = {res}")
   
if __name__ == "__main__":
    main()