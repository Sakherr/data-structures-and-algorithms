class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

def inorder(tree):
    values = []
    if tree.root:
        _inorder(tree.root, values)
    return values

def _inorder(node, values):
    if node:
        _inorder(node.left, values)
        values.append(node.value)
        _inorder(node.right, values)

def intersection(list1, list2):
    hashmap = {}
    result = []
    for value in list1:
        if value not in hashmap:
            hashmap[value] = 1
        else:
            hashmap[value] += 1

    for value in list2:
        if value in hashmap and hashmap[value] > 0:
            result.append(value)
            hashmap[value] -= 1
    return set(result)

def tree_intersection(tree1, tree2):
    list1 = inorder(tree1)
    list2 = inorder(tree2)
    return intersection(list1, list2)


tree1 = BinaryTree(Node(150))
tree1.root.left = Node(100)
tree1.root.right = Node(250)
tree1.root.left.left = Node(75)
tree1.root.left.right = Node(160)
tree1.root.left.right.left = Node(125)
tree1.root.left.right.right = Node(175)
tree1.root.right.left = Node(200)
tree1.root.right.right = Node(350)
tree1.root.right.right.left = Node(300)
tree1.root.right.right.right = Node(500)

tree2= BinaryTree(Node(42))
tree2.root.left = Node(100)
tree2.root.right = Node(600)
tree2.root.left.left = Node(15)
tree2.root.left.right = Node(160)
tree2.root.left.right.left = Node(125)
tree2.root.left.right.right = Node(175)

tree2.root.right.left = Node(200)
tree2.root.right.right = Node(350)
tree2.root.right.right.left = Node(4)
tree2.root.right.right.right = Node(500)

print(tree_intersection(tree1, tree2))
