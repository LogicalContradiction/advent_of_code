from pathlib import Path



def readInput(input_filename):
	filepath = Path(__file__).parent / input_filename
	with open(filepath, "r", encoding="utf8", newline=None) as file:
			data = file.readlines()
	return data

def get_cal_num_of_all_elves(data):
	"""
	Creates a reverse-sorted list of tuples that represent each elf and the number of calories they're carrying.
	Format = (num_calories, elf_num)
	"""
	result = []
	curr_elf_num = 1
	curr_elf_cal = 0
	for line in data:
		if line == "\n":
			#newline indicates there's a new elf pack
			result.append((curr_elf_cal, curr_elf_num))
			#now reset cal count and increment elf counter
			curr_elf_num += 1
			curr_elf_cal = 0
			continue
		#elf has more snacks, increment the counter
		curr_elf_cal += int(line)
	#include the last one since it's not explicitly added to the list
	result.append((curr_elf_cal, curr_elf_num))
	#now return reverse-sorted list of all elves
	result.sort(reverse=True)
	return result

def get_most_cal(reverse_sorted_cal_count):
	cal_num, elf_num = reverse_sorted_cal_count[0]
	return elf_num, cal_num

def get_elf_with_most_cal(data):
	elf_and_cal_data_rev = get_cal_num_of_all_elves(data)
	return get_most_cal(elf_and_cal_data_rev)


def get_total_cal_of_top_3(data):
	reverse_sorted_cal_count = get_cal_num_of_all_elves(data)
	total = 0
	for index in range(3):
		num_cal, elf_num = reverse_sorted_cal_count[index]
		total += num_cal
	return total


def run_solution_1(filename):
	data = readInput(filename)
	elf_num, num_cal = get_elf_with_most_cal(data)
	if elf_num == -1:
		print("No elves found in input")
	else:
		print(f"Elf num {elf_num} has the most calories.\nThey are carrying {num_cal} calories.")

def run_solution_2(filename):
	data = readInput(filename)
	num_cal_top_3 = get_total_cal_of_top_3(data)
	print(f"The total number of calories carried by the top 3 elves is {num_cal_top_3} calories.")

