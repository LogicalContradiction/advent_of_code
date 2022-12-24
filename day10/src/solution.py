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

def convert_signal_strengths_to_register_value(signal_strengths):
	""""""
	register_values = []
	#no cycle 0, so append placeholder
	register_values.append(0)
	for index in range(1, len(signal_strengths), 1):
		strength = signal_strengths[index]
		register_values.append(strength // index)
	return register_values

def get_min_max_sprite_pos(sprite_size, center_index):
	"""Determines the minimum and maximum index this sprite will occupy.
	
	Parameters:
		sprite_size (int): The number of pixels this sprite is.
		center_index (int): The middle index of the sprite.
		
	Returns:
		int, int: The minimum and maximum index of the sprite, respecitvely"""
	sprite_size_half = sprite_size // 2
	min_index = center_index - sprite_size_half
	max_index = center_index + sprite_size_half
	return min_index, max_index

def is_sprite_on_screen(reg_value, curr_cycle_num, sprite_size, screen_width):
	"""Determines if the sprite will be visible when the pixel is drawn.
	
	Parameters:
		reg_value (int): The value being held by the register during this cycle.
		curr_cycle_num (int): The current cycle number.
		sprite_size (int): The number of pixels the sprite is
		screen_width (int): The width (in pixels) of the screen
		
	Returns:
		bool: True if the sprite will be visible when the pixel is drawn, otherwise False."""
	#current sprite position is centered on the value in the register
	min_index, max_index = get_min_max_sprite_pos(sprite_size, reg_value)
	curr_pixel_index = (curr_cycle_num-1) % screen_width #the index of the pixel being drawn is one less than the cycle number
	return curr_pixel_index >= min_index and curr_pixel_index <= max_index #pixel is visible if it's on or between the min and max

def generate_image(screen_width, reg_values, sprite_size):
	"""Generates the screen image based on the register values.
	
	Parameters:
		screen_width (int): The width (in pixels) of the screen.
		screen_height (int): The height (in pixels) of the screen.
		reg_values (list<int>): The value of the register at the start of each cycle.
		sprite_size (int): The size (in pixels) of the sprite.
		
	Returns:
		str: The image that will be printed."""
	image = ""
	cycle_num = 0
	while cycle_num < len(reg_values)-1:
		cycle_num += 1
		reg_value = reg_values[cycle_num]
		if is_sprite_on_screen(reg_value, cycle_num, sprite_size, screen_width):
			image = image + "#"
		else:
			image = image + "."
		if cycle_num % screen_width == 0:
			image = image + "\n"
	return image



def run_solution_1(filename):
	instructions = readInput(filename)
	cycle_nums = [20, 60, 100, 140, 180, 220]
	strength_sum = get_sum_of_certain_signal_strengths_from_instructions(instructions, cycle_nums)
	print(f"The sum of the six signal strengths is {strength_sum}.")

def run_solution_2(filename):
	instructions = readInput(filename)
	signal_strengths = simulate_instructions(instructions)
	reg_values = convert_signal_strengths_to_register_value(signal_strengths)
	screen_width = 40
	sprite_size = 3
	image = generate_image(screen_width, reg_values, sprite_size)
	print(f"The image generated:\n{image}\n")
