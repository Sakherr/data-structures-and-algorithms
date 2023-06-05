class Node:
    """
    Node class represents a node in a linked list-based stack.
    """
    def __init__(self, value):
        """
        Initializes a new instance of the Node class.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None


class Stack:
    """
    Stack class represents a stack data structure implemented using a linked list.
    """
    def __init__(self):
        """
        Initializes a new instance of the Stack class.
        """
        self.top = None

    def push(self, value):
        """
        Pushes a value onto the top of the stack.

        Args:
            value: The value to be pushed onto the stack.
        """
        new_node = Node(value)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Removes and returns the value at the top of the stack.

        Returns:
            The value at the top of the stack, or None if the stack is empty.
        """
        if self.top:
            popped_value = self.top.value
            self.top = self.top.next
            return popped_value
        return None

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.top is None


def validate_brackets(string):
    """
    Validates whether the brackets in the given string are balanced.

    Args:
        string: The string to be validated.

    Returns:
        True if the brackets are balanced, False otherwise.
    """
    stack = Stack()
    brackets_map = {'(': ')', '[': ']', '{': '}'}

    for char in string:
        if char in brackets_map.keys():
            stack.push(char)
        elif char in brackets_map.values():
            if stack.is_empty():
                return False
            opening_bracket = stack.pop()
            if brackets_map[opening_bracket] != char:
                return False
    
    return stack.is_empty()


# Test cases for balanced brackets
print(validate_brackets("{}"))  # True
print(validate_brackets("{}(){}"))  # True
print(validate_brackets("()[[Extra Characters]]"))  # True
print(validate_brackets("(){}[[]]"))  # True
print(validate_brackets("{}{Code}[Fellows](())"))  # True

# Test cases for unbalanced brackets
print(validate_brackets("[({}]"))  # False
print(validate_brackets("(]("))  # False
print(validate_brackets("{(})"))  # False

# Additional test cases
print(validate_brackets(""))  # True (empty string)
print(validate_brackets("()"))  # True (single pair of brackets)
print(validate_brackets("[[()]]"))  # True (nested brackets)
print(validate_brackets("{[}]"))  # False (unbalanced nested brackets)
print(validate_brackets("([)]"))  # False (mixed brackets)
