from insertion import insertion_sort

def test_insertion_sort_regular_input():
    input_array = [8, 4, 23, 42, 16, 15]
    expected_output = [4, 8, 15, 16, 23, 42]
    assert insertion_sort(input_array) == expected_output

def test_insertion_sort_reverse_sorted_input():
    input_array = [20, 18, 12, 8, 5, -2]
    expected_output = [-2, 5, 8, 12, 18, 20]
    assert insertion_sort(input_array) == expected_output

def test_insertion_sort_input_with_few_uniques():
    input_array = [5, 12, 7, 5, 5, 7]
    expected_output = [5, 5, 5, 7, 7, 12]
    assert insertion_sort(input_array) == expected_output

def test_insertion_sort_nearly_sorted_input():
    input_array = [2, 3, 5, 7, 13, 11]
    expected_output = [2, 3, 5, 7, 11, 13]
    assert insertion_sort(input_array) == expected_output

def test_insertion_sort_empty_input():
    input_array = []
    expected_output = []
    assert insertion_sort(input_array) == expected_output

def test_insertion_sort_single_element_input():
    input_array = [42]
    expected_output = [42]
    assert insertion_sort(input_array) == expected_output

def test_insertion_sort_all_elements_equal_input():
    input_array = [5, 5, 5, 5, 5]
    expected_output = [5, 5, 5, 5, 5]
    assert insertion_sort(input_array) == expected_output
