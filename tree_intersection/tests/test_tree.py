from tree_intersection import BinaryTree, Node, tree_intersection

def test_tree_intersection_1():
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

    assert set(tree_intersection(tree1, tree2)) == {100, 125, 160, 175, 200, 350, 500}

def test_tree_intersection_2():
    tree1 = BinaryTree(Node(182))
    tree1.root.left = Node(6)
    tree1.root.right = Node(482)

    tree2= BinaryTree(Node(482))
    tree2.root.left = Node(10)
    tree2.root.right = Node(6)

    assert set(tree_intersection(tree1, tree2)) == {482,6}

def test_tree_intersection_3():
    tree1 = BinaryTree(Node(-100))
    tree1.root.left = Node(200)
    tree1.root.right = Node(-50)

    tree2= BinaryTree(Node(-300))
    tree2.root.left = Node(-400)
    tree2.root.right = Node(200)

    assert set(tree_intersection(tree1, tree2)) == {200}
