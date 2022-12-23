from pathlib import Path



def readInput(input_filename):
	filepath = Path(__file__).parent / input_filename
	with open(filepath, "r", encoding="utf8", newline=None) as file:
			data = file.readlines()
	return data


#add isn't fully processed until after the cycle is complete - it is still the original value before and during the cycle

def calculate_signal_strength(cycle_num, reg_value):
	"""Calculates the signal strength given the cycle number and register value.
	
	Parameters:
		cycle_num (int): The cycle number the cpu is at.
		reg_value (int): The value in register X at the given cycle number.
		
	Returns:
		int: The signal strength."""
	return cycle_num * reg_value

def caluclate_sum_of_signal_strength(signal_strengths, cycle_nums):
	"""Calculates the sum of the signal strengths of the chosen cycle numbers.
	
	Parameters:
		signal_strengths (list<int>): List of signal strengths. The index of the list is the cycle number.
		cycle_nums (list<int>): List of cycle numbers that we are interested in the sum of.
		
	Returns:
		int: The sum of the signal strengths at the chosen cycle numbers."""
	total_sum = 0
	for cycle_num in cycle_nums:
		total_sum += signal_strengths[cycle_num]
	return total_sum

def simulate_instructions(instructions):
	"""Simulates running the instructions on the CPU.
	
	Parameters:
		instructions (list<str>): List of instructions to run.
		
	Returns:
		list<int>: The signal strengths at each cycle number."""
	signal_strengths = []
	instruction_index = 0
	cycle_num = 0
	register = 1
	do_add = False
	#there is no cycle 0, so just add a placeholder
	signal_strengths.append(0)
	while instruction_index < len(instructions):
		cycle_num += 1
		curr_instruction = instructions[instruction_index]
		signal_strengths.append(calculate_signal_strength(cycle_num, register))
		if curr_instruction == "noop" or curr_instruction == "noop\n":
			#noop does nothing, so increment instruction counter
			instruction_index += 1
		#otherwise it's add, so process it
		elif do_add:
			#this is the second cycle of add, so do the add now
			do_add = False
			#split the string and extract the value to add
			split_inst = curr_instruction.split()
			add_value = int(split_inst[1])
			register += add_value
			#done with add, now increment instruction index
			instruction_index += 1
		else:
			#first cycle of add, no change yet, but need to set the boolean
			do_add = True
			#do not increment the instruction index since we're not done processing the add instruction
	return signal_strengths

def get_sum_of_certain_signal_strengths_from_instructions(instructions, cycle_nums):
	"""Calculates the sum of the signal strengths of the chosen cycles from the set of instructions.
	
	Parameters:
		instructions (list<str>): The instruction list to get the strengths of.
		cycle_nums (list<int>): The cycle numbers we want the sum of the signal strength of.
		
	Returns:
		int: The sum of the signal strengths of the chosen cycles."""
	signal_strengths = simulate_instructions(instructions)
	strength_sum = caluclate_sum_of_signal_strength(signal_strengths, cycle_nums)
	return strength_sum


def run_solution_1(filename):
	instructions = readInput(filename)
	cycle_nums = [20, 60, 100, 140, 180, 220]
	strength_sum = get_sum_of_certain_signal_strengths_from_instructions(instructions, cycle_nums)
	print(f"The sum of the six signal strengths is {strength_sum}.")
