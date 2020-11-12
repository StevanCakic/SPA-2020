# Zadatak 5
from stack_ex import Stack
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
print(s.get_stack())

r = remove_duplicates_in_pair(s)
reverse_stack(r)
print(r.get_stack())

print(remove_duplicates(r).get_stack())

