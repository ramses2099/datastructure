class Node:
    def __init__(self, data):
        self.data = data
        self.next_ref = None
   
class CircularSingleLinkedlist:
    def __init__(self) -> None:
        self.head = None
        
    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next_ref = self.head
        else:
            current_node = self.head
            while current_node.next_ref != self.head:
                current_node = current_node.next_ref
            current_node.next_ref = new_node
            new_node.next_ref = self.head
    
    def display(self):
        nodes = []
        if not self.head:
            print("Circular linked list is empty.")
            return
        current_node = self.head
        while True:
            nodes.append(current_node.data)
            current_node = current_node.next_ref
            if current_node == self.head:
                break
        print(" -> ".join(map(str,nodes)) + " -> ... (back to head)")