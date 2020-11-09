class Node:
    def __init__(self, value):
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

    # Za potrebe zadatke 12 pod c)
    # Ako je potrebno pojasnjenje -> https://www.youtube.com/watch?v=xFuJI29BiDY
    def reverse(self): 
        prev = None
        current = self.head 
        while current is not None: 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev
    
    # Za potrebe zadatka 13
    def countIncreasingElements(self, head):  
        # Obilazimo listu i pratimo duzinu najvece rastuce i trenutno rastuce podliste 
        curr_len = 1
        max_len = 1
        total_count = 1
        res_index = 0
        curr = head  
        while(curr.next != None):  
            
            # Ako je trenutno vrijednost manja od next, onda se siri rastuca podlista
            if (curr.value < curr.next.value):  
                curr_len = curr_len + 1
            else:  
                
                # poredimo trenutni max_len sa trenutnom duzinom podliste
                if (max_len < curr_len):  
                    max_len = curr_len  
                    res_index = total_count - curr_len  
                
                curr_len = 1
            
            total_count = total_count + 1
            curr = curr.next
        
        if (max_len < curr_len):  
            max_len = curr_len  
            res_index = total_count - max_len  
        
        # Duzina najduze rastuce podliste je  
        print("Duzina najduze rastuce podliste je : ", max_len)  
    
        # Ponovo prolazimo kroz listu i stampamo onu najduzi rastucu podlistu
        i = 0
        print("Rastuca podlista")  
        curr = head 
        str_final = ""
        while curr != None:  
            
            # Poredimo index sa onim od kog treba krenuti sa prikazom/stampom elemenata najduze
            # podliste 
            if i == res_index:  
                
                # Vrtimo petlju sve do kraja te najduze rastupe podliste 
                
                while (max_len > 0): 
                    str_final += str(curr.value) + " " # mozete direktno i ovdje da stampate
                    curr = curr.next
                    max_len = max_len - 1
                
                break
            
            i = i + 1
            curr = curr.next
        print(str_final)

# Zadatak 12
l1 = LinkedList()
element = int(input("Unesite element liste:"))

# Pod a)
while element != 0:
    n = Node(element)
    l1.prepend(n)
    element = int(input("Unesite element liste:"))
l1.print_list()

# Pod b)    
l2 = LinkedList()
element = int(input("Unesite element liste:"))
if element != 0: # provjeriti da li je prvi element razlicit od 0 za svaki slucaj
    # Sad dodajmo drugi element
    l2.prepend(Node(element))
    element = int(input("Unesite element liste:"))
    while element != 0:
        n = Node(element)
        if element <= l2.get_value_from_position(1).value: 
            l2.prepend(n)
        else:
            l2.append(n)
        element = int(input("Unesite element liste:"))
        
l2.print_list()

# Pod c)
l3 = LinkedList()
element = int(input("Unesite element liste:"))

while element != 0:
    n = Node(element)
    l3.append(n)
    element = int(input("Unesite element liste:"))

l3.reverse() # implementirano u klasi za jednostruku listu !
l3.print_list()

# Zadatak 13 [ovo je malo tezi zadatak !]
# Preskocicu dio ucitavanje i upisivanja iz/u fajl, to ostavljam vama, vrlo je jednostavno
# radjeno iz programiranja 1 !

n1 = Node(5)
n2 = Node(7)
n3 = Node(3)
n4 = Node(2)

l1.prepend(n4)
l1.prepend(n3)
l1.prepend(n2)
l1.prepend(n1)

l1.print_list()
l1.countIncreasingElements(l1.head)


# Zadatak 14, uputstvo
# 1) Kreirati listu 3 -> 4 -> 6 -> 7 -> 0
# 1*) Kreirati praznu listu koja ce biti finalna lista (zvacemo je final_list)
# 2) Uzimati dva susjedna elementa iz liste (uvijek provjerovati da li postoje oba)
# 3) Naci razliku izmedju lijevog i desnog
# 4) U final_list dodati (prepend) lijevi cvor, pa njihovu razliku (kao novi cvor), i desni cvor
# 5) Korake 2-4 ponavljati dok postoje dva susjedna elementa (lijevi i desni!)