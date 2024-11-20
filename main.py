import os
from typing import List, Dict, Set, Tuple
from array import array 
from functions import largest_and_second_largest, twoSum

def main():
    os.system("cls")
    arr = [2,7,11,15]
    target = 9
    output = tuple([1,2])
    
    res = twoSum(arr, target)
    assert res == output, "Incorrect output"
    print(f"result : {res}")
    
    # start = 0
    # end = len(arr) - 1
    # print(f"result : {end}")
    
    # while arr[start] + arr[end] != target:
    #     if arr[start] + arr[end] < target:
    #         start += 1
    #     elif arr[start] + arr[end] > target:
    #         end -= 1
    
    # print(f"sum : {arr[start] + arr[end]} index 1: {start+1} index 2: {end+1}")
    
    
   
if __name__ == "__main__":
    main()