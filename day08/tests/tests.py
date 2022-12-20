import unittest
from pathlib import Path

from src import solution


class AoC_2022_Puzzle_7_Tests(unittest.TestCase):

	def setUp(self):
		filepath = Path(__file__).parent / "test_input.txt"
		with open(filepath, "r", encoding="utf8", newline=None) as file:
			self.data = file.readlines()
		self.clean_data = []
		for line in self.data:
			self.clean_data.append(line.strip())

	def test_strip_newlines(self):
		result = solution.strip_newlines(self.data)

		self.assertEqual(self.clean_data, result)

	def test_is_visible_row_test(self): #rewrite
		row = self.clean_data[3] # 33549

		self.assertTrue(solution.is_visible_row_test(row, 0)) #left edge
		self.assertTrue(solution.is_visible_row_test(row, len(row)-1)) #right edge
		self.assertFalse(solution.is_visible_row_test(row, 3)) #height=4, hidden
		self.assertTrue(solution.is_visible_row_test(row, 2)) #height=5, visible

	def test_is_visible_col_test(self):
		col = 0 #32633

		self.assertTrue(solution.is_visible_col_test(self.data, col, 0)) #top edge
		self.assertTrue(solution.is_visible_col_test(self.data, col, len(self.data)-1)) #bottom edge
		self.assertFalse(solution.is_visible_col_test(self.data, col, 1)) #height=2, hidden
		self.assertTrue(solution.is_visible_col_test(self.data, col, 2)) #height=6, visible

	def test_get_num_visible_trees(self):
		exp_result = 21
		result = solution.get_num_visible_trees(self.clean_data)

		self.assertEqual(exp_result, result)