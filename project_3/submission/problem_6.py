def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    current_min = None
    current_max = None

    for num in ints:
        if current_min is None or num <= current_min:
            current_min = num
        if current_max is None or num >= current_max:
            current_max = num

    return(current_min, current_max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("<< Test Cases >>")
print('\nMin:{} and Max:{} of array: {}'.format(*get_min_max(l), l))
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 25)]  # a list containing 0 - 9
random.shuffle(l)
print('\nMin:{} and Max:{} of array: {}'.format(*get_min_max(l), l))
print ("Pass" if ((0, 24) == get_min_max(l)) else "Fail")

l = [i for i in range(-5, 5)]  # a list containing 0 - 9
random.shuffle(l)
print('\nMin:{} and Max:{} of array: {}'.format(*get_min_max(l), l))
print ("Pass" if ((-5, 4) == get_min_max(l)) else "Fail")

l = [i for i in range(-10, -1)]  # a list containing 0 - 9
random.shuffle(l)
print('\nMin:{} and Max:{} of array: {}'.format(*get_min_max(l), l))
print ("Pass" if ((-10, -2) == get_min_max(l)) else "Fail")

l = []
random.shuffle(l)
print('\nMin:{} and Max:{} of array: {}'.format(*get_min_max(l), l))
print ("Pass" if ((None, None) == get_min_max(l)) else "Fail")
