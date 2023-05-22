class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
    
    
    
    
    
    
    
    
    
    def zip_lists(values1, values2):
        list1 = Node(values1[0])
        current1 = list1
        for value in values1[1:]:
            current1.next = Node(value)
            current1 = current1.next

        list2 = Node(values2[0])
        current2 = list2
        for value in values2[1:]:
            current2.next = Node(value)
            current2 = current2.next

        if not list1:
            return list2
        if not list2:
            return list1

        dummy_head = Node()
        current = dummy_head

        while list1 and list2:
            current.next = list1
            list1 = list1.next
            current = current.next

            current.next = list2
            list2 = list2.next
            current = current.next

        current.next = list1 or list2

        return dummy_head.next
