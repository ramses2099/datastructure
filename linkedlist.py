class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def printLinkedList(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("")
        
    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def add_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = new_node
        
    def add_after(self, data, node):
        new_node = Node(data)
        
        if self.head is None:
            print("Linked List is empty")
            return
        
        current_node = self.head
        while current_node is not None:
            if current_node.data == node:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        
    def add_before(self, data, node):
        if self.head is None:
            print("Linked List is empty")
            return
        
        if self.head.data == node:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == node:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        
    def insert_empty_list(self, data):
        if self.head is not None:
            print("Linked List is not empty")
            return
        
        self.head = Node(data)
               
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
            return
        self.head = self.head.next
        
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        
        current_node.next = None
           
    def delete_by_value(self, value):
        if self.head is None:
            print("Linked List is empty")
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
            
    