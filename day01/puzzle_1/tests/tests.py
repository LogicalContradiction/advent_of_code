import unittest
from pathlib import Path

from solution import solution


class AoC_2022_Puzzle_1_Tests(unittest.TestCase):

	def setUp(self):
		filepath = Path(__file__).parent / "test_input.txt"
		with open(filepath, "r", encoding="utf8") as file:
			self.data = file.readlines()


	def test_solution(self):
		result_elf_num, result_num_cal = solution.get_elf_with_most_cal(self.data)
		self.assertEqual(result_elf_num, 4)
		self.assertEqual(result_num_cal, 24000)