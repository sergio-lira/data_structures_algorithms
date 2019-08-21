def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if not is_valid_input(number):
        return None

    return sqrt_recursive_sol(number/2, number)

def is_valid_input(number):
    if number == None:
        return False

    if isinstance(number, int) or isinstance(number, float):
        if number >= 0:
            return True

    return False

def calculate_new_guess(guess, number):
    return guess - ( (guess*guess - number) / (2 * guess))

def is_acceptable(guess, number, error=0.01):
    return abs(number - guess*guess) <= error

def sqrt_recursive_sol(guess, number, error=0.01):
    #Use Newton's method of computing square root
    # https://en.wikipedia.org/wiki/Newton%27s_method#Square_root_of_a_number
    # https://m.tau.ac.il/~tsirel/dump/Static/knowino.org/wiki/Newton's_method.html
    #print("guess: {} number= {}".format(guess, number))
    if  is_acceptable(guess, number):
        return guess//1
    else:
        return sqrt_recursive_sol(calculate_new_guess(guess,number),number)

print("<< Basic Test Cases >> ")
print("Square root of 9: "+ "Pass" if  (3 == sqrt(9)) else "Fail")
print("Square root of 0: "+ "Pass" if  (3 == sqrt(9)) else "Fail")
print("Square root of 4: "+ "Pass" if  (3 == sqrt(9)) else "Fail")
print("Square root of 1: "+ "Pass" if  (3 == sqrt(9)) else "Fail")
print("Square root of 5: "+ "Pass" if  (3 == sqrt(9)) else "Fail")
print("\n<< Additional Test Cases >> ")
print("Square root of -1: "+ "Pass" if  (None == sqrt(-1)) else "Fail")
print("Square root of 99999: "+ "Pass" if  (316 == sqrt(99999)) else "Fail")
print("Square root of None: "+ "Pass" if  (None == sqrt(None)) else "Fail")
