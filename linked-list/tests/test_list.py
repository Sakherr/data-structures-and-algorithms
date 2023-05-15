from linked_list import LinkedList

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

        