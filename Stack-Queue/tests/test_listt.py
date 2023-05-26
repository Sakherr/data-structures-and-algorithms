from linked_list import Stack, Queue

def test_stack():
    stack = Stack()

    # Test 1: Calling pop on empty stack raises exception
    try:
        stack.pop()
    except Exception as e:
        assert str(e) == "Stack is empty"
    else:
        assert False, "Expected exception when calling pop on empty stack"

    # Test 2: Calling peek on empty stack raises exception
    try:
        stack.peek()
    except Exception as e:
        assert str(e) == "Stack is empty"
    else:
        assert False, "Expected exception when calling peek on empty stack"

    # Test 3: Pushing and popping elements from the stack
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty() is True

    # Test 4: Pushing elements and checking the top value
    stack.push(3)
    assert stack.peek() == 3
    stack.push(4)
    assert stack.peek() == 4

   
def test_queue():
    queue = Queue()

    # Test 1: Calling dequeue on empty queue raises exception
    try:
        queue.dequeue()
    except Exception as e:
        assert str(e) == "Queue is empty"
    else:
        assert False, "Expected exception when calling dequeue on empty queue"

    # Test 2: Calling peek on empty queue raises exception
    try:
        queue.peek()
    except Exception as e:
        assert str(e) == "Queue is empty"
    else:
        assert False, "Expected exception when calling peek on empty queue"

    # Test 3: Enqueuing and dequeuing elements from the queue
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.is_empty() is True

    # Test 4: Enqueuing elements and checking the front value
    queue.enqueue(3)
    assert queue.peek() == 3
    queue.enqueue(4)
    assert queue.peek() == 3

    # Test 5: Enqueuing elements and checking if the queue is empty
    queue.enqueue(5)
    assert queue.is_empty() is False

