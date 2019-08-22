def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return 0, 0

    #Sorting the elements with merge sort is done in O(nlogn)
    sorted_number = mergesort(input_list)
    number_1 = 0
    number_2 = 0

    #We use the sorted list as a stack and pop the largest element from the end to create our
    #two numbers that sum to the maximun possible
    while len(sorted_number):

        n_1 = sorted_number.pop()

        if len(sorted_number):
            n_2 = sorted_number.pop()
        else:
            n_2 = 0

        if n_1:
            number_1 *= 10
        number_1 += n_1

        if n_2:
            number_2 *= 10
        number_2 += n_2

    return [number_1, number_2]


#Merge Sort methods learned from the sorting algorithms section
def mergesort(items):

    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def test_function(test_case):
    print("Input: {}".format(test_case[0]))
    output = rearrange_digits(test_case[0])
    print("Output: {}".format(output))
    solution = test_case[1]
    print("Solution: {}".format(solution))
    if sum(output) == sum(solution):
        print("Pass\n")
    else:
        print("Fail\n")

print("<< Test Cases >>")
test_case = [[3, 4, 5, 1, 2,], [542, 31]]
test_function(test_case)

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_case = [[4, 6], [4, 6]]
test_function(test_case)

test_case = [[1], [1, 0]]
test_function(test_case)

test_case = [[5, 5, 5, 5, 5, 5, 5], [5555, 555]]
test_function(test_case)

test_case = [[], [0, 0]]
test_function(test_case)

test_case = [[0,0,0,0,0,0], [0, 0]]
test_function(test_case)
