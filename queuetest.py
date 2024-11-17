
class QueueTest:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    
    def print(self):
        for item in self.queue:
            print(item, end="->")
            
            