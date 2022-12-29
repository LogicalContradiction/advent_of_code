from pathlib import Path
from collections import deque



def readInput(input_filename):
	filepath = Path(__file__).parent / input_filename
	with open(filepath, "r", encoding="utf8", newline=None) as file:
			data = file.readlines()
	return data

class MapNode:
	def __init__(self, elevation, init_col, init_row):
		if elevation == "S":
			self.elevation = "a"
			self.is_start = True
			self.is_end = False
			self.cost_to_reach = 0
		elif elevation == "E":
			self.elevation = "z"
			self.is_start = False
			self.is_end = True
			self.cost_to_reach = -1
		else:
			self.elevation = elevation
			self.is_start = False
			self.is_end = False
			self.cost_to_reach = -1
		self.col = init_col
		self.row = init_row
		self.prev_node = None
		self.visited = False

	def get_location(self):
		return self.row, self.col

def is_legal_move(node_move_from, node_go_to):
	"""Determines if moving from one node to the other is valid under the rules of part 1 of the puzzle (elevation is either +1 or down).
	
	Parameters:
		node_move_from (MapNode): The node you are moving from.
		node_go_to (MapNode): The node you are moving to.
		
	Returns:
		bool: True if this is a valid move, False if not."""
	elevation_from = ord(node_move_from.elevation)
	elevation_to = ord(node_go_to.elevation)
	elev_diff = elevation_to - elevation_from
	#diff should either by +1 (stepping up), or negavite (going down)
	if elev_diff <= 1:
		return True
	return False

def construct_path(end_node):
	"""Constructs the path taken, working backwards from the last node.
	
	Parameters:
		end_node (MapNode): The node you want the path to end on.
		
	Returns:
		list<MapNode>: The nodes visited in this path, in order."""
	path = deque()
	curr_node = end_node
	while not curr_node.is_start:
		path.appendleft(curr_node)
		curr_node = curr_node.prev_node
	#add the start node
	path.appendleft(curr_node)
	return list(path)

def create_map(map_data):
	"""Creates a map for use in the solution.
	
	Parameters:
		map_data (list<str>): A list of strings representing the map. The puzzle input.
		
	Returns:
		list<list<MapNode>>, MapNode, MapNode: A list of lists of MapNodes that represents the map, the start node, and the end node."""
	result_map = []
	start_node = None
	end_node = None
	for row_index in range(len(map_data)):
		curr_row = map_data[row_index].strip()
		result_map_row = []
		for col_index in range(len(curr_row)):
			node_elevation = curr_row[col_index]
			node = MapNode(node_elevation, col_index, row_index)
			if node.is_start:
				start_node = node
			elif node.is_end:
				end_node = node
			result_map_row.append(node)
		result_map.append(result_map_row)
	return result_map, start_node, end_node

def get_node_neighbors(height_map, node):
	"""Gets the neighbors in cardinal directions of a node.
	
	Parameters:
		height_map (list<list<MapNode>>): The heightmap that this node is a part of.
		node (MapNode): The node that we want the neighbors of.
		
	Returns:
		list<MapNode>: The neighbors of the node."""
	node_row = node.row
	node_col = node.col
	neighbors = []
	#left neighbor (row, col-1)
	if node_col-1 >= 0:
		neighbors.append(height_map[node_row][node_col-1])
	#up neighbor (row-1, col)
	if node_row-1 >= 0:
		neighbors.append(height_map[node_row-1][node_col])
	#right neighbor (row, col+1)
	if node_col+1 < len(height_map[node_row]):
		neighbors.append(height_map[node_row][node_col+1])
	#down neighbor (row+1, col)
	if node_row+1 < len(height_map):
		neighbors.append(height_map[node_row+1][node_col])
	return neighbors


