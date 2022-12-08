import unittest
from pathlib import Path
from collections import deque

from src import solution


class AoC_2022_Puzzle_6_Tests(unittest.TestCase):

	def setUp(self):
		filepath = Path(__file__).parent / "test_input.txt"
		with open(filepath, "r", encoding="utf8", newline=None) as file:
			self.data = file.readlines()

	def test_is_start_of_packet_marker(self):
		seq1 = "abdc"
		seq2 = "adat"
		self.assertTrue(solution.is_start_of_packet_marker(seq1))
		self.assertFalse(solution.is_start_of_packet_marker(seq2))

	def test_get_first_unique_sequence_index_of_length(self):
		datastream = "abababababababacdzeafsdasdfaweasdfa"
		exp_res = 18
		length = 5
		result = solution.get_first_unique_sequence_index_of_length(datastream, length)
		self.assertEqual(exp_res, result)

	def test_get_marker_index(self):
		datastream = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
		length = 4
		exp_res = 7
		self.assertEqual(solution.get_marker_index(datastream, length), exp_res)