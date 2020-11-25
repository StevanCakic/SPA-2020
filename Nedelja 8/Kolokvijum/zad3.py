class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None
class DoublyLinkedlist:
    def __init__(self ):
        self.head = None
    
    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        new_node = Node(data)
        cur.next = new_node
        new_node.prev = cur
        new_node.next = None
    
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next
    
    def link_lists(self, l2):
        
        current_1 = self.head
        while current_1.next:
            current_1 = current_1.next
        current_1.next = l2.head
        self.print_list()

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

    def __contains__(self, data):
        if self.head == None:
            return False
        else:
            current = self.head
            while current:
                if current.value['cijena'] == data:
                    return True
                current = current.next
            return False
    def remove_largest_elements(self):
        maximum = -1
        current = self.head
        while current != None:
            if maximum < current.value['cijena']:
                maximum = current.value['cijena']
            current = current.next
        while maximum in self:
            self.delete_val(maximum, 'cijena')

    def remove_smallest_elements(self):
        minimum = 1000
        current = self.head
        while current:
            if minimum > current.value['cijena']:
                minimum = current.value['cijena']
            current = current.next
        self.delete_val(minimum, 'cijena')
    
    # {...., "godina": 2, "prosjek": 9} <-> {...., "godine":2, "prosjek": 8}] ; (9 + 8) / 2 = 8.5

    def prosjek_godine(self, year):
        zbir = 0
        broj_studenata_zadate_godine = 0
        current = self.head
        while current:
            if current.value["godina"] == year:
                zbir += current.value["prosjek"]
                broj_studenata_zadate_godine += 1
            current = current.next
        return zbir / broj_studenata_zadate_godine
    
    # 2 <-> 4 <-> 6 <-> 8 <-> 10 ; 3              output: 4 <-> 2
    def stampa_prije_indeksa(self, index):
        current = current.head
        count = 1
        while count < index:
            current = current.next
            count += 1
        previus = current
        while previus:
            print(previus.value)
            previus = previus.prev
