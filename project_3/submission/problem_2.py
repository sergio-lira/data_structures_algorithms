def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list == None or len(input_list) == 0:
        return -1

    arr_size = len(input_list)
    pivot = find_pivot(input_list, 0, arr_size-1)

    if pivot == -1:
        return binary_search(input_list, number, 0, arr_size-1)
    elif input_list[pivot] == number:
        return pivot
    elif input_list[0] <= number:
        return binary_search(input_list, number, 0, pivot-1)
    else:
        return binary_search(input_list, number, pivot+1, arr_size-1)

def binary_search(input_list, target, start, end):
    #Base Cases
    if end < start:
        return -1

    middle = (start + end) // 2
    if input_list[middle] == target:
        return middle

    #Recursive search
    if target < input_list[middle]:
        return binary_search(input_list, target, start, middle-1)
    else:
        return binary_search(input_list, target, middle+1, end)

def find_pivot(input_list, start, end):
    #Base Cases
    if end < start:
        return -1
    elif start == end:
        return end
    middle = (start + end) // 2
    #Look for the pivot by searching for the value that is either larger than it's right side
    # or smaller than it's left side
    #Check if the element to the 'right' is smaller
    if middle < end and input_list[middle] > input_list[middle + 1]:
        return middle
    #Check if the element to the 'left' is larger
    elif middle > start and input_list[middle] < input_list[middle - 1]:
        return middle -1
    #Recursive search
    #if the value at the start is larger than the value at the middle, the pivot is somewhere in between
    elif input_list[start]  > input_list[middle]:
        return find_pivot(input_list, start, middle-1)
    #Else the opossite is true
    else:
        return find_pivot(input_list, middle+1, end)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        return "Pass"
    else:
        return "Fail"

print("<< Basic Test Cases >> ")
arr = [6, 7, 8, 9, 10, 1, 2, 3, 4]
print("Array: {}".format(arr))
print("Searching for 6: {}".format(test_function([arr, 6])))
print("Searching for 1: {}".format(test_function([arr, 1])))
arr = [6, 7, 8, 1, 2, 3, 4]
print("Array: {}".format(arr))
print("Searching for 6: {}".format(test_function([arr, 8])))
print("Searching for 6: {}".format(test_function([arr, 1])))
print("Searching for 6: {}".format(test_function([arr, 10])))

print("\n<< Edge Test Cases >> ")
arr = [n for n in range(0,25)]
print("Sorted Array: {}".format(arr))
print("Searching for 20: {}".format(test_function([arr, 8])))
print("Empty Array: {}".format([]))
print("Searching for 20: {}".format(test_function([[], 1])))
arr = [n for n in range(-20,1,1)]
print("Negative Array: {}".format(arr))
print("Searching for 20: {}".format(test_function([arr, -11])))
arr = arr[10:]+arr[0:10]
print("Rotated Array: {}".format(arr))
print("Searching for 20: {}".format(test_function([arr, -11])))
