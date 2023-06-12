from max import BinaryTree, Node
import pytest
@pytest.fixture
def binary_tree():
    # Create a binary tree
    tree = BinaryTree()

    # Populate the tree with nodes
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(8)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(7)
    tree.root.right.left = Node(9)
    tree.root.right.right = Node(11)

    return tree

def test_max_value_empty_tree():
    tree = BinaryTree()  # Empty tree
    expected = None
    assert tree.find_maximum_value() == expected

def test_max_value(binary_tree):
    expected = 11
    assert binary_tree.find_maximum_value() == expected


@pytest.fixture
def binary_tree2():
    tree = BinaryTree()

    tree.root = Node(7)
    tree.root.left = Node(3)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.right.left = Node(1)
    tree.root.right.right = Node(9)

    return tree
    

def test_max_value_other_output(binary_tree2):
    expected = 9
    assert binary_tree2.find_maximum_value() == expected