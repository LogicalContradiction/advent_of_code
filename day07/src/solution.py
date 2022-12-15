from pathlib import Path



def readInput(input_filename):
	filepath = Path(__file__).parent / input_filename
	with open(filepath, "r", encoding="utf8", newline=None) as file:
			data = file.readlines()
	return data

def process_ls(commands, command_index):
	"""Called to process the terminal output after the user executes the 'ls' command.
	
	Parameters:
		commands (list<str>): List of strings representing the terminal commands and output.
		command_index (int): The index into the commands list of the 'ls' command that is being processed.
		
	Returns:
		int, int, int: The sum of all the files in this directory (does not include other directories), the number of directories in this directory, the next index to be processed."""
	sum_file_size = 0
	num_dirs = 0

	command_index += 1
	#the next command we entered has the line start with '$'
	while command_index < len(commands) and commands[command_index][0] != "$":
		line = commands[command_index].split()
		#directories will have "dir" as the first part 
		if line[0] == "dir":
			num_dirs += 1
		else:
			#otherwise it's a file with a size
			sum_file_size += int(line[0])
		command_index += 1
	return sum_file_size, num_dirs, command_index

def process_cd(commands, command_index, max_dir_size, large_files):
	"""Called to process the terminal output after the user executes the 'cd' command.
	
	Parameters:
		commands (list<str>): List of strings representing the terminal commands and output.
		command_index (int): The index into the commands list of the current 'cd' command that is being processed.
		max_dir_size (int): The maximum size of a directory that should be recorded in large_files. If -1 is specified, it will save the size of all directories to large_files.
		large_files (list<int>): List of filesizes that are less than max_dir_size.

	Returns:
		int, int: The index of the next command to be processed, and the size of the directory"""
	#otherwise this is a valid directory, so process it.
	this_dir_sum, num_dir_remain, next_command_index = process_ls(commands, command_index+1)
	#now process each of the sub-directories
	while num_dir_remain > 0:
		#increment next_command_index to get the next command
		next_command_index, dir_size = process_cd(commands, next_command_index, max_dir_size, large_files)
		#now increment the size of this directory
		this_dir_sum += dir_size
		#decrement counter
		num_dir_remain -= 1
	#all sub-directories have been processed. Check if this directory qualifies for the large_files
	if this_dir_sum <= max_dir_size or max_dir_size == -1:
		large_files.append(this_dir_sum)
	#the next command is '$ cd ..' to leave this directory, so return and skip this command
	return next_command_index+1, this_dir_sum

def get_all_dir_sizes_less_than_size(commands, max_dir_size):
	"""Processes the terminal output and gets sizes of all the directories that are less than max_size.
	
	Parameters:
		commands (list<str>): The terminal output.
		max_dir_size (int): The maximum size of a directory to be included in the result.
		
	Returns:
		list<int>: A list containing the size of every directory that is less than the provided max_size."""
	command_index = 0
	large_files = []
	process_cd(commands, command_index, max_dir_size, large_files)
	return large_files

def get_sum_of_dir_less_than_size(commands, max_dir_size):
	""""Processes the terminal output and gets the sum of the sizes of directories that are smaller than max_dir_size.
	
	Parameters:
		commands (list<str>): The terminal output.
		max_dir_size (int): The maximum size of a directory to be considered in this sum.
		
	Returns:
		int: The sum of the directory sizes that are less than max_dir_size."""
	large_files = get_all_dir_sizes_less_than_size(commands, max_dir_size)
	total_sum = 0
	for dir_size in large_files:
		total_sum += dir_size
	return total_sum

def get_size_of_all_directories(commands):
	"""Gets the size of all directories.
	
	Parameters:
		commands (list<str>): The terminal output.
		
	Returns:
		list<int>, int: A list of all the sizes of the directories in commands, and the total size of the filesystem in use."""
	large_files = []
	command_index = 0
	next_command, total_size_in_use = process_cd(commands, command_index, -1, large_files)
	return large_files, total_size_in_use

def calcuate_min_space_to_free_to_run_update(filesys_size, space_needed, used_space):
	"""Calculates the minimum amount of space needed to be freed to run an update of the given size.
	
	Parameters:
		filesys_size (int): The total size of the file system.
		space_needed (int): The amount of space needed to run this update.
		used_space (int): The amount of space that is currently in use.
		
	Returns:
		int: The amount of space needed to be freed to run an update of the given size."""
	space_free = filesys_size - used_space
	min_space_to_free = space_needed - space_free
	return min_space_to_free

def remove_dirs_smaller_than_size(files, min_size):
	"""Removes the directories that are less than the provided size from files.
	
	Parameters:
		files (list<int>): The sizes of the files we are looking through.
		min_size (int): The minimum size of directory needed to be kept.
	
	Returns:
		list<int>: A list where every element is greater than or equal to min_size."""
	larger_files = []
	for file_size in files:
		if file_size >= min_size:
			larger_files.append(file_size)
	return larger_files

def get_min_dir_size_to_delete_to_update(commands, free_space_needed, filesys_size):
	"""Gets the minimum size of directory needed to be deleteed to allow the update to run.
	
	Parameters:
		commands (list<str>): The terminal output.
		free_space_needed (int): The amount of free space that is required for the update to run.
		filesys_size (int): The total size of the filesystem.
		
	Returns:
		int: The minimum size of the directory that needs to be deleted in order to run the update."""
	all_dir_sizes, total_size_in_use = get_size_of_all_directories(commands)
	min_space_need_to_free = calcuate_min_space_to_free_to_run_update(filesys_size, free_space_needed, total_size_in_use)
	dir_larger_than_needed = remove_dirs_smaller_than_size(all_dir_sizes, min_space_need_to_free)
	min_dir_size_to_delete = min(dir_larger_than_needed)
	return min_dir_size_to_delete

	
def run_solution_1(filename):
	data = readInput(filename)
	max_dir_size = 100000
	total_sum = get_sum_of_dir_less_than_size(data, max_dir_size)
	print(f"The sum of all directories smaller than {max_dir_size} is {total_sum}.")

def run_solution_2(filename):
	data = readInput(filename)
	filesys_size = 70000000
	free_space_needed = 30000000
	dir_size_to_delete = get_min_dir_size_to_delete_to_update(data, free_space_needed, filesys_size)
	print(f"The minimum size of directory to delete to run this update is {dir_size_to_delete}.")

