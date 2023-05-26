class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, values=None):
        self.head = None

        if values is not None:
            for value in values:
                self.add_node(value)

    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next


def zip_lists(list1, list2):
    """Zips two linked lists together into one so that the nodes alternate between the two lists.

    Args:
        list1: The first linked list.
        list2: The second linked list.

    Returns:
        A new linked list, zipped as noted above.
    """
    if not list1.head and not list2.head:
        return LinkedList()  # Return an empty list

    zipped_list = LinkedList()
    current_node = zipped_list.head = Node(None)

    while list1.head and list2.head:
        if list1.head is not None:
            current_node.next = list1.head
            list1.head = list1.head.next
            current_node = current_node.next
        if list2.head is not None:
            current_node.next = list2.head
            list2.head = list2.head.next
            current_node = current_node.next

    if list1.head:
        current_node.next = list1.head
    if list2.head:
        current_node.next = list2.head

    zipped_list.head = zipped_list.head.next

    return zipped_list


list1 = LinkedList()
list1.add_node(1)
list1.add_node(3)
list1.add_node(5)

list2 = LinkedList()
list2.add_node(2)
list2.add_node(4)
list2.add_node(6)

zipped_list = zip_lists(list1, list2)

for node in zipped_list:
  print(node)
