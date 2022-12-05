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

def modify_round_for_adjusted_cypher(round):
	"""Takes the information about the old cypher and generates a new round representation using the new cypher. Used for solution 2.
	
	Parameters:
		round (str): Represents the old round information.
	
	Returns:
		str: New representation of a round based on the updated cypher given."""
	opp_throw = round[0]
	round_result = round[2]
	you_throw = get_your_throw_from_opp_throw_and_round_result(opp_throw, round_result)
	new_round = f"{opp_throw} {you_throw}"
	return new_round

def get_your_throw_from_opp_throw_and_round_result(opp_throw, round_result):
	"""Returns the shape you must throw to get the desired round result.
	
	Parameters:
		opp_throw (str): A single-character string representing what shape the opponent threw.
		round_result (str): A single-character string representing what the desired round result is.
	
	Returns:
		str: A single-character string representing what shape you must throw to acheive the desired round result."""
	rock = "X"
	paper = "Y"
	scissors = "Z"
	if opp_throw == "A":		#rock
		if round_result == "X":		#lose
			return scissors
		elif round_result == "Y":	#draw
			return rock
		else:						#win
			return paper
	elif opp_throw == "B":		#paper
		if round_result == "X":		#lose
			return rock
		elif round_result == "Y":	#draw
			return paper
		else:						#win
			return scissors
								#scissors
	if round_result == "X":			#lose
		return paper
	elif round_result == "Y":		#draw
		return scissors
	return rock						#win

def adjust_data_for_new_cypher(data):
	"""Takes the data and adjusts it to use the new cypher given.
	
	Parameters:
		data (list): Represents the old round data as a list of strings.
	
	Returns:
		list: New list of strings where each string has been changed to account for the new cypher."""
	adjusted_data = []
	for line in data:
		adjusted_data.append(modify_round_for_adjusted_cypher(line))
	return adjusted_data

def run_solution_1(filename):
	data = readInput(filename)
	total_score = calc_your_total_score(data)
	print(f"By following the encrypted guide, you will end the tournament with {total_score} points.")

def run_solution_2(filename):
	data = readInput(filename)
	adjusted_data = adjust_data_for_new_cypher(data)
	total_score = calc_your_total_score(adjusted_data)
	print(f"After adjusting for the new cypher, the guide will allow you to end the tournament with {total_score} points.")

