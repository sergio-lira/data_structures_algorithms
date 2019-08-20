import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    result_set = list()

    recursive_search(suffix, path, result_set)

    return result_set

def recursive_search(suffix, path, results):
    if os.path.isfile(path):
        if path.endswith(suffix):
            results.append(path)
        else:
            return
    elif os.path.isdir(path):
        items = os.listdir(path)
        for item in items:
                recursive_search(suffix, os.path.join(path, item), results)
    else:
        print("Error: this path does not exist!")
        return

print('\n<<< Test Case 1 >>>\nSearching for .h')
print(find_files(".h", "."))
"""Expected result:
['.\\testdir\\subdir1\\a.h',
 '.\\testdir\\subdir3\\subsubdir1\\b.h',
 '.\\testdir\\subdir5\\a.h',
 '.\\testdir\\t1.h']"""

print('\n<<< Test Case 2 >>>\nSearching for .c')
print(find_files(".c", "."))
"""['.\\testdir\\subdir1\\a.c',
 '.\\testdir\\subdir3\\subsubdir1\\b.c',
 '.\\testdir\\subdir5\\a.c',
 '.\\testdir\\t1.c']"""

print('\n<<< Test Case 3 >>>\nSearching for .f')
print(find_files(".f", "."))
#Expected empty set as result

print('\n<<< Test Case 4 >>>\nSearching for t1.c')
print(find_files('t1.c', "."))
#Expected a single match

print('\n<<< Test Case 5 >>>\nSearching for *.*')
print(find_files("*.*", "."))
#Expected empty set, I was trying to mess around with the .endswith function

print('\n<<< Test Case 6 >>>\nSearching for path that does not exist')
print(find_files("*.*", "not_a_path/"))
#Expected empty set, I was trying to mess around with the .endswith function
