import os
from typing import List, Dict, Set, Tuple
from doublelinkedlist import DoubleLinkedList


def main():
    os.system("cls")
    dll = DoubleLinkedList()
    [dll.add_begin(d * 2) for d in range(0, 10)]
    dll.print_forward()
    dll.print_backward()

if __name__ == "__main__":
    main()