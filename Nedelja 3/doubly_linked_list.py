class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    def prepend(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete_first(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
        self.head = self.head.next
        self.prev = None

    def delete_last(self):
        if self.head is None:
            return 
        if self.head.next is None:
            self.head = None
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None
        current.prev = None
    
    def get_middle_node(self):
        current_1 = self.head
        current_2 = self.head
        while current_1.next:
            current_1 = current_1.next.next
            current_2 = current_2.next
        return current_2

    def __eq__(self, other):
        current_1 = self.head
        current_2 = other.head
        while current_1 and current_2:
            if current_1.value == current_2.value:
                current_1 = current_1.next
                current_2 = current_2.next
            else:
                return False
        if not current_1 and not current_2:
            return True
        else:
            return False


    def remove_duplicates(self):
        current_1 = self.head
        current_2 = self.head
        while current_1.next:
            while current_2.next:
                if current_2.next.value == current_1.value:
                    current_2.next = current_2.next.next
                else:
                    current_2 = current_2.next
            current_1 = current_1.next
            current_2 = current_1
    
    # Append, delete_last, delete_last_two, insert_at_position, delete_element_by_value, 
    # reverse (1 -> 2 -> 3 u 3 -> 2 -> 1), concat