def calculate_path(elevation_map, start_node, end_node):
	"""Uses Dijkstra's algorithm to construct shortest path from start node to end node.
	
	Parameters:
		elevation_map (list<list<MapNode>>): Represents the heightmap we want to get the path of.
		start_node (MapNode): The node that we start on.
		end_node (MapNode): The node we are trying to get to.
		
	Returns:
		MapNode: The end node we wanted to visit. Using this node, it is possible to reconstruct the path."""
	nodes_to_visit = deque()
	nodes_to_visit.append(start_node)
	while not end_node.visited and nodes_to_visit:
		#get current node
		curr_node = nodes_to_visit.popleft()
		if curr_node.visited:
			#skip this node since we've visited it already
			continue
		#get neighbors
		neighbors = get_node_neighbors(elevation_map, curr_node)
		for neighbor_node in neighbors:
			if is_legal_move(curr_node, neighbor_node):
				if neighbor_node.cost_to_reach == -1 or curr_node.cost_to_reach + 1 < neighbor_node.cost_to_reach:
					neighbor_node.prev_node = curr_node
					neighbor_node.cost_to_reach = curr_node.cost_to_reach + 1
					nodes_to_visit.append(neighbor_node)
		#mark node as visited
		curr_node.visited = True
	return end_node

def get_all_nodes_of_height(height_map, desired_elevation):
	"""Gets all the nodes of a desired height from the map.
	
	Parameters:
		height_map (list<MapNode>): The height map.
		desired_elevation (str): A single-character string representing the elevation we wanted all the nodes of.
		
	Returns:
		list<MapNode>: All of the nodes that have the desired elevation."""
	result = []
	for row in height_map:
		for node in row:
			if node.elevation == desired_elevation:
				result.append(node)
	return result

def reset_map_and_set_new_start(height_map, old_start, new_start):
	"""Resets the height map and sets a new start node.
	
	Parameters:
		height_map (list<list<MapNode>>): The height map.
		old_start (MapNode): The old starting node.
		new_start (MapNode): The new starting node.
		
	Returns:
		list<list<MapNode>>: The newly-reset map."""
	for row in height_map:
		for node in row:
			if node == new_start:
				node.is_start = True
				node.cost_to_reach = 0
			else:
				node.cost_to_reach = -1
			if node == old_start:
				node.is_start = False
			node.visited = False
			node.prev_node = None
	return height_map

def get_shortest_path(height_map, start_node, end_node):
	"""Gets the shortest path between the start node and the end node.
	
	Parameters:
		height_map <list<list<MapNode>>): The height map.
		start_node (MapNode): The starting node of the path.
		end_node (MapNode): The ending node of the path.
		
	Returns:
		int: The sortest distance between the start node and end node, or -1 if it's impossible."""
	final_node = calculate_path(height_map, start_node, end_node)
	num_steps = final_node.cost_to_reach
	return num_steps
	
def get_shortest_path_all_possible_starts(map_data):
	"""Gets the shorest path from all possible starting points to the endpoint.
	
	Parameters:
		map_data (list<str>): The map data (puzzle input).
	
	Returns:
		int: The distance of the shortest path from a set of starting points to the end point."""
	height_map, start_node, end_node = create_map(map_data)
	possible_start_nodes = get_all_nodes_of_height(height_map, "a")
	shortest_num_steps = get_shortest_path(height_map, start_node, end_node)
	old_start_node = start_node
	for new_start_node in possible_start_nodes:
		if new_start_node == start_node:
			continue
		reset_map_and_set_new_start(height_map, old_start_node, new_start_node)
		num_steps = get_shortest_path(height_map, new_start_node, end_node)
		old_start_node = new_start_node
		if num_steps != -1 and num_steps < shortest_num_steps:
			shortest_num_steps = num_steps
	return shortest_num_steps


def run_solution_1(filename):
	map_data = readInput(filename)
	height_map, start_node, end_node = create_map(map_data)
	num_steps = get_shortest_path(height_map, start_node, end_node)
	print(f"The fewest steps needed to move from current position to the best signal location are {num_steps} steps.")

def run_solution_2(filename):
	map_data = readInput(filename)
	num_steps = get_shortest_path_all_possible_starts(map_data)
	print(f"Out of all possible starting points, the number of steps needed to walk the shortest path are {num_steps} steps.")
	

