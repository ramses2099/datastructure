class Node:
    def __init__(self, data):
        self.data = data
        self.next_ref = None
        self.prev_ref = None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None    
    
    def print_forward(self):
        if self.is_empty() == True: 
            print("Linked list is empty")
            return
        
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_ref
        print("")  
        
    def print_backward(self):
        if self.is_empty() == True: 
            print("Linked list is empty")
            return
        
        current_node = self.head
        while current_node.next_ref is not None:
            current_node = current_node.next_ref
        while current_node is not None:
            print(current_node.data, end=" <- ")
            current_node = current_node.prev_ref
        print("")    
    
    
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node            
        else:
            new_node.next_ref = self.head
            self.head.prev_ref = new_node
            self.head = new_node
    