files = [] 
# create an empty list to store targeted filename. 
# This line should be put outside of def find_files(), or
# it will be cleared at each iteration.
def find_files(path,suffix):
    for i in os.listdir(path):
        new_path = os.path.join(path,i)
        if os.path.isfile(new_path) and new_path.endswith(suffix):
            files.append(new_path)
        elif os.path.isdir(new_path):
            find_files(new_path,suffix)                    
    return files
# Test:
find_files('root','.c')

# return:
'''
['root/subdir5/a.c',
 'root/subdir3/subsubdir1/b.c',
 'root/subdir1/a.c',
 'root/t1.c']

'''
