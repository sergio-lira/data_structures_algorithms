def sort_012(arr):
    next_pos_0 = 0
    next_pos_2 = len(arr) - 1

    index = 0

    while index <= next_pos_2:

        if arr[index] == 0:
            arr[next_pos_0], arr[index] = arr[index], arr[next_pos_0]
            next_pos_0 += 1
            index += 1

        elif arr[index] == 2:
            arr[next_pos_2], arr[index] = arr[index], arr[next_pos_2]
            next_pos_2 -= 1

        else:
            index += 1
    return arr


def test_function(test_case):
    print("Test Case: {}".format(test_case))
    sorted_array = sort_012(test_case)
    print("Result: {}".format(sorted_array))
    if sorted_array == sorted(test_case):
        print("Pass\n")
    else:
        print("Fail\n")

print('<< Test Cases >>\n')
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1])
test_function([2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2])
test_function([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
test_function([0, 1, 2])
test_function([])
