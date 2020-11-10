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

    def __len__(self):
        return len(self.items)
    
    # U postavci su s1 i s2 parametri, ja sam uzeo da je self s1, mada moglo je da bude i
    # self, s1, s2 da budu parametri
    def parnepar(self, s2):
        s1 = Stack()
        while not self.is_empty():
            element = self.pop()
            if element % 2 == 0:
                s1.push(element)
            else:
                s2.push(element)
        return s1, s2
# Zadatak 2        
s = Stack()
print(s.is_empty())
s.push("*")
s.push("D")
s.push("*")
s.push("C")
s.push("B")
s.push("A")

new_stack = Stack()
while not s.is_empty():
    element = s.pop()
    if element != "*":
        new_stack.push(element)
print(new_stack.get_stack())

# Zadatak 3
s = Stack()
s2 = Stack()
s.push(3)
s.push(1)
s.push(4)
s.push(1)
s.push(2)
s.push(6)

parnep = s.parnepar(s2)
print(parnep[0].get_stack(), parnep[1].get_stack()) # napomena, funkcija parnepar vraca torku!

# Zadatak 4
# Potrebno je samo porediti element sa vrha oba stack-a
# Onaj koji je manji, pushujete, a sa stack-a sa kog ste uzeli taj manji element, uklonite ga
# i idete na sledecu iteraciju
# s1: [1 3 5] s2: [ 2 3 4]
# I) Poredim 5 i 4, manji je 4, ukljunjam ga sa vrha s2 i cuvam u novi stack koji trenutno izgleda:
#    s: [4], s1: [1 3 5] s2:[2 3]
# II) Sa poredite 5 i 3, manji je 3, njega micete
#    s: [4 3] , s1: [1 3 5] s2: [2]
# III) Poredite 5 i 2, 2 je manje:
#    s: [4 3 2], s1: [1 3 5] s2: []
# IV) Kako je s2 sad prazan samo ostaje da sve elemente sa s1 prebacite u s
#    s: [4 3 2 5 3 1]
# Napomena: sa stack uvijek uzimate poslednji element

# Zadatak 5
# Ovaj zadatak je prilicno jasan, trebalo bi da mozete da ga rijesite bez problema