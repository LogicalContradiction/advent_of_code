from pathlib import Path



def readInput(input_filename):
	filepath = Path(__file__).parent / input_filename
	with open(filepath, "r", encoding="utf8", newline=None) as file:
			data = file.readlines()
	return data


def split_pair_rep(elf_pair):
	"""Takes a pair of elves and splits it into the representation that each individual elf has to clean.
	
	Paramters:
		elf_pair (str): A string representing a single pair of elves.
	
	Returns:
		list<str>: A list of two strings, each representing the space a single elf has to clean."""
	return elf_pair.split(",")

def split_cleaning_space_rep(cleaning_space):
	"""Takes a representation of the space an elf needs to clean and converts it to a tuple of integers.
	
	Parameters:
		cleaning_space (str): String representation of the sapce an elf needs to clean. Broken up by -.
		
	Returns:
		int, int: the start and end point that this elf needs to clean."""
	split_data = cleaning_space.split("-")
	return int(split_data[0]), int(split_data[1])

def does_one_range_enclose_other(range1, range2):
	"""Tests to see if one range completely encloses the other.
	
	Parameters:
		range1 (int, int): Tuple of ints that represent the start and end of this range.
		range2 (int, int): Tuple of ints that represent the start and end of this range.
		
	Returns:
		bool: True if one range encloses the other, False if not."""
	range1_s, range1_e = range1
	range2_s, range2_e = range2
	#test if range 1 encloses range 2
	if range1_s <= range2_s and range1_e >= range2_e:
		return True
	#test if range 2 encloses range 1
	if range2_s <= range1_s and range2_e >= range1_e:
		return True
	return False

def count_num_fully_overlapping_sections(data):
	"""Counts the number of pairs of elves where one elf is cleaning a section entirely enclosed by the other.
	
	Parameters:
		data (list<str>): A list of strings representing the spaces each pair of elves is supposed to clean.
		
	Returns:
		int: The number of pairs of elves where one elf is cleaning a section enerely enclosed by the other."""
	total = 0
	for elf_pair in data:
		cleaning_spaces = split_pair_rep(elf_pair.strip())
		elf1_space = split_cleaning_space_rep(cleaning_spaces[0])
		elf2_space = split_cleaning_space_rep(cleaning_spaces[1])
		if does_one_range_enclose_other(elf1_space, elf2_space):
			total += 1
	return total


def run_solution_1(filename):
	data = readInput(filename)
	total = count_num_fully_overlapping_sections(data)
	print(f"There are {total} pairs of elves where one elf's section is completely enclosing the other's.")