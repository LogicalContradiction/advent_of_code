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

	def test_convert_signal_strengths_to_register_value(self):
		strengths = [0,1,4,9,16,25,36,49,64,81,100]
		exp_results = [0,1,2,3,4,5,6,7,8,9,10]
		results = solution.convert_signal_strengths_to_register_value(strengths)

		self.assertEqual(exp_results, results)

	def test_get_min_max_sprite_pos(self):
		center_index = 10
		sprite_size = 3
		exp_result = (9, 11)
		result = solution.get_min_max_sprite_pos(sprite_size, center_index)

		self.assertEqual(exp_result, result)

	def test_is_sprite_on_screen(self):
		reg_value = 10
		cycle_num_1 = 10
		cycle_num_2 = 11
		cycle_num_3 = 12
		cycle_num_4 = 13
		sprite_size = 3
		screen_width = 40
		result1 = solution.is_sprite_on_screen(reg_value, cycle_num_1, sprite_size, screen_width)
		result2 = solution.is_sprite_on_screen(reg_value, cycle_num_2, sprite_size, screen_width)
		result3 = solution.is_sprite_on_screen(reg_value, cycle_num_3, sprite_size, screen_width)
		result4 = solution.is_sprite_on_screen(reg_value, cycle_num_4, sprite_size, screen_width)

		self.assertTrue(result1)
		self.assertTrue(result2)
		self.assertTrue(result3)
		self.assertFalse(result4)

	def test_generate_image(self):
		sprite_size = 3
		signal_strengths = solution.simulate_instructions(self.data)
		reg_values = solution.convert_signal_strengths_to_register_value(signal_strengths)
		screen_width = 40
		exp_result = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""
		result = solution.generate_image(screen_width, reg_values, sprite_size)

		self.assertEqual(exp_result, result)