class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def get_stack(self):
        return self.items

'''
s = Stack()
print(s.is_empty())
s.push(1)
s.push(2)
print(s.is_empty())
print(s.peek())
print(s.get_stack())
s.pop()
print(s.get_stack())
'''