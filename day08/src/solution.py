from pathlib import Path



def readInput(input_filename):
	filepath = Path(__file__).parent / input_filename
	with open(filepath, "r", encoding="utf8", newline=None) as file:
			data = file.readlines()
	return data

def strip_newlines(data):
	"""Used to strip the newline character from the end of each string in the data list.
	
	Parameters:
		data (list<str>): List of strings to remove the newlines from.
		
	Returns:
		list<str>: A reference to the list with the new strings."""
	result = []
	for line in data:
		result.append(line.strip())
	return result

def is_visible_row_test(row, tree_to_check_index):
	"""Used to check if the tree at the given index is visible. If all the other trees between this one and the edges are shorter, the tree is visible.
	
	Parameters:
		row (str): A string representing the height of each tree in the row.
		tree_to_check_index (int): The index of the tree we are checking to see if it's visible.
		
	Returns:
		bool: True if the tree is visible (all other trees in row are shorter), or False if it is not."""
	if tree_to_check_index == 0 or tree_to_check_index == len(row)-1:
		#if this is the outside edges, it is visible no matter what
		return True
	tree_to_check_height = row[tree_to_check_index]
	visible = True
	#check left side first
	for index in range(tree_to_check_index):
		curr_tree_height = row[index]
		if curr_tree_height >= tree_to_check_height:
			visible = False
			break
	if visible:
		return True
	visible = True
	#check right side
	for index in range(tree_to_check_index+1, len(row), 1):
		curr_tree_height = row[index]
		if curr_tree_height >= tree_to_check_height:
			visible = False
			break
	if visible:
		return True
	return False


def is_visible_col_test(data, col_index, tree_to_check_row_index):
	"""Used to check if the tree at the given index is visible. If all the other trees between this one and the edges are shorter, the tree is visible.
	
	Parameters:
		data (list<str>): The grid of trees.
		col_index (int): The column index of trees that is being checked.
		tree_to_check_row_index (int): The row index of the tree we are checking to see if it's visible.
		
	Returns:
		bool: True if the tree is visible (all other trees in the column are shorter), or False if it is not."""
	if tree_to_check_row_index == 0 or tree_to_check_row_index == len(data)-1:
		#the two trees on the outside edges of the column are always visible
		return True
	tree_to_check_height = data[tree_to_check_row_index][col_index]
	visible = True
	#check topside first
	for index in range(tree_to_check_row_index):
		curr_tree_height = data[index][col_index]
		if curr_tree_height >= tree_to_check_height:
			visible = False
			break
	if visible:
		return True
	visible = True
	for index in range(tree_to_check_row_index+1, len(data), 1):
		curr_tree_height = data[index][col_index]
		if curr_tree_height >= tree_to_check_height:
			visible = False
			break
	if visible:
		return True
	return False

def get_num_visible_trees(trees):
	"""Counts the number of visible trees in this grid of trees. A tree is visible if there are no other trees in the same row or column that are as tall as, or taller than it.
	
	Parameters:
		trees (list<str>): A list of tree heights that represents the current height of the trees.
		
	Returns:
		int: The number of trees that are visible."""
	tree_grid_num_rows = len(trees)
	tree_grid_num_cols = len(trees[0])
	num_visible = (2*tree_grid_num_rows) + (2*tree_grid_num_cols) - 4 #subtract 4 to avoid counting corners twice
	#check every tree except the ones on the outside of the grid
	for row_index in range(1, tree_grid_num_rows-1, 1):
		for col_index in range(1, tree_grid_num_cols-1, 1):
			if is_visible_row_test(trees[row_index], col_index) or is_visible_col_test(trees, col_index, row_index):
				num_visible += 1
	return num_visible

def run_solution_1(filename):
	data = readInput(filename)
	trees = strip_newlines(data)
	num_visible = get_num_visible_trees(trees)
	print(f"The number of trees visible from at least one direction are {num_visible} trees.")