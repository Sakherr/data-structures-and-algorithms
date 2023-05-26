from linked_list import LinkedList, zip_lists

def test_zip_lists_empty_lists():
    """Tests that the function returns an empty list if both input lists are empty."""
    assert list(zip_lists(LinkedList(), LinkedList())) == []

def test_zip_lists_one_empty_list():
    """Tests that the function returns the non-empty list if one input list is empty."""
    assert list(zip_lists(LinkedList(), LinkedList([1, 2, 3]))) == [1, 2, 3]
    assert list(zip_lists(LinkedList([1, 2, 3]), LinkedList())) == [1, 2, 3]

def test_zip_lists_non_empty_lists():
    """Tests that the function zips the two input lists together correctly."""
    assert list(zip_lists(LinkedList([1, 2, 3]), LinkedList([4, 5, 6]))) == [1, 4, 2, 5, 3, 6]
