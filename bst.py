class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)
            
    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)
                
    def search(self, data):
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, current_node, data):
        if not current_node:
            return False
        elif current_node.data == data:
            return True
        elif data < current_node.data:
            return self._search_recursive(current_node.left, data)
        else:
            return self._search_recursive(current_node.right, data)
        
    def delete(self,data):
        self.root = self._delete_recursive(self.root, data)
        
    def _delete_recursive(self, current_node, data):
        if not current_node:
            return current_node
        
        if data < current_node.data:
            current_node.left = self._delete_recursive(current_node.left, data)
        elif data > current_node.data:
            current_node.right = self._delete_recursive(current_node.right, data)
        else:
            if not current_node.left and not current_node.right:
                current_node = None
            elif not current_node.left:
                current_node = current_node.right
            elif not current_node.right:
                current_node = current_node.left
            else:
                min_value = self._find_min_value(current_node.right)
                current_node.data = min_value
                current_node.right = self._delete_recursive(current_node.right, min_value)
                
        return current_node
    
    def _find_min_value(self, node):
        current_node = node
        while current_node.left:
            current_node = current_node.left
        return current_node.data
    
    def inorder_traversal(self):
        """Perform an in-order traversal of the tree."""
        result = []
        self._inorder_recursively(self.root, result)
        return result

    def _inorder_recursively(self, current, result):
        if current is not None:
            self._inorder_recursively(current.left, result)
            result.append(current.value)
            self._inorder_recursively(current.right, result)

    def preorder_traversal(self):
        """Perform a pre-order traversal of the tree."""
        result = []
        self._preorder_recursively(self.root, result)
        return result

    def _preorder_recursively(self, current, result):
        if current is not None:
            result.append(current.value)
            self._preorder_recursively(current.left, result)
            self._preorder_recursively(current.right, result)

    def postorder_traversal(self):
        """Perform a post-order traversal of the tree."""
        result = []
        self._postorder_recursively(self.root, result)
        return result

    def _postorder_recursively(self, current, result):
        if current is not None:
            self._postorder_recursively(current.left, result)
            self._postorder_recursively(current.right, result)
            result.append(current.value)
