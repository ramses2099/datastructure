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
    
    def count(self):
        count = 0
        
        if self.is_empty():
            return 0
        
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next_ref
        return count
    
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
    
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node            
        else:
            current_node = self.head
            while current_node.next_ref is not None:
                current_node = current_node.next_ref
            current_node.next_ref = new_node
            new_node.prev_ref = current_node
            
    def add_after(self, data, prev_node_data):
        new_node = Node(data)
        if self.head is None:
            print("Linked list is empty")
            return
        
        current_node = self.head
        while current_node is not None:
            if current_node.data == prev_node_data:
                new_node.next_ref = current_node.next_ref
                if current_node.next_ref is not None:
                    current_node.next_ref.prev_ref = new_node
                current_node.next_ref = new_node
                new_node.prev_ref = current_node
                return
            current_node = current_node.next_ref
        print("Previous node not found")
        
    def add_before(self, data, prev_node_data):
        new_node = Node(data)
        if self.head is None:
            print("Linked list is empty")
            return
        
        if self.head.data == prev_node_data:
            new_node.next_ref = self.head
            self.head.prev_ref = new_node
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next_ref is not None:
            if current_node.next_ref.data == prev_node_data:
                new_node.next_ref = current_node.next_ref
                current_node.next_ref.prev_ref = new_node
                current_node.next_ref = new_node
                new_node.prev_ref = current_node
                return
            current_node = current_node.next_ref
        print("Previous node not found")
        
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        self.head = self.head.next_ref
        if self.head is not None:
            self.head.prev_ref = None
            
    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        if self.head.next_ref is None:
            self.head = None
            return
        
        current_node = self.head
        while current_node.next_ref.next_ref is not None:
            current_node = current_node.next_ref
        current_node.next_ref = None
        
    def delete_by_value(self, node):
        if self.head is None:
            print("Linked list is empty")
            return
        
        if self.head.data == node:
            self.head = self.head.next_ref
            if self.head is not None:
                self.head.prev_ref = None
            return
        
        current_node = self.head
        while current_node.next_ref is not None:
            if current_node.data == node:
                current_node.next_ref = current_node.next_ref.next_ref
                if current_node.next_ref is not None:
                    current_node.next_ref.prev_ref = current_node
                return
            current_node = current_node.next_ref
        print("Node not found")