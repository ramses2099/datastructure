# datastructure
Data Structure with python

# data structures:
- Way to store and organize the data so that it can be accessed efficiently.

# Build-in
- List
- Tuple
- Set
- Dictionary

# User defined
- Stack
- Queue
- Linked list
- Tree
- Graph

# List
- Lists may be constructed in several ways:

1.Using a pair of square brackets to denote the empty list: []

1.Using square brackets, separating items with commas: [a], [a, b, c]

1.Using a list comprehension: [x for x in iterable]

1.Using the type constructor: list() or list(iterable)

- You can access list elements using indexing
- Lists are Dynamic

# Tuples
- Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). 

- Tuples may be constructed in a number of ways:

1.Using a pair of parentheses to denote the empty tuple: ()

1.Using a trailing comma for a singleton tuple: a, or (a,)

1.Separating items with commas: a, b, c or (a, b, c)

1.Using the tuple() built-in: tuple() or tuple(iterable)

# Stack

- Stacks are Last in first out (LIFO) or First in last out (FIFO)

- Operations on the stack
1. Push
1. Pop
1. Peek or Top
1. isEmpty

- Implementation of stack with list or modules
- push ---> append
- pop ---> pop

``` stack = []
    stack.append(10)
    stack.append(20)
    stack.append(30)
    stack
```
- Implementation using the module collection
- collections module has the class deque

- Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

- Implementation using the module queue
- queue module has the class lifoqueue
- Constructor for a LIFO queue. maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will block once this size has been reached, until queue items are consumed. If maxsize is less than or equal to zero, the queue size is infinite.
```
from queue import LifoQueue

# stack 
stack = LifoQueue()

stack.put(10)
stack.put(20)
stack.put(30)
    
print(f"Stack: {stack}")
print(f"Pop: {stack.get()}")
```
# Queue
- Constructor for a FIFO queue. maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will block once this size has been reached, until queue items are consumed. If maxsize is less than or equal to zero, the queue size is infinite.

- enqueue -> add element to the queue
- dequeue -> remove element to the queue

- Implement Queue
- enqueue: append method
- dequeue: pop method: list.pop(0)

# Linked list
-  A linked list is a type of linear data structure similar to arrays. It is a collection of nodes that are linked with each other.

- Node: elements of linked list
- Head: is the first node in the linked list
- Tail: is the last node in the linked list
- Data: is the data

```
from queuetest import QueueTest

# stack 
stack = QueueTest()
stack.enqueue(10)
stack.enqueue(20)
stack.enqueue(30)
    
stack.print()
print(f"dequeue {stack.dequeue()}")
stack.print()

```

- Advantages of linked list
- Dynamic data structure
- Insertion a deletion is easy
- You can implement stack, queue and graph
- Represent and manipulate polynomials

- Disadvantages of linked list
- Need extra memory
- Random access no possible

# Types linked list
- Single linked list
- Double linked list
- Circular linked list


# Single linked list
- add
  - begin
  - end
  - in between
- traversal
    - Start with head if head is no NULL access the info.
- delete

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

 ll = LinkedList()
    ll.add_begin(10)
    ll.add_begin(20)
    ll.add_begin(30)
    ll.add_begin(40)
    ll.add_end(5)
    print("Original Linked List:")
    ll.printLinkedList()
    ll.add_after(0,5)
    ll.printLinkedList()
    ll.add_begin(50)
    ll.printLinkedList()
    ll.delete_begin()
    ll.printLinkedList()
    ll.delete_end()
    ll.printLinkedList()
    ll.delete_by_value(10)
    ll.printLinkedList()       
```

# Double linked list

- Operations on double linked list
- Insert
- Delete
- Traversal

```
dll = DoubleLinkedList()
    [dll.add_begin(d * 2) for d in range(0, 10)]
    dll.print_forward()
    dll.print_backward()
    dll.add_end(-1)
    dll.print_forward()
    dll.print_backward()
    print(f"count node in list: %s" % dll.count())
```
 
# Non-Linear data structure
- Tree
- Graph

# Binary Search Tree
```
bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("In-order Traversal:", bst.inorder_traversal())  # Sorted order
    print("Pre-order Traversal:", bst.preorder_traversal())
    print("Post-order Traversal:", bst.postorder_traversal())

    print("Search 40:", bst.search(40))  # True
    print("Search 90:", bst.search(90))  # False

    bst.delete(50)
    print("In-order Traversal after deleting 50:", bst.inorder_traversal())
    ```