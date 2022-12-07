import os
import numpy as np

# load txt file as list:
with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    input = f.readlines()

def expand_dirs(path_key, dirs):
    # function that expands the list of files in subdirectories using the subdir path as dict key
    files = []
    items = dirs[path_key]
    for i in items:
        if type(i) == str:
            # i is a subdir
            subdir = '/'.join([path_key, i])
            # recursion for subdir:
            files_add = expand_dirs(subdir, dirs)
            for f in files_add:
                files.append(f)
        else:
            # i is a file
            files.append(i)
    return files

def get_dir_dict(input):
    # function that creates a dictionary file tree from given input command lines

    # modify input list
    lines = [i.replace('\n','').strip() for i in input]

    # keeping track of the file structure in form of a dict, with keys representing
    # file directories, and values being subdirs or files
    dirs = {}

    # keeping track of path as a list of strings, as subdirs can have the same name in 
    # different parts of the file tree.
    path = []

    for l in lines:
        if l.startswith('$ cd'):
            # go deeper or shallower in dir tree
            if l.endswith('cd ..'):
                # go shallower
                path.pop()
            else:
                # go deeper in subdir
                current_dir = l.replace('$ cd', '').strip()
                path.append(current_dir)
                # cd into new subdirectory, create new dict entry:
                dirs['/'.join(path)] = []
        elif l.startswith('$ ls'):
            # calls list of files
            pass
        else:
            if l.startswith('dir'):
                # append a subdir (string) to the value list of this dir
                dirs['/'.join(path)].append(l.split(' ')[1].strip())
            else:
                # append a file (list of name and size) to the value list of this dir
                size, file = l.split(' ')
                dirs['/'.join(path)].append([file,size])
    return dirs

### part 1 ###
def part1(input):
    # function to solve part 1, sum of all subdir sizes smaller or equal 100000:
    dirs = get_dir_dict(input)

    total_size = 0
    dirs_check = []
    
    for key, val in dirs.items():
        # expand all subdirs of this dir into a list of files:
        ff = expand_dirs(key, dirs)

        # create list of all file sizes in this subdir
        sizes = [int(f[1]) for f in ff]

        # add up if smaller 100000
        if sum(sizes) <= 100000:
            total_size += sum(sizes)
    
    return total_size

print(f'answer 1: {part1(input)}')

### part 2 ###
def part2(input):
    dirs = get_dir_dict(input)

    total_available = 70000000
    total_needed = 30000000

    # get current free space by checking root dir size
    root = expand_dirs('/', dirs)
    root_sizes = [int(f[1]) for f in root]
    current_free = total_available - sum(root_sizes)

    target_size = total_needed - current_free
    min_size = np.inf

    for key, val in dirs.items():
        # expand all subdirs in this dir into the containing files
        ff = expand_dirs(key, dirs)
        sizes = [int(f[1]) for f in ff]

        if min_size > sum(sizes) > target_size:
            # if this dir has the right size, set the new min_size
            min_size = sum(sizes)

    return min_size

print(f'answer 2: {part2(input)}')
