# The key here is to distinguish between a file name and a directory name.
# If it's a file name, then just return the filename, however, if we encountered a directory name, 
#we should dive into that directory and search for new file names. Thus, recursion should be used if
#we come across a directory name.
# Given this, if .isfile is true, we append the file name into the output list
# if .isdir is true, we recursively do the find_files() function again to dive deep, using the new pathway


import os

files = []
# create an empty list to store targeted filename. 
# This line should be put outside of def find_files(), or
# it will be cleared at each iteration.
def find_files(path,suffix):
    
    # add edge case for null path
    # ref: https://thispointer.com/python-how-to-check-if-a-directory-is-empty/
    if not os.path.exists(path):
        print("\nCurrent directory doesn't exist!")
    else:
        for i in os.listdir(path):

            new_path = os.path.join(path,i)
            if os.path.isfile(new_path) and new_path.endswith(suffix):
                #print("files appending...")
                files.append(new_path)

            elif os.path.isdir(new_path):
                #print("recursing...")
                find_files(new_path,suffix)
        return files
        
# Test case 1:
files = []
test1 = find_files('root','.c')
print("test1: ", test1)
# return:
#test1: 
#['root/test1.c', 'root/subdir1/subdir4_under_1/test3.c', 'root/subdir1/test2.c']

# Test case 2:
files = []
test2 = find_files('root2','.c')
print("test2: ", test2)
# return:
#test2:  \
#['root2/test1.c', 'root2/subdir1/subdir4_under_1/test3.c', 'root2/subdir1/test2.c']


# Test case 3:
files = []
test3 = find_files('root2','.h')
print("test3: ", test3)
# return:
# test3:
#['root2/subdir3/test3.h', 'root2/subdir1/subdir4_under_1/test2.h', 'root2/test2.h']

# Test case 4, when directory is null:
files = []
test4 = find_files('root3','.h')
print("test4: ", test4)
# return:
#Current directory doesn't exist!
#test4:  None

# Test case 5, when file extension is invalid:
files = []
test5 = find_files('root','.xls')
print("test5: ", test5)
# return:
#test5:  []