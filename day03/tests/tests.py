import unittest
from pathlib import Path

from src import solution



class AoC_2022_Puzzle_3_Tests(unittest.TestCase):


	def setUp(self):
		filepath = Path(__file__).parent / "test_input.txt"
		with open(filepath, "r", encoding="utf8") as file:
			self.data = file.readlines()

	def test_divide_rucksack_into_2_compartments(self):
		rucksack = "abcdefghijkl"
		exp_left = "abcdef"
		exp_right = "ghijkl"
		res_left, res_right = solution.divide_rucksack_into_2_compartments(rucksack)
		self.assertEqual(exp_left, res_left)
		self.assertEqual(exp_right, res_right)


	def test_find_duplicate_item(self):
		left = sorted("vJrwpWtwJgWr")
		right = sorted("hcsFMMfFFhFp")
		self.assertEqual(solution.find_duplicate_item(left, right), "p")

	def test_convert_item_to_priority(self):
		self.assertEqual(solution.convert_item_to_priority("A"), 27)
		self.assertEqual(solution.convert_item_to_priority("Z"), 52)
		self.assertEqual(solution.convert_item_to_priority("G"), 33)
		self.assertEqual(solution.convert_item_to_priority("a"), 1)
		self.assertEqual(solution.convert_item_to_priority("z"), 26)
		self.assertEqual(solution.convert_item_to_priority("u"), 21)

	def test_get_duplicate_item_in_rucksack(self):
		rucksack = "vJrwpWtwJgWrhcsFMMfFFhFp"
		self.assertEqual(solution.get_duplicate_item_in_rucksack(rucksack), "p")

	def test_get_dup_item_priority_from_rucksack(self):
		rucksack = "vJrwpWtwJgWrhcsFMMfFFhFp"
		self.assertEqual(solution.get_dup_item_priority_from_rucksack(rucksack), 16)
	
	def test_get_total_priority_of_dup_items_in_all_rucksacks(self):
		self.assertEqual(solution.get_total_priority_of_dup_items_in_all_rucksacks(self.data), 157)