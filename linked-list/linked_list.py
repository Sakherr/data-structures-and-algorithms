class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    
   def kth_from_end(self, k):
    if self.head is None:
        raise Exception("Empty List")
    elif k < 0:
        raise Exception("Invalid value of k")

    slow_ptr = self.head
    fast_ptr = self.head

    for _ in range(k):
        if fast_ptr is None:
            raise Exception("k is greater than the length of the linked list")
        fast_ptr = fast_ptr.next

    if fast_ptr is None:
        raise Exception("k is greater than the length of the linked list")

    while fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next

    return slow_ptr.value

    
   def __init__(self):
        self.head = None

   def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

   def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

   def to_string(self):
        if self.head is None:
            return "NULL"
        else:
            result = ""
            current = self.head
            while current is not None:
                result += "{{ {} }} -> ".format(current.value)
                current = current.next
            result += "NULL"
            return result
    
   def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

   def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            raise Exception("Empty List")
        elif self.head.value == value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                if current.next.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
            raise Exception("   No Value ")


   def insert_after(self, value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            raise Exception("Empty List")
        else:
            current = self.head
            while current is not None:
                if current.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
            raise Exception("No Value")



