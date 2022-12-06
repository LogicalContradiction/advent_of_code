from pathlib import Path



def readInput(input_filename):
	filepath = Path(__file__).parent / input_filename
	with open(filepath, "r", encoding="utf8") as file:
			data = file.readlines()
	return data

def divide_rucksack_into_2_compartments(rucksack):
	"""Divide a rucksack into two equal compartments.
	
	Parameters:
		rucksack (str): String representation of the contents of a rucksack.
	
	Returns:
		str, str: Two strings representing compartments 1 and 2 of the rucksack."""
	midpoint = len(rucksack) // 2
	comp_left = rucksack[:midpoint]
	comp_right = rucksack[midpoint:]
	return comp_left, comp_right

def find_duplicate_item(left, right):
	"""Searches two sorted rucksacks for an item found in both.
	
	Parameters:
		left (str): Sotred string representation of the left compartment of a rucksack.
		right (str): Sorted string representation of the right compartment of a rucksack.
		
	Returns:
		str: Single-character string representing the item found in both rucksacks."""
	ptr_left = 0
	ptr_right = 0
	while left[ptr_left] != right[ptr_right]:
		if left[ptr_left] < right[ptr_right]:
			ptr_left += 1
		else:
			ptr_right += 1
	return left[ptr_left]

def convert_item_to_priority(item):
	"""Converts an item into its priority.
	
	Parameters:
		item (str): Single-character string representing an item that we want the priority of.
		
	Returns:
		int: An integer representing the priority of this item."""
	item_ascii_code = ord(item)
	#if ascii < 91, it's uppercase
	if item_ascii_code < 91:
		return item_ascii_code - 38
	#otherwise it's a lowercase
	return item_ascii_code - 96

def get_duplicate_item_in_rucksack(rucksack):
	"""Takes a single rucksack and finds the duplicate item in its compartments.
	
	Parameters:
		rucksack (str): String representing the contents of a rucksack.
		
	Returns:
		str: Single-character string representing the item that is in both compartments."""
	left, right = divide_rucksack_into_2_compartments(rucksack)
	sort_left = sorted(left)
	sort_right = sorted(right)
	
	dup_item = find_duplicate_item(sort_left, sort_right)
	return dup_item

def get_dup_item_priority_from_rucksack(rucksack):
	"""Takes a single rucksack and finds the item priority of the duplicate item in it.
	
	Parameters:
		rucksack (str): String representing the contens of a rucksack.
		
	Returns:
		int: An integer representing the priority of the duplicate item in this rucksack."""
	dup_item = get_duplicate_item_in_rucksack(rucksack)
	priority = convert_item_to_priority(dup_item)
	return priority

def get_total_priority_of_dup_items_in_all_rucksacks(data):
	"""Gets the sum of the priority of each single duplicate item in each rucksack.
	
	Parameters:
		data (list <str>): List of string representations of each rucksack.
		
	Returns:
		int: The sum of the priorities of the single duplicate item in each rucksack."""
	total = 0
	for rucksack in data:
		total += get_dup_item_priority_from_rucksack(rucksack.strip())
	return total

def get_badge_from_3_rucksacks(rucksack1, rucksack2, rucksack3):
	"""Get the badge from three unsorted rucksacks. The badge is the common element between the three.
	
	Parameters:
		rucksack1 (str): String representing one of the rucksacks. Unsorted.
		rucksack2 (str): String representing one of the rucksacks. Unsorted.
		rucksack3 (str): String representing one of the rucksacks. Unsorted.
		
	Returns:
		str: Single-character string containing the representation of this group's badge."""
	rs_1_sorted = sorted(rucksack1.strip())
	rs_2_sorted = sorted(rucksack2.strip())
	rs_3_sorted = sorted(rucksack3.strip())
	ptr_1 = 0
	ptr_2 = 0
	ptr_3 = 0
	while rs_1_sorted[ptr_1] != rs_2_sorted[ptr_2] or rs_2_sorted[ptr_2] != rs_3_sorted[ptr_3]:
		max_element = max(rs_1_sorted[ptr_1], rs_2_sorted[ptr_2], rs_3_sorted[ptr_3])
		if rs_1_sorted[ptr_1] < max_element:
			ptr_1 += 1
		if rs_2_sorted[ptr_2] < max_element:
			ptr_2 += 1
		if rs_3_sorted[ptr_3] < max_element:
			ptr_3 += 1
	return rs_1_sorted[ptr_1]

def get_total_priority_of_all_badges(data):
	"""Gets the sum of the priority of all the badges from each group.
	
	Parameters:
		data (list<str>): A list of strings that represent each rucksack. Each group of 3 is a single badge group.
		
	Returns:
		int: Sum of all the priorities of the badges."""
	total = 0
	for index in range(0, len(data), 3):
		badge = get_badge_from_3_rucksacks(data[index], data[index+1], data[index+2])
		total += convert_item_to_priority(badge)
	return total


def run_solution_1(filename):
	data = readInput(filename)
	total = get_total_priority_of_dup_items_in_all_rucksacks(data)
	print(f"The total priority for the single duplicate item in each rucksack is {total}.")

def run_solution_2(filename):
	data = readInput(filename)
	total = get_total_priority_of_all_badges(data)
	print(f"The sum of the priorities of all the badges is {total}.")