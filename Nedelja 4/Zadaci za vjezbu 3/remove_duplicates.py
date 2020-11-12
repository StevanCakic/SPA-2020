# Zadatak 5
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

def remove_duplicates_in_pair(s):
    res = Stack()
    while not s.is_empty():
        elem = s.pop()        
        if s.peek() != elem:    
            res.push(elem); 
    return res

def reverse_stack(stack):
    stack.get_stack().reverse()
    return stack

def remove_duplicates(s):
    l = s.get_stack().copy() # ovo obavezno da se ne desi da odradimo reverse i nad s i nad l
    l.reverse()
    
    new_stack = Stack()
    counter = 1
    while not s.is_empty():
        elem = s.pop()
        if elem not in l[counter:]:
            new_stack.push(elem)
        counter = counter + 1
    
    return reverse_stack(new_stack)

s = Stack()
s.push(1)
s.push(2)
s.push(1)
s.push(1)
s.push(3)
s.push(1)
print(s.get_stack())

r = remove_duplicates_in_pair(s)
reverse_stack(r)
print(r.get_stack())

print(remove_duplicates(r).get_stack())

