from tree import BinaryTree, BinarySearchTree, Node

def test_preorder_traversal():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)

    result = []
    tree.preorder_traversal(tree.root, result)
    assert result == [1, 2, 3]


def test_inorder_traversal():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)

    result = []
    tree.inorder_traversal(tree.root, result)
    assert result == [2, 1, 3]


def test_postorder_traversal():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)

    result = []
    tree.postorder_traversal(tree.root, result)
    assert result == [2, 3, 1]


def test_binary_search_tree_add():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(2)
    bst.add(6)
    bst.add(1)
    bst.add(3)
    bst.add(5)
    bst.add(7)

    result = []
    bst.inorder_traversal(bst.root, result)
    assert result == [1, 2, 3, 4, 5, 6, 7]


def test_binary_search_tree_contains():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(2)
    bst.add(6)

    assert bst.contains(4) is True
    assert bst.contains(2) is True
    assert bst.contains(6) is True
    assert bst.contains(5) is False