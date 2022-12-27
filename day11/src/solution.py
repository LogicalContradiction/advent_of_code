from pathlib import Path
from collections import deque
import operator
import math



def readInput(input_filename):
	filepath = Path(__file__).parent / input_filename
	with open(filepath, "r", encoding="utf8", newline=None) as file:
			data = file.readlines()
	return data

class Monkey:
	def __init__(self, init_id, init_items, worry_operator, other_operator, test_divisor, divisor_true, divisor_false, mod_decrease_value=1):
		self.num_inspections = 0
		self.id = init_id
		self.items = deque(init_items)
		if worry_operator == "*":
			self.operation = operator.mul
		else:
			self.operation = operator.add
		if other_operator != None:
			self.other_operator = other_operator
			self.use_worry_as_other_operator = False
		else:
			self.use_worry_as_other_operator = True
		self.test_divisor = test_divisor
		self.divisor_true = divisor_true
		self.divisor_false = divisor_false
		self.mod_decrease_value = mod_decrease_value

	def inspect(self, worry_decreasing_factor=3):
		"""The monkey takes the first item in its list and inspects it, changing the worry value to a new one based on the operation.
		
		Parameters:
			worry_decreasing_factor (int): The factor your worry is divided by after inspection (default=3).
		
		Returns:
			int: The new worry level of the item, or -1 if the monkey is holding no other items."""
		if not self.items:
			return -1
		self.num_inspections += 1
		worry_value = self.items.popleft()
		if self.use_worry_as_other_operator:
			worry_value = self.operation(worry_value, worry_value)
			if worry_decreasing_factor != 1:
				worry_value = math.floor(worry_value / worry_decreasing_factor)
		else:
			worry_value = self.operation(worry_value, self.other_operator)
			if worry_decreasing_factor != 1:
				worry_value = math.floor(worry_value / worry_decreasing_factor)
		if self.mod_decrease_value != 1:
			return worry_value % self.mod_decrease_value
		return worry_value

	def get_monkey_id_to_throw_to(self, worry_level):
		"""Gets the id of the monkey to throw the item to based on the worry level.
		
		Parameters:
			worry_level (int): The id of the item that will be thrown.
		
		Returns:
			int: The id of the monkey that this item will be thrown to."""
		if worry_level % self.test_divisor == 0:
			return self.divisor_true
		return self.divisor_false

	def do_single_item(self, worry_decreasing_factor=3):
		"""Monkey inspects and throws a single item (the first item in the queue).
		
		Parameters:
			worry_decreasing_factor (int): The factor your worry is divided by after inspection (default=3).
		
		Returns:
			int, int: The monkey index that this monkey will throw to, and the new worry level of the item, respectively."""
		new_worry_value = self.inspect(worry_decreasing_factor)
		monkey_to_throw_to = self.get_monkey_id_to_throw_to(new_worry_value)
		return monkey_to_throw_to, new_worry_value

	def do_turn(self, worry_decreasing_factor=3):
		"""This monkey takes a single turn. It inspects and throws all of the items it is currently holding.
		
		Parameters:
			worry_decreasing_factor (int): The factor your worry is divided by after inspection (default=3).
		
		Returns:
			list<tuple<int,int>>: A list of tuples. Each tuple represents the monkey an item will be thrown to and the new worry level."""
		result = []
		while self.items:
			item_result = self.do_single_item(worry_decreasing_factor)
			result.append(item_result)
		return result

	def get_info(self):
		return self.num_inspections, self.id

def convert_input_to_monkey(monkey_input):
	"""Takes the puzzle input that describes a single monkey and converts it to a single monkey object.
	
	Parameters:
		monkey_input (list<str>): A list of strings rerpesenting information about a monkey.
		
	Returns:
		Monkey: A monkey object representing the monkey described by these strings."""
	#extract the id
	split_id_line = monkey_input[0].split()
	id = int((split_id_line[1])[:-1])
	#extract starting items
	split_items = monkey_input[1].split(":")
	items = split_items[1].split(",")
	starting_items = []
	for item in items:
		starting_items.append(int(item))
	#extract operation info
	split_op_line = monkey_input[2].split("old ")
	operator_data = split_op_line[1]
	worry_operator = operator_data[0]
	if operator_data[2:] == "old\n":
		other_operator = None
	else:
		other_operator = int(operator_data[1:])
	#extract test data
	split_test_line = monkey_input[3].split("by")
	test_divisor = int(split_test_line[1])
	#extract monkey to throw if true
	true_id_split = monkey_input[4].split(" ")
	true_monkey_id = int(true_id_split[-1])
	#extract monkey to throw if false
	false_id_split = monkey_input[5].split(" ")
	false_monkey_id = int(false_id_split[-1])

	#make monkey
	monkey = Monkey(id, starting_items, worry_operator, other_operator, test_divisor, true_monkey_id, false_monkey_id)
	return monkey

