import unittest
from pathlib import Path
from collections import deque

from src import solution


class AoC_2022_Puzzle_5_Tests(unittest.TestCase):

	def setUp(self):
		filepath = Path(__file__).parent / "test_input.txt"
		with open(filepath, "r", encoding="utf8", newline=None) as file:
			self.data = file.readlines()

	def test_decode_starting_pos(self):
		init_stack = self.data[:4]
		exp_res_stack1 = deque(["Z", "N"])
		exp_res_stack2 = deque(["M", "C", "D"])
		exp_res_stack3 = deque(["P"])
		result = solution.decode_starting_pos(init_stack)

		self.assertEqual(result[0], exp_res_stack1)
		self.assertEqual(result[1], exp_res_stack2)
		self.assertEqual(result[2], exp_res_stack3)
	
	def test_decode_single_movement(self):
		move1 = "move 1 from 2 to 1"
		move2 = "move 1 from 2 to 1\n"
		self.assertEqual(solution.decode_single_movement(move1), (2, 1, 1))
		self.assertEqual(solution.decode_single_movement(move2), (2, 1, 1))

	def test_decode_all_movements(self):
		exp_res = [(2,1,1), (1,3,3), (2,1,2), (1,2,1)]
		result = solution.decode_all_movements(self.data[5:])
		self.assertEqual(exp_res, result)

	def test_process_single_move(self):
		stacks = [deque(["A", "B", "C"]), deque(["D", "E", "F"])]
		move = (1, 2, 2)
		exp_result = [deque(["A"]), deque(["D", "E", "F", "C", "B"])]
		result = solution.process_single_move(move, stacks)
		self.assertEqual(exp_result, result)

	def test_get_top_crates_message(self):
		stacks = [deque(["A", "B", "C"]), deque(["D", "E", "F"])]
		exp_res = "CF"
		result = solution.get_top_crates_message(stacks)
		self.assertEqual(exp_res, result)

	def test_process_all_moves(self):
		stacks = [deque(["Z", "N"]), deque(["M", "C", "D"]), deque(["P"])]
		moves = [(2,1,1), (1,3,3), (2,1,2), (1,2,1)]
		exp_res = [deque(["C"]), deque(["M"]), deque(["P", "D", "N", "Z"])]
		result = solution.process_all_moves(moves, stacks)
		self.assertEqual(exp_res, result)

	def test_get_div_point_index_of_data(self):
		self.assertEqual(solution.get_div_point_index_of_data(self.data), 4)

	def test_do_simulation(self):
		exp_res = "CMZ"
		result = solution.do_simulation(self.data)
		self.assertEqual(exp_res, result)

	def test_process_single_move_keep_order(self):
		stacks = [deque(["Z", "N", "D"]), deque(["M", "C"]), deque(["P"])]
		move = (1, 3, 3)
		exp_res = [deque([]), deque(["M", "C"]), deque(["P", "Z", "N", "D"])]
		result = solution.process_single_move_keep_order(move, stacks)
		self.assertEqual(exp_res, result)

	def test_process_all_moves_keep_order(self):
		stacks = [deque(["Z", "N"]), deque(["M", "C", "D"]), deque(["P"])]
		moves = [(2,1,1), (1,3,3), (2,1,2), (1,2,1)]
		exp_res = [deque(["M"]), deque(["C"]), deque(["P", "Z", "N", "D"])]
		result = solution.process_all_moves_keep_order(moves, stacks)
		self.assertEqual(exp_res, result)

	def test_do_simulation_preserve_order(self):
		exp_res = "MCD"
		result = solution.do_simulation_preserve_order(self.data)
		self.assertEqual(exp_res, result)