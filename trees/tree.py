class Node:
    def __init__(self, value):
        """
        Initialize a new Node with the given value.

        Args:
            value: The value to be stored in the Node.
        """
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        """
        Initialize a new BinaryTree with an empty root.
        """
        self.root = None

    def preorder_traversal(self, node, result):
        """
        Perform a preorder traversal of the binary tree starting from the given node.

        Args:
            node: The starting node for the traversal.
            result: A list to store the traversed node values.

        Returns:
            None
        """
        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)

    def inorder_traversal(self, node, result):
        """
        Perform an inorder traversal of the binary tree starting from the given node.

        Args:
            node: The starting node for the traversal.
            result: A list to store the traversed node values.

        Returns:
            None
        """
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)

    def postorder_traversal(self, node, result):
        """
        Perform a postorder traversal of the binary tree starting from the given node.

        Args:
            node: The starting node for the traversal.
            result: A list to store the traversed node values.

        Returns:
            None
        """
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)


class BinarySearchTree(BinaryTree):
    def __init__(self):
        """
        Initialize a new BinarySearchTree by calling the base class constructor.
        """
        super().__init__()

    def add(self, value):
        """
        Add a new node with the given value to the binary search tree.

        Args:
            value: The value to be added.

        Returns:
            None
        """
        if not self.root:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        """
        Recursively find the correct position to add the new node with the given value.

        Args:
            node: The current node being traversed.
            value: The value to be added.

        Returns:
            None
        """
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_recursive(node.right, value)

    def contains(self, value):
        """
        Check if the binary search tree contains a node with the given value.

        Args:
            value: The value to search for.

        Returns:
            True if the value is found, False otherwise.
        """
        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, node, value):
        """
        Recursively search for a node with the given value in the binary search tree.

        Args:
            node: The current node being traversed.
            value: The value to search for.

        Returns:
            True if the value is found, False otherwise.
        """


        
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._contains_recursive(node.left, value)
        if value > node.value:
            return self._contains_recursive(node.right, value)