def create_all_monkies(monkey_input):
	"""Takes the entire puzzle input and creates the list of monkies described by it.
	
	Parameters:
		monkey_input (list<str>): The puzzle input. Describes all the monkies used by this puzzle.
		
	Returns:
		list<Monkey>: A list of Monkey objects described by this input."""
	all_monkies = []
	for line_index in range(0, len(monkey_input), 7):
		monkey_data = monkey_input[line_index:line_index+6]
		monkey = convert_input_to_monkey(monkey_data)
		all_monkies.append(monkey)
	return all_monkies

def simulate_rounds(monkies, num_rounds, worry_decreasing_factor=3):
	"""Simulates the monkies inspecting and throwing items for the specified number of rounds.
	
	Parameters:
		monkies (list<Monkey>): List of monkies that will be inspecting and throwing items.
		num_rounds (int): The number of rounds the monkies will be inspecting and throwing items for.
		worry_decreasing_factor (int): The factor your worry is divided by after inspection (default=3).
		
	Returns:
		list<Monkey>: The list of monkies that was provided."""
	for round_num in range(num_rounds):
		for monkey in monkies:
			thrown_items = monkey.do_turn(worry_decreasing_factor)
			for item_thrown in thrown_items:
				monkey_thrown_to_id, new_item_worry_value = item_thrown
				monkey_thrown_to = monkies[monkey_thrown_to_id]
				monkey_thrown_to.items.append(new_item_worry_value)
	return monkies

def get_most_active_monkies_info(monkies, num_monkies_to_get, get_ids):
	"""Gets the desired number of most active monkies.
	
	Parameters:
		monkies (list<Monkey>): A list of monkies that have thrown items around.
		num_monkies_to_get (int): The number of most active monkies to get.
		get_ids (bool): Determines if you want the ids of the active monkies (True) or the num of inspections (False).
		
	Returns:
		list<int>: A list containing the ids of the most active monkies."""
	monkey_info = []
	for monkey in monkies:
		monkey_info.append(monkey.get_info())
	monkey_info.sort(reverse=True)
	result_num_inspections = []
	result_monkey_ids = []
	for curr_active_monkey_num_to_get in range(num_monkies_to_get):
		num_inspections, active_monkey_id = monkey_info[curr_active_monkey_num_to_get]
		result_num_inspections.append(num_inspections)
		result_monkey_ids.append(active_monkey_id)
	if get_ids:
		return result_monkey_ids
	return result_num_inspections

def calculate_monkey_business(num_inspections):
	"""Calculates the level of monkey business by multiplying the number of times each monkey inspected an item together.
	
	Parameters:
		num_inspections (list<int>): A list where each entry contains the number of times a single monkey inspected items.
		
	Returns:
		int: The level of monkey business (found by multiplying the number of inspections together."""
	monkey_business = num_inspections[0]
	for index_num in range(1, len(num_inspections), 1):
		monkey_business *= num_inspections[index_num]
	return monkey_business


def run_solution_1(filename):
	puzzle_input = readInput(filename)
	monkies = create_all_monkies(puzzle_input)
	num_rounds = 20
	worry_decreasing_factor = 3
	simulate_rounds(monkies, num_rounds)
	most_active_monkies_inspect = get_most_active_monkies_info(monkies, 2, False)
	monkey_business = calculate_monkey_business(most_active_monkies_inspect)
	print(f"The level of monkey business after {num_rounds} rounds and worry decreasing by a factor of {worry_decreasing_factor} is {monkey_business}.")

def run_solution_2(filename):
	puzzle_input = readInput(filename)
	monkies = create_all_monkies(puzzle_input)
	num_rounds = 10000
	worry_decreasing_factor = 1
	#use the Chinese remainder theorem to find divisor to decrease the worry to managable amounts
	mod_value = monkies[0].test_divisor
	for monkey_index in range(1, len(monkies), 1):
		mod_value *= monkies[monkey_index].test_divisor
	for monkey in monkies:
		monkey.mod_decrease_value = mod_value
	simulate_rounds(monkies, num_rounds, worry_decreasing_factor)
	most_active_monkies_inspect = get_most_active_monkies_info(monkies, 2, False)
	monkey_business = calculate_monkey_business(most_active_monkies_inspect) #* mod_value
	print(f"The level of monkey business after {num_rounds} rounds and worry decreasing by a factor of {worry_decreasing_factor} is {monkey_business}.")
