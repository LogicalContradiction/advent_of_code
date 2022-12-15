import unittest
from pathlib import Path

from src import solution


class AoC_2022_Puzzle_7_Tests(unittest.TestCase):

	def setUp(self):
		filepath = Path(__file__).parent / "test_input.txt"
		with open(filepath, "r", encoding="utf8", newline=None) as file:
			self.data = file.readlines()

	def test_process_ls(self):
		command_index = 1
		exp_result = (23352670, 2, 6)
		result = solution.process_ls(self.data, command_index)

		self.assertEqual(exp_result, result)

	def test_process_cd_no_recursion(self):
		command_index = 12
		max_dir_size = 100000
		large_files = []
		exp_result = (16, 584)
		exp_final_large_files = [584]
		result = solution.process_cd(self.data, command_index, max_dir_size, large_files)

		self.assertEqual(exp_result, result)
		self.assertEqual(exp_final_large_files, large_files)

	def test_process_cd_recursion(self):
		command_index = 6
		max_dir_size = 100000
		large_files = []
		exp_result = (17, 94853)
		exp_final_large_files = [584, 94853]
		result = solution.process_cd(self.data, command_index, max_dir_size, large_files)

		self.assertEqual(exp_result, result)
		self.assertEqual(exp_final_large_files, large_files)
		
	def test_process_cd_all_data(self):
		command_index = 0
		max_dir_size = 100000
		large_files = []
		num_commands = len(self.data)
		exp_result_size = 48381165
		exp_final_large_files = [584, 94853]
		result_command_index, result_size = solution.process_cd(self.data, command_index, max_dir_size, large_files)

		self.assertGreater(result_command_index, num_commands)
		self.assertEqual(exp_result_size, result_size)
		self.assertEqual(exp_final_large_files, large_files)

	def test_get_all_dir_sizes_less_than_size(self):
		max_dir_size = 100000
		exp_result = [584, 94853]
		result = solution.get_all_dir_sizes_less_than_size(self.data, max_dir_size)

		self.assertEqual(exp_result, result)

	def test_get_sum_of_dir_less_than_size(self):
		exp_result = 95437
		max_dir_size = 100000
		result = solution.get_sum_of_dir_less_than_size(self.data, max_dir_size)

		self.assertEqual(exp_result, result)