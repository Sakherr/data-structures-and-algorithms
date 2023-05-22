from linked_list import LinkedList
from linked_list import Stack
from linked_list import Queue



def test_instantiate_empty_linked_list():
    my_list = LinkedList()
    assert my_list.head is None


def test_insert_into_linked_list():
    my_list = LinkedList()
    my_list.insert('a')
    assert my_list.head.value == 'a'
    assert my_list.head.next is None


def test_insert_multiple_nodes():
    my_list = LinkedList()
    my_list.insert('c')
    my_list.insert('b')
    my_list.insert('a')
    assert my_list.head.value == 'a'
    assert my_list.head.next.value == 'b'
    assert my_list.head.next.next.value == 'c'
    assert my_list.head.next.next.next is None


def test_search_existing_value():
    my_list = LinkedList()
    my_list.insert('c')
    my_list.insert('b')
    my_list.insert('a')
    assert my_list.includes('b') is True


def test_search_nonexistent_value():
    my_list = LinkedList()
    my_list.insert('c')
    my_list.insert('b')
    my_list.insert('a')
    assert my_list.includes('d') is False


def test_return_all_values():
    my_list = LinkedList()
    my_list.insert('c')
    my_list.insert('b')
    my_list.insert('a')
    assert my_list.to_string() == "{ a } -> { b } -> { c } -> NULL"




def test_append():

    my_list = LinkedList()

    my_list.append('a')
    assert my_list.head.value == 'a'
    assert my_list.head.next is None

    my_list.append('b')
    assert my_list.head.value == 'a'
    assert my_list.head.next.value == 'b'
    assert my_list.head.next.next is None

    my_list.append('c')
    assert my_list.head.value == 'a'
    assert my_list.head.next.value == 'b'
    assert my_list.head.next.next.value == 'c'
    assert my_list.head.next.next.next is None


def test_insert_before():
    my_list = LinkedList()

    my_list.append('a')
    my_list.append('b')
    my_list.insert_before('b', 'x')
    assert my_list.head.value == 'a'
    assert my_list.head.next.value == 'x'
    assert my_list.head.next.next.value == 'b'
    assert my_list.head.next.next.next is None

    my_list.insert_before('a', 'y')
    assert my_list.head.value == 'y'
    assert my_list.head.next.value == 'a'
    assert my_list.head.next.next.value == 'x'
    assert my_list.head.next.next.next.value == 'b'
    assert my_list.head.next.next.next.next is None


def test_insert_after_append():
    my_list = LinkedList()

    my_list.append('a')
    my_list.append('b')
    my_list.insert_after('a', 'x')
    assert my_list.head.value == 'a'
    assert my_list.head.next.value == 'x'
    assert my_list.head.next.next.value == 'b'
    assert my_list.head.next.next.next is None

    my_list.insert_after('b', 'y')
    assert my_list.head.value == 'a'
    assert my_list.head.next.value == 'x'
    assert my_list.head.next.next.value == 'b'
    assert my_list.head.next.next.next.value == 'y'
    assert my_list.head.next.next.next.next is None

def test_kth_from_end():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)

    try:
        linked_list.kth_from_end(6)
    except Exception as e:
        assert str(e) == "k is greater than the length of the linked list"

    assert linked_list.kth_from_end(4) == 1
    
    try:
        linked_list.kth_from_end(-2)
    except Exception as e:
        assert str(e) == "Invalid value of k"

    single_list = LinkedList()
    single_list.append(1)
    assert single_list.kth_from_end(0) == 1

    assert linked_list.kth_from_end(2) == 3


def test_queue():
    queue = Queue()

    queue.enqueue(10)
    assert queue.peek() == 10

    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.peek() == 10

    assert queue.dequeue() == 10
    assert queue.peek() == 20

    assert queue.peek() == 20

    queue.dequeue()
    assert queue.is_empty() is False
    queue.dequeue()
    assert queue.is_empty() is True

    empty_queue = Queue()
    assert empty_queue.is_empty() is True

  
def test_stack():
    stack = Stack()

    stack.push(10)
    assert stack.peek() == 10

    stack.push(20)
    stack.push(30)
    assert stack.peek() == 30

    assert stack.pop() == 30
    assert stack.peek() == 20

    stack.pop()
    assert stack.is_empty() is True


    empty_stack = Stack()
    assert empty_stack.is_empty() is True

