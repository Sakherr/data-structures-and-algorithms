# Trees

Node

Create a Node class that represents a node in a binary tree. It should have the following properties:

value: The value stored in the node.
left: A reference to the left child node.
right: A reference to the right child node.
Binary Tree

Create a BinaryTree class that represents a binary tree. It should have the following methods:

preorder_traversal: Performs a preorder traversal of the binary tree and returns an array of values.
inorder_traversal: Performs an inorder traversal of the binary tree and returns an array of values.
postorder_traversal: Performs a postorder traversal of the binary tree and returns an array of values.
Binary Search Tree

Create a BinarySearchTree class that extends the BinaryTree class. It should have the following additional methods:

add: Adds a new node with the given value to the binary search tree in the correct location.
Arguments: value - The value to be added.
Return: Nothing.
contains: Checks if the binary search tree contains a node with the given value.
Argument: value - The value to search for.
Returns: A boolean indicating whether or not the value is present in the tree at least once.

## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
 the time complexity is  O(n) for traversals and O(log n) to O(n) for adding and searching in a binary search tree. The space complexity is O(n) for traversals, O(1) for adding a node, and O(1) for searching a node in a binary search tree.
## Solution
 pytest