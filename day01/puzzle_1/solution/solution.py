from pathlib import Path



def readInput(input_filename):
	filepath = Path(__file__).parent / input_filename
	with open(filepath, "r", encoding="utf8") as file:
			data = file.readlines()
	return data

def get_elf_with_most_cal(data):
	most_cal = -1
	most_cal_elf_num = -1

	curr_elf_num = 1
	curr_elf_cal = 0
	for line in data:
		if line == '\n':
			if curr_elf_cal > most_cal:
				most_cal = curr_elf_cal
				most_cal_elf_num = curr_elf_num
			curr_elf_num+= 1
			curr_elf_cal = 0
			continue
		curr_elf_cal += int(line)
	return most_cal_elf_num, most_cal


def run(filename):
	data = readInput(filename)
	elf_num, num_cal = get_elf_with_most_cal(data)
	if elf_num == -1:
		print("No elves found in input")
	else:
		print(f"Elf num {elf_num} has the most calories.\nThey are carrying {num_cal} calories.")
