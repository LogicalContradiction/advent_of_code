from pathlib import Path
from collections import deque



def readInput(input_filename):
	filepath = Path(__file__).parent / input_filename
	with open(filepath, "r", encoding="utf8", newline=None) as file:
			data = file.readlines()
	return data

def decode_starting_pos(init_pos):
	"""Takes the data and creates queues based on the starting location of each crate.
	
	Parameters:
		data (list<str>): List of strings representing the inital stacks of crates.
		
	Returns:
		list<deque>: List of deque objects where each deque represents the inital stacks."""
	result = []
	num_stacks = len(init_pos[-1]) // 4	#each stack uses 3 characters to represent it and a space separator
										#The last stack uses a \n separator
	#append empty lists for stacks
	for index in range(num_stacks):
		result.append(deque())
	#now fill the stacks
	for row in init_pos[:-1]:	#last line has the stack numbers, so ignore it
		curr_stack_index = 0
		#go through each position and add it to the deque
		for crate_index in range(1, len(row), 4):
			crate = row[crate_index]
			if crate != " ":
				result[curr_stack_index].appendleft(crate)
			curr_stack_index += 1
	return result

def decode_single_movement(move):
	"""Takes a single movement representation and converts it to a usable format.
	
	Parameters:
		move (str): A string representation of a sigle movement.
		
	Returns:
		int, int, int: Represents this movement. Format: (source, destination, amount)."""
	data = move.split(" ")
	amount = int(data[1])
	source = int(data[3])
	dest = int(data[5])
	return source, dest, amount

def decode_all_movements(all_moves):
	"""Takes the text of the crate movements and converts it to a usable format.
	
	Paramters:
		all_moves (list<str>): A list of string representations of the crate movements.
		
	Returns:
		list<tuples<int, int, int>>: A list of tuples representing the moves that will be made. Format: (source, destination, amount)."""
	result = []
	for move in all_moves:
		result.append(decode_single_movement(move))
	return result

def process_single_move(move, stacks):
	"""Moves a crate from its source to its destination.
	
	Parameters:
		move (tuple<int,int,int>): Represents the move that needs to be executed.
		stacks (list<deque>): The current state of the stacks.
		
	Returns:
		list (deque<str>): The same list as stacks."""
	source, dest, amount = move
	#subtract 1 from source and dest to convert from stack num to stack list index
	source_index = source - 1
	dest_index = dest - 1
	for crate_num in range(amount):
		crate = stacks[source_index].pop()
		stacks[dest_index].append(crate)
	return stacks

def get_top_crates_message(stacks):
	"""Gets the top crate from each stack and combines them to generate the solution message.
	
	Parameters:
		stacks (list<deque<str>>): Represents the state of the stacks.
		
	Returns:
		str: The top elements of each stack, combined into one string."""
	result = ""
	for stack in stacks:
		if len(stack) == 0:
			crate = " "
		else:
			crate = stack[-1]
		result = result + crate
	return result

def process_all_moves(moves, stacks):
	"""Moves all the crates in stacks accourding to the moves.
	
	Parameters:
		moves (int, int, int): Represents the movements of the crates.
		stacks (list<deque<str>>): Represents the current state of the stacks of crates.
		
	Returns:
		list<duque<str>>: The final state of the stacks. This is the same reference as stacks."""
	for move in moves:
		process_single_move(move, stacks)
	return stacks

def get_div_point_index_of_data(data):
	"""Calculates the index of the split point between the stack info and move list. Split point is a single string of just newline.
	
	Parameters:
		data (list<str>): List of strings that were read from the input.
	
	Returns:
		int: The integer of the single newline which is the breakpoint between the stacks info and the move list."""
	for index in range(len(data)):
		if data[index] == "\n":
			return index
	return -1

def do_simulation(data):
	"""Simulates moving the crates based off of the data.
	
	Parameters:
		data (list<str>): The input data to run this simulation based on.
		
	Returns:
		str: A string containing the crates on top of each stack."""
	div_point = get_div_point_index_of_data(data)
	stacks = decode_starting_pos(data[:div_point])
	moves = decode_all_movements(data[div_point+1:])
	process_all_moves(moves, stacks)
	result = get_top_crates_message(stacks)
	return result

def process_single_move_keep_order(move, stacks):
	"""Moves crates from one stack to another. In the case of multiple crates being moved at once, the order is preserved.
	
	Paramters:
		move (int, int, int): A tuple representing a move to be executed.
		stacks (list<deque<str>>): Represents the current state of the stacks of crates.
		
	Returns:
		list<deque<str>>: The same list as stacks."""
	source, dest, amount = move
	#convert stack num to stack index by subtracting 1
	source_index = source - 1
	dest_index = dest - 1
	temp = deque()
	for crate_index in range(amount):
		crate = stacks[source_index].pop()
		temp.appendleft(crate)
	#now add these items to the destination
	stacks[dest_index].extend(temp)
	return stacks

def process_all_moves_keep_order(moves, stacks):
	"""Moves all the crates in stacks accourding to the moves. Preserves order when moving multiple crates at once.
	
	Parameters:
		moves (int, int, int): Represents the movements of the crates.
		stacks (list<deque<str>>): Represents the current state of the stacks of crates.
		
	Returns:
		list<duque<str>>: The final state of the stacks. This is the same reference as stacks."""
	for move in moves:
		process_single_move_keep_order(move, stacks)
	return stacks

def do_simulation_preserve_order(data):
	"""Simulates moving the crates based off of the data. Will preserve order of crates when multiple are moved in a single step.
	
	Parameters:
		data (list<str>): The input data to run this simulation based on.
		
	Returns:
		str: A string containing the crates on top of each stack."""
	div_point = get_div_point_index_of_data(data)
	stacks = decode_starting_pos(data[:div_point])
	moves = decode_all_movements(data[div_point+1:])
	process_all_moves_keep_order(moves, stacks)
	result = get_top_crates_message(stacks)
	return result


def run_solution_1(filename):
	data = readInput(filename)
	message = do_simulation(data)
	print(f"You need to give the Elves the message '{message}'.")

def run_solution_2(filename):
	data = readInput(filename)
	message = do_simulation_preserve_order(data)
	print(f"The new message you have to give the Elves is '{message}'.")
