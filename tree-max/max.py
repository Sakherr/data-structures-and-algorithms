class Node:
    def __init__(self, data):
        """
        Initializes a new node with the given data.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        """
        Initializes a new binary tree.
        """
        self.root = None

    def find_maximum_value(self):
        """
        Finds the maximum value stored in the binary tree.

        Returns:
            The maximum value stored in the binary tree.
            Returns None if the tree is empty.
        """
        if self.root is None:
            return None

        return self._find_maximum_value_recursive(self.root)

    def _find_maximum_value_recursive(self, node):
        """
        Helper function to recursively find the maximum value in the binary tree.

        Args:
            node: The current node being processed.

        Returns:
            The maximum value found in the binary tree.
        """
        if node is None:
            return float('-inf')

        max_value = node.data
        left_max = self._find_maximum_value_recursive(node.left)
        right_max = self._find_maximum_value_recursive(node.right)

        if left_max > max_value:
            max_value = left_max
        if right_max > max_value:
            max_value = right_max

        return max_value
