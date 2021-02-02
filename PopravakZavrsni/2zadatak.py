class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def length(self): 
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def get_stack(self):
        return self.items

def reverse(izvorni):
    count = 0
    pomocni = Stack()
    while count != izvorni.length() - 1: 
      
        topVal = izvorni.pop() 
        while count != izvorni.length(): 
            pomocni.push(izvorni.pop()) 
            
        izvorni.push(topVal) 
        while pomocni.length() != 0: 
            izvorni.push(pomocni.pop()) 
          
        count += 1
    return izvorni

def prebroj_bombe(S):
    pomocni = Stack()
    brojac = 0
    while not S.is_empty():
        a = S.pop()
        if a != "+":
            pomocni.push(a)
        else:
            brojac += 1
    while not pomocni.is_empty():
        S.push(pomocni.pop())
    reverse(S)
    return S
    

S1 = Stack()
S1.push("+")
S1.push("D")
S1.push("+")
S1.push("C")
S1.push("B")
S1.push("A")

print(S1.get_stack())
print(prebroj_bombe(S1).get_stack())