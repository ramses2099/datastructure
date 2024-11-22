import os
from typing import List, Dict, Set, Tuple
from array import array 
from functions import rolling_hash_search


def main():
    os.system("cls")
    text = "abracadabra"
    pattern = "cada"
    
    index = rolling_hash_search(text, pattern)
    if index != -1:
        print(f"Pattern found at index: {index}")
    else:
        print("Pattern not found in the text.")
        
    
        
if __name__ == "__main__":
    main()