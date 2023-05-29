class Node:
    def __init__(self, value):
        """
        Initialize a Node object with a given value.

        Args:
        - value: The value to be stored in the node.

        """
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        """
        Initialize a Stack object with an empty stack.

        """
        self.top = None

    def push(self, value):
        """
        Push a value onto the top of the stack.

        Args:
        - value: The value to be pushed onto the stack.

        """
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        """
        Pop the value from the top of the stack and return it.

        Returns:
        - The value popped from the top of the stack.

        """
        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value

    def peek(self):
        """
        Return the value on the top of the stack without removing it.

        Returns:
        - The value on the top of the stack.

        """
        if self.top:
            return self.top.value

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
        - True if the stack is empty, False otherwise.

        """
        return not self.top


class PseudoQueue:
    def __init__(self):
        """
        Initialize a PseudoQueue object with two stacks.

        """
        self.stack1 = Stack()  # Stack for enqueue operation
        self.stack2 = Stack()  # Stack for dequeue operation

    def enqueue(self, value):
        """
        Insert a value into the PseudoQueue using a first-in, first-out approach.

        Args:
        - value: The value to be inserted into the PseudoQueue.

        """
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())
        self.stack1.push(value)

    def dequeue(self):
        """
        Extract a value from the PseudoQueue using a first-in, first-out approach.

        Returns:
        - The value extracted from the PseudoQueue.

        """
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
queue = PseudoQueue()
queue.enqueue(10)
queue.enqueue(15)
queue.enqueue(20)
print(queue.dequeue())  # Output: 10
print(queue.dequeue())  # Output: 15