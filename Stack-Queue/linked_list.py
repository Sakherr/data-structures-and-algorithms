class Node:
    def __init__(self, value):
        """
        Initialize a new Node with the given value.
        """
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        """
        Initialize an empty Stack.
        """
        self.top = None

    def push(self, value):
        """
        Push a new element with the given value onto the top of the Stack.
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Remove and return the element at the top of the Stack.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        """
        Return the value of the element at the top of the Stack without removing it.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        """
        Check if the Stack is empty. Returns True if the Stack is empty, False otherwise.
        """
        return self.top is None


class Queue:
    def __init__(self):
        """
        Initialize an empty Queue.
        """
        self.head = None
        self.tail = None

    def enqueue(self, value):
        """
        Add a new element with the given value to the back of the Queue.
        """
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Remove and return the element at the front of the Queue.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

    def peek(self):
        """
        Return the value of the element at the front of the Queue without removing it.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.head.value

    def is_empty(self):
        """
        Check if the Queue is empty. Returns True if the Queue is empty, False otherwise.
        """
        return self.head is None


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2
print(stack.is_empty())  # Output: False

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.peek())  # Output: 2
print(queue.is_empty())  # Output: False
