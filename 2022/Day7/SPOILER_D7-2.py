import sys
file = open(sys.argv[1], 'r')

# Class
class Directory :
    # Variables
    root = False
    parent = ''
    total_size = 0

    # Methods
    def __init__(self, root, parent, size) :
        self.root = root
        self.parent = parent
        self.total_size = size

    def get_parent(self) :
        return self.parent
    def get_size(self) :
        return self.total_size
    def is_root(self) :
        return self.root
    def set_parent(self, parent) :
        self.parent = parent
    def add_size(self, plus_size) :
        self.total_size += plus_size

# Parsing and creating the file system
directories = []
root = Directory(True, None, 0) # Initialization
directories.append(root)
current_dir = root
for line in file :
    line = line.split()
    # Different cases : command, directory, file
    # If it's a command
    if line[0] == "$" :
        if line[1] == "cd" :
            # If it's the root
            if line[2] == "/" :
                current_dir = root
            # If it's the parent
            elif line[2] == ".." :
                if current_dir.is_root() :
                    print("ERROR : Already at the root")
                else :
                    current_dir = current_dir.get_parent()
            # If it's a new directory
            else :
                new_dir = Directory(False, current_dir, 0)
                current_dir = new_dir
                directories.append(new_dir)

    # If it's a directory
    elif line[0] == "dir" :
        pass

    # If it's a file
    else :
        file_size = int(line[0])
        current_dir.add_size(file_size)

# Adding the sizes to their parent directories
directories.reverse() # Putting the tree leaves first
for directory in directories :
    if directory.get_parent() != None :
        directory.get_parent().add_size(directory.get_size())

# Finding the right directory to delete
space_taken = directories[-1].get_size()
max_size = 70000000 - 30000000
if space_taken < max_size :
    print("How amazing, there's nothing to delete !")
else :
    smallest = space_taken
    for directory in directories :
        if space_taken - directory.get_size() <= max_size :
            smallest = min(smallest, directory.get_size())
    print(smallest)