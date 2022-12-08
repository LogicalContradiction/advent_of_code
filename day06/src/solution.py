from pathlib import Path



def readInput(input_filename):
	filepath = Path(__file__).parent / input_filename
	with open(filepath, "r", encoding="utf8", newline=None) as file:
			data = file.readlines()
	return data

def is_start_of_packet_marker(sequence):
	"""Checks a sequence of characters to see if it's the start of packet marker. To be the marker, all characters must be unique.
	
	Parameters:
		sequence (str): A string representing the character sequence that needs to be checked.
		
	Returns:
		bool: True if all of the characters are unique, otherwise False."""
	sort_seq = sorted(sequence)
	for index in range(1, len(sort_seq)):
		char = sort_seq[index]
		prev_char = sort_seq[index-1]
		if char == prev_char:
			return False
	return True

def get_marker_index(datastream, length):
	"""Searches the datastream for the start of packet marker of a given length. The marker is a sequence of characters of the given length that are all unique.
	
	Parameters:
		datastream (str): String of characters representing the datastream.
		length (int): The length of the start of packet marker.
		
	Returns:
		int: The number of characters from the beginning of the buffer to the end of the first start of packet marker."""
	return get_first_unique_sequence_index_of_length(datastream, length)

def get_first_unique_sequence_index_of_length(datastream, length):
	"""Searches the datastream for a group of unique characters of the given length.

	Parameters:
		datastream (str): String of characters representing the datastream.
		length (int): The length of the group of unique characters.
		
	Returns:
		int: The number of characters from the beginning of the buffer to the end of the first unique group of characters."""
	ptr_start = 0
	ptr_end = length
	while ptr_end < len(datastream):
		if is_start_of_packet_marker(datastream[ptr_start:ptr_end]):
			return ptr_end
		ptr_start += 1
		ptr_end += 1
	return -1

	
def run_solution_1(filename):
	data = readInput(filename)
	num_char = get_marker_index(data[0].strip(), 4)
	print(f"The number of characters that need to be read before the first start of packet marker are {num_char} characters.")
