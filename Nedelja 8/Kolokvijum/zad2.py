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

# a) Input: 5 -> 4 -> 3 -> 8 -> 2; Output: 16 -> 64 -> 4
    def parni_kvadrati(self):
        l2 = LinkedList()
        current = self.head
        while current:
            if current.value % 2 == 0:
                cvor = Node(current.value ** 2)
                l2.append(cvor)
            current = current.next
        
        l2.print_list()

# b) Input: 5 -> 4 -> 3 -> 8 -> 2; Output: 5 -> 3 -> 2
    def delete_every_second(self):
        current = self.head
        current2 = current.next
        while current.next:
            current_2 = current.next
            current.next = current_2.next
            current = current.next
        self.print_list()