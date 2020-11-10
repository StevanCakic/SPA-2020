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

    # Prosirio sam ovu funkciju radi potreba za zadatak 1 !!!
    def delete_val(self, value, key):
        current = self.head
        prev = None
        while current.value[key] != value and current.next:
            prev = current
            current = current.next
        
        if current.value[key] == value:
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

    # Za potrebe zadatka 1, implementacija operacije in
    def __contains__(self, data):

        if self.head == None:
            return False
        else:
            current = self.head
            while current is not None:
                # Poredimo da li su knjige jednake po cijeni !!! 
                if current.value["cijena"] == data:
                    return True
                current = current.next
            return False

    # Slicno mozete implementirati i za lowest element! To ostavljam da sami uradite.
    def remove_largest_elements(self):  
  
        # Declare a max variable and initialize  
        # it with INT_MIN value.  
        # INT_MIN is integer type and its value  
        # is -32767 or less.  
        max = -32767
        current = self.head
        # Check loop while head not equal to None  
        while current != None: 
        
            # If max is less then head.data then  
            # assign value of head.data to max  
            # otherwise node point to next node.  
            if max < current.value["cijena"] : 
                max = current.value["cijena"]
            current = current.next
        
        while max in self:
            self.delete_val(max, "cijena")

# Napomena: Node ne mora da sadrzi samo broj kao value
# Dozvoljeni su svi tipovi podataka koje smo i ranije radili
n1 = Node({"sifra": 123, "naziv": "na drini cuprija", "autor": 1234, "cijena": 10.50})
n2 = Node({"sifra": 231, "naziv": "dervis i smrt", "autor": 4321, "cijena": 8.50})
n3 = Node({"sifra": 131, "naziv": "zlocin i kazna", "autor": 3321, "cijena": 12.50})
n4 = Node({"sifra": 223, "naziv": "zapisi iz podzemlja", "autor": 3321, "cijena": 12.50})

l1 = LinkedList()
l1.prepend(n4)
l1.prepend(n3)
l1.prepend(n2)
l1.prepend(n1)

l1.print_list()
print("Nakon brisanja")
l1.remove_largest_elements()
l1.print_list()




