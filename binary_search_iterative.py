"""Iterative Binary search function.
Function takes two inputs:
a Python list to search through, and the value searched for.
Assume the list only has distinct elements,
and elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    while low <= high:
        mid = (low + high)/2
        if input_array[mid] == value:
            return mid
        elif input_array[mid] >= value:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# Test cases
test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)