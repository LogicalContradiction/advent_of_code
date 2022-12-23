import unittest
from pathlib import Path

from src import solution


class AoC_2022_Puzzle_10_Tests(unittest.TestCase):

	def setUp(self):
		filepath = Path(__file__).parent / "test_input.txt"
		with open(filepath, "r", encoding="utf8", newline=None) as file:
			self.data = file.readlines()


	def test_caluclate_sum_of_signal_strength(self):
		signal_strengths =[0,1,2,3,4,5,6,7,8,9]
		cycles_of_interest = [1,3,5,8]
		exp_result = 17
		result = solution.caluclate_sum_of_signal_strength(signal_strengths, cycles_of_interest)

		self.assertEqual(exp_result, result)

	def test_simulate_instructions(self):
		set_of_exp_results = [
			(20, 420),
			(60, 1140),
			(100, 1800),
			(140, 2940),
			(180, 2880),
			(220, 3960)
			]
		signal_strengths = solution.simulate_instructions(self.data)

		for exp_result in set_of_exp_results:
			exp_cycle_num, exp_strength = exp_result
			self.assertEqual(signal_strengths[exp_cycle_num], exp_strength)

	def test_get_sum_of_certain_signal_strengths_from_instructions(self):
		cycle_nums = [20, 60, 100, 140, 180, 220]
		exp_result = 13140
		result = solution.get_sum_of_certain_signal_strengths_from_instructions(self.data, cycle_nums)

		self.assertEqual(exp_result, result)