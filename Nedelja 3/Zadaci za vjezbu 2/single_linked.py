class Node:
    def __init__(self, value = None):
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def prepend(self, new_element):
        new_element.next = self.head
        self.head = new_element
    
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def delete_first(self):
        if not self.head:
            return None
        self.head = self.head.next

    def delete_last(self):
        current = self.head
        while current.next:
            prev = current
            current = current.next
        prev.next = None

    def get_value_from_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter = counter + 1
        return None

    def insert_on_position(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter = counter + 1
            return None
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
        else:
            return None

    def delete_val(self, value):
        current = self.head
        prev = None
        while current.value != value and current.next:
            prev = current
            current = current.next
        
        if current.value == value:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next
    
    def delete_from_position(self, position):
        current = self.head
        prev = None
        counter = 1

        if position == 1:
            self.head = current.next
            current = None
            return
        
        while current and counter != position:
            prev = current
            current = current.next
            counter = counter + 1

        if current is None:
            return None

        prev.next = current.next
        current = None

    def len_iterative(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count = count + 1
        return count

    def getCountRec(self, node):
        if not node:
            return 0
        else:
            return 1 + self.getCountRec(node.next)
    
    def len_recursive(self):
        return self.getCountRec(self.head)

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    # Dodatna funkcija za zadatak 1
    def __eq__(self, l2):
        
        # ako je duzina listi razlicita, sigurno su razlicite
        if self.len_iterative() != l2.len_iterative():
            return False
        else:
            c1 = self.head
            c2 = l2.head
            while c1 and c2:
                # ako se vrijednosti listi razliku na istim pozicijama, liste se razlikuju
                if c1.value != c2.value: 
                    return False
                c1 = c1.next
                c2 = c2.next
            return True
    
    # Zadatak 2 - iz nekog razloga beskonacna petlja mi se javlja (linija 144 iz nekog razloga sporna)
    # Mozete da probate da napravite trecu listu koja ce da bude concat(l1 i l2)
    def list_concat(self, l2):
        current = self.head
        while current.next != None:
            current = current.next  
        current.next = l2.head
        return self.head
    
    # Zadatak 5
    def intersect(self, olinked):
        thisone = self.head
        otherone = olinked.head
        final = LinkedList()
        while thisone:
            while otherone:
                if thisone.value == otherone.value:
                    final.append(Node(otherone.value))
                    break
                else:
                    otherone = otherone.next
            thisone = thisone.next
            otherone = olinked.head
        return final

n1 = Node(5)
n2 = Node(7)
n3 = Node(3)
n4 = Node(2)
n5 = Node(1)

l1 = LinkedList()
l1.prepend(n4)
l1.prepend(n3)
l1.prepend(n2)
l1.prepend(n1)

l1.print_list()

l2 = LinkedList()
l2.prepend(n4)
l2.prepend(n3)
l2.prepend(n2)
l2.prepend(n5) # ako promijenite n5 u n1 vraca True, jer su liste iste u tom slucaju

l2.print_list()

print(l1 == l2)

# Zadata 2
# l1.list_concat(l2)
# l2.print_list()

# Zadatak 5
l3 = l1.intersect(l2)
print("Intersaction")
l3.print_list()

