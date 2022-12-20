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

def get_num_trees_visible_row(row, tree_index):
	"""Counts the number of trees visible in the same row to the left and right of the current tree.
	
	Parameters:
		row (str): Representation of the current row being checked.
		tree_index (int): The index of the tree that is being checked.
		
	Returns:
		int, int: The number of trees that can be seen to the left and right of the current tree, respectively."""
	tree_height = row[tree_index]
	#count left side first
	left = 0
	for index in range(tree_index-1, -1, -1):
		curr_tree_height = row[index]
		left += 1
		if curr_tree_height >= tree_height:
			break
	#now right
	right = 0
	for index in range(tree_index+1, len(row), 1):
		curr_tree_height = row[index]
		right += 1
		if curr_tree_height >= tree_height:
			break
	return left, right

def get_num_trees_visible_col(trees, col_index, tree_to_check_row_index):
	"""Counts the number of trees visible in the same column to the above and below the current tree.
	
	Parameters:
		trees (list<str>): Representation of the current tree heights.
		col_index (int): The column index of the column of trees to be checked.
		tree_to_check_row_index (int): 
		
	Returns:
		int, int: The number of trees that can be seen above and below the current tree, respectively."""
	tree_height = trees[tree_to_check_row_index][col_index]
	#count above side first
	above = 0
	for row_index in range(tree_to_check_row_index-1, -1, -1):
		curr_tree_height = trees[row_index][col_index]
		above += 1
		if curr_tree_height >= tree_height:
			break
	#now below
	below = 0
	for row_index in range(tree_to_check_row_index+1, len(trees), 1):
		curr_tree_height = trees[row_index][col_index]
		below += 1
		if curr_tree_height >= tree_height:
			break
	return above, below

def calculate_scenic_score(vd_left, vd_right, vd_up, vd_down):
	"""Calculates the viewing distance of a tree given the viewing distance in each cardinal direction.
	
	Parameters:
		vd_left (int): The number of trees (viewing distance) in the left direction.
		vd_right (int): The number of trees (viewing distance) in the right direction.
		vd_up (int): The number of trees (viewing distance) in the up direction.
		vd_down (int): The number of trees (viewing distance) in the down direction.
	
	Returns:
		int: The scenic score of a tree that has the given viewing distances. Found by mulitplying the four viewing distances together."""
	return vd_left * vd_right * vd_up * vd_down

def calculate_scenic_score_of_tree(trees, tree_row_index, tree_col_index):
	"""Calculates the scenic score of the tree at the given index.
	
	Parameters:
		trees (list<str>): The representation of the grid of trees.
		tree_row_index (int): The row index of the tree you want the scenic score of.
		tree_col_index (int): The column index of the tree you want the scenic score of."""
	vd_left, vd_right = get_num_trees_visible_row(trees[tree_row_index], tree_col_index)
	vd_up, vd_down = get_num_trees_visible_col(trees, tree_col_index, tree_row_index)
	scenic_score = calculate_scenic_score(vd_left, vd_right, vd_up, vd_down)
	return scenic_score

def get_highest_scenic_score(trees):
	max_scenic_score = 0
	num_rows = len(trees)
	num_cols = len(trees[0])

	for row_index in range(num_rows):
		for col_index in range(num_cols):
			curr_scenic_score = calculate_scenic_score_of_tree(trees, row_index, col_index)
			if curr_scenic_score > max_scenic_score:
				max_scenic_score = curr_scenic_score
	return max_scenic_score


def run_solution_1(filename):
	data = readInput(filename)
	trees = strip_newlines(data)
	num_visible = get_num_visible_trees(trees)
	print(f"The number of trees visible from at least one direction are {num_visible} trees.")

def run_solution_2(filename):
	data = readInput(filename)
	trees = strip_newlines(data)
	max_scenic_score = get_highest_scenic_score(trees)
	print(f"The maximum scenic score of this grid of trees is {max_scenic_score}.")