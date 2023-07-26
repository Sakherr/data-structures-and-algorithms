class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

def inorder(tree):
    values = LinkedListNode(None)
    current = values
    if tree.root:
        current = _inorder(tree.root, current)
    return values.next

def _inorder(node, current):
    if node:
        current = _inorder(node.left, current)
        current.next = LinkedListNode(node.value)
        current = current.next
        current = _inorder(node.right, current)
    return current

def intersection(list1, list2):
    hashmap = {}
    result = []
    current = list1
    while current:
        value = current.value
        if value not in hashmap:
            hashmap[value] = 1
        else:
            hashmap[value] += 1
        current = current.next

    current = list2
    while current:
        value = current.value
        if value in hashmap and hashmap[value] > 0:
            result.append(value)
            hashmap[value] -= 1
        current = current.next
    return result

def tree_intersection(tree1, tree2):
    list1 = inorder(tree1)
    list2 = inorder(tree2)
    return intersection(list1, list2)

