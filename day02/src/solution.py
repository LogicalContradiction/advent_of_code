from pathlib import Path



def readInput(input_filename):
	filepath = Path(__file__).parent / input_filename
	with open(filepath, "r", encoding="utf8") as file:
			data = file.readlines()
	return data


def calc_score_of_round(round):
	"""Returns the numerical score of a round.

	Parameters:
		round (str): A string representing a round.

	Returns:
		int: The number of points you would receive if this round is played."""
	#first extract what each player throws
	you_throw = round[2]
	opp_throw = round[0]
	return get_score_of_your_throw(you_throw) + determine_num_points_from_round_result(you_throw, opp_throw)


def get_score_of_your_throw(you_throw):
	"""Returns the number of points you receive for throwing that shape."""

	if you_throw == "X": #rock
		return 1
	elif you_throw == "Y": #paper
		return 2
	return 3	#scissors

def determine_num_points_from_round_result(you_throw, opp_throw):
	"""Determines the number of points received based on the round result.
	
	Parameters:
		you_throw (str): A single-character string representing the shape you threw.
		opp_throw (str): A single-character string representing the shape your opponent threw.
		
	Returns:
		int: The number of points you would receive from the outcome of this round (win/loss/draw only)."""
	point_value_win = 6
	point_value_loss = 0
	point_value_draw = 3

	if you_throw == "X": 			#you-rock
		if opp_throw == "C":			#opp-scisors
			return point_value_win
		elif opp_throw == "B":			#opp-paper
			return point_value_loss
		else:							#opp-rock
			return point_value_draw
	elif you_throw == "Y":			#you-paper
		if opp_throw == "A":			#opp-rock
			return point_value_win
		elif opp_throw == "C":			#opp-scissors
			return point_value_loss
		else:							#opp-paper
			return point_value_draw
									#you-scissors
	if opp_throw == "B":				#opp-paper
		return point_value_win
	elif opp_throw == "A":				#opp-rock
		return point_value_loss
	return point_value_draw				#opp-scissors

def calc_your_total_score(data):
	"""Calculates the total score you would receive by following the rounds.
	
	Parameters:
		data (str): Represents each round. One line per round
		
	Returns:
		int: The total number of points you will have at the end of the tournament."""
	total_score = 0
	for line in data:
		total_score += calc_score_of_round(line)
	return total_score

def run_solution_1(filename):
	data = readInput(filename)
	total_score = calc_your_total_score(data)
	print(f"By following the encrypted guide, you will end the tournament with {total_score} points.")
