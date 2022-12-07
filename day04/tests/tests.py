import unittest
from pathlib import Path

from src import solution



class AoC_2022_Puzzle_4_Tests(unittest.TestCase):


	def setUp(self):
		filepath = Path(__file__).parent / "test_input.txt"
		with open(filepath, "r", encoding="utf8", newline=None) as file:
			self.data = file.readlines()

	def test_split_pair_rep(self):
		data = "2-4,6-8"
		pair = solution.split_pair_rep(data)
		self.assertEqual(pair[0], "2-4")
		self.assertEqual(pair[1], "6-8")

	def test_split_cleaning_space_rep(self):
		data = "2-4"
		result1, result2 = solution.split_cleaning_space_rep(data)
		self.assertEqual(result1, 2)
		self.assertEqual(result2, 4)

	def test_does_one_range_enclose_other(self):
		range1 = (2, 4)
		range2 = (6, 8)
		range3 = (2, 8)
		range4 = (3, 7)
		self.assertFalse(solution.does_one_range_enclose_other(range1, range2))
		self.assertTrue(solution.does_one_range_enclose_other(range3, range4))
		self.assertTrue(solution.does_one_range_enclose_other(range4, range3))

	def test_count_num_fully_overlapping_sections(self):
		total = solution.count_num_fully_overlapping_sections(self.data)
		self.assertEqual(total, 2)
