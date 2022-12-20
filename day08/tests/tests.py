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

	def test_get_num_trees_visible_row(self):
		row = self.clean_data[1]
		index = 2
		exp_result = (1, 2)
		result = solution.get_num_trees_visible_row(row, index)

		self.assertEqual(exp_result, result)

	def test_get_num_trees_visible_row_left_edge(self):
		row = self.clean_data[2]
		index = 0
		exp_result = (0, 4)
		result = solution.get_num_trees_visible_row(row, index)

		self.assertEqual(exp_result, result)

	def test_get_num_trees_visible_row_right_edge(self):
		row = self.clean_data[3]
		index = 4
		exp_result = (4, 0)
		result = solution.get_num_trees_visible_row(row, index)

		self.assertEqual(exp_result, result)

	def test_get_num_trees_visible_col(self):
		col_index = 2
		tree_to_check_row_index = 1
		exp_result = (1, 2)
		result = solution.get_num_trees_visible_col(self.clean_data, col_index, tree_to_check_row_index)

		self.assertEqual(exp_result, result)

	def test_get_num_trees_visible_col_top_edge(self):
		col_index = 3
		tree_to_check_row_index = 0
		exp_result = (0, 4)
		result = solution.get_num_trees_visible_col(self.clean_data, col_index, tree_to_check_row_index)

		self.assertEqual(exp_result, result)

	def test_get_num_trees_visible_col_bot_edge(self):
		col_index = 3
		tree_to_check_row_index = 4
		exp_result = (4, 0)
		result = solution.get_num_trees_visible_col(self.clean_data, col_index, tree_to_check_row_index)

		self.assertEqual(exp_result, result)

	def test_calculate_scenic_score(self):
		left = 1
		right = 1
		up = 2
		down = 2
		exp_result = 4
		result = solution.calculate_scenic_score(left, right, up, down)

		self.assertEqual(exp_result, result)

	def test_calculate_scenic_score_of_tree(self):
		row_index = 3
		col_index = 2
		exp_result = 8
		result = solution.calculate_scenic_score_of_tree(self.clean_data, row_index, col_index)

		self.assertEqual(exp_result, result)

	def test_get_highest_scenic_score(self):
		exp_result = 8
		result = solution.get_highest_scenic_score(self.clean_data)

		self.assertEqual(exp_result, result)
