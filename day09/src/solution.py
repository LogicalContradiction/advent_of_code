from pathlib import Path



class RopeNode:
	def __init__(self, init_x, init_y):
		self.x = init_x
		self.y = init_y

	def get_location(self):
		return (self.x, self.y)


def readInput(input_filename):
	filepath = Path(__file__).parent / input_filename
	with open(filepath, "r", encoding="utf8", newline=None) as file:
			data = file.readlines()
	return data

def is_head_touching_tail(head, tail):
	"""Used to check if the tail of the rope is in a valid position (touching the head).
	
	Parameters:
		head (RopeNode): An object representing the head of the rope.
		tail (RopeNode): An object representing the head of the rope.
		
	Returns:
		bool: True if the tail is in a valid position, False otherwise."""
	diff_x = abs(head.x - tail.x)
	diff_y = abs(head.y - tail.y)
	return (diff_x == 0 or diff_x == 1) and (diff_y == 0 or diff_y == 1)

def move_rope_node_up(node):
	"""Moves the rope node up by 1.
	
	Parameters:
		node (RopeNode): The rope node to move up one.
		
	Returns:
		RopeNode: The same rope node, but moved up in the y direction by 1."""
	node.y += 1
	return node

def move_rope_node_down(node):
	"""Moves the rope node down by 1.
	
	Parameters:
		node (RopeNode): The rope node to move down one.
		
	Returns:
		RopeNode: The same rope node, but moved down in the y direction by 1."""
	node.y -= 1
	return node

def move_rope_node_left(node):
	"""Moves the rope node left by 1.
	
	Parameters:
		node (RopeNode): The rope node to move left one.
		
	Returns:
		RopeNode: The same rope node, but moved left in the x direction by 1."""
	node.x -= 1
	return node

def move_rope_node_right(node):
	"""Moves the rope node right by 1.
	
	Parameters:
		node (RopeNode): The rope node to move right one.
		
	Returns:
		RopeNode: The same rope node, but moved right in the x direction by 1."""
	node.x += 1
	return node

def move_tail_towards_head(head, tail):
	"""Moves the tail towards the head in the case of the head being too far away from the tail.
	
	Parameters:
		head (RopeNode): Represents the head of the rope.
		tail (RopeNode): Represents the tail of the rope.
		
	Returns:
		RopeNode: A reference to the tail."""
	#first check if they're in the same row
	if head.y == tail.y:
		#same row, move tail towards the head
		if head.x > tail.x:
			move_rope_node_right(tail)
		else:
			move_rope_node_left(tail)
	#check if they're in the same column
	elif head.x == tail.x:
		#same column, move tail towards head
		if head.y > tail.y:
			move_rope_node_up(tail)
		else:
			move_rope_node_down(tail)
	#it's diagonal, so move diagonally towards the head
	else:
		#horizontal movement
		if head.x > tail.x:
			move_rope_node_right(tail)
		else:
			move_rope_node_left(tail)
		#vertical movement
		if head.y > tail.y:
			move_rope_node_up(tail)
		else:
			move_rope_node_down(tail)
	return tail

def process_move_set(head, tail, visited, direction, num_moves):
	"""Process a set of moves in a given direction.
	
	Parameters:
		head (RopeNode): Represents the head of the rope.
		tail (RopeNode): Represents the tail of the rope.
		visited (dict): Keeps track of the nodes that the tail has visited.
		direction (str): Single character string representing the direction the head moves.
		num_moves (int): The number of spaces to move the head.
		
	Returns:
		None"""
	for counter in range(num_moves):
		#first move the head
		if direction == "U":
			move_rope_node_up(head)
		elif direction == "D":
			move_rope_node_down(head)
		elif direction == "L":
			move_rope_node_left(head)
		else:
			move_rope_node_right(head)
		#now check the position of the tail
		if not is_head_touching_tail(head, tail):
			#head isn't touching tail, so move it
			move_tail_towards_head(head, tail)
			#now mark this location as visited
			location = tail.get_location()
			visited[str(location)] = True
		#we don't need to move the tail, so just exit

def process_all_move_sets(moves, head, tail, visited):
	"""Processes all moves and marks visited with the locations that have been visited by the tail.
	
	Paramters:
		moves (list<str>): Represents all of the moves that need to be processed.
		head (RopeNode): The head of this rope.
		tail (RopeNode): The tail of this rope.
		visited (dict): The unique locations that the tail has already visited.
		
	Returns:
		dict: A reference to the unique nodes visited."""
	for move in moves:
		split_moves = move.split()
		direction = split_moves[0]
		num_moves = int(split_moves[1])
		process_move_set(head, tail, visited, direction, num_moves)
	return visited

def calculate_num_unique_locations_tail_visits(moves):
	"""Calculates the number of unique locations the tail of a rope will visit given this set of moves.
	
	Parameters:
		moves (list<str>): Represents all of the moves the head will make.
		
	Returns:
		int: The number of unique locations visted by the tail of a rope if the given set of moves is followed."""
	head = RopeNode(0, 0)
	tail = RopeNode(0, 0)
	visited = {}
	#explicitly add the origin as a location the tail visits
	visited[str(tail.get_location())] = True
	process_all_move_sets(moves, head, tail, visited)
	return len(visited.keys())


def run_solution_1(filename):
	moves = readInput(filename)
	num_locations = calculate_num_unique_locations_tail_visits(moves)
	print(f"The tail visits {num_locations} positions at least once.")
