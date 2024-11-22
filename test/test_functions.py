import pytest
from functions import *

def test_maxSumFirstKElement():
    arr = [1,7,6,10,23,3,1,0,20]
    K = 4
    output_sum = 46
    
    res = maxSumFirstKElement(arr, K)
    assert res == output_sum
    
    
def test_rolling_hash():
    text = "abracadabra"
    pattern = "cada"
    output = 4
    
    index = rolling_hash_search(text, pattern)
    
    assert index == output