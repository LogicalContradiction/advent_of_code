import unittest
from pathlib import Path

from src import solution


class AoC_2022_Puzzle_9_Tests(unittest.TestCase):

	def setUp(self):
		filepath = Path(__file__).parent / "test_input.txt"
		with open(filepath, "r", encoding="utf8", newline=None) as file:
			self.data = file.readlines()

		self.head1 = solution.RopeNode(1, 1)

		self.tail1 = solution.RopeNode(1, 1)

		self.tail2 = solution.RopeNode(2, 1)

		self.tail3 = solution.RopeNode(0, 1)

		self.tail4 = solution.RopeNode(1, 2)

		self.tail5 = solution.RopeNode(1, 0)

		self.tail6 = solution.RopeNode(2, 2)

		self.tail7 = solution.RopeNode(0, 0)

		filepath_longdata = Path(__file__).parent / "long_test_input.txt"
		with open(filepath_longdata, "r", encoding="utf8", newline=None) as file:
			self.long_data = file.readlines()

	def test_is_head_touching_tail(self):
		not_valid_tail = solution.RopeNode(-1, -1)

		self.assertTrue(solution.is_head_touching_tail(self.head1, self.tail1))
		self.assertTrue(solution.is_head_touching_tail(self.head1, self.tail2))
		self.assertTrue(solution.is_head_touching_tail(self.head1, self.tail3))
		self.assertTrue(solution.is_head_touching_tail(self.head1, self.tail4))
		self.assertTrue(solution.is_head_touching_tail(self.head1, self.tail5))
		self.assertTrue(solution.is_head_touching_tail(self.head1, self.tail6))
		self.assertTrue(solution.is_head_touching_tail(self.head1, self.tail7))

		self.assertFalse(solution.is_head_touching_tail(self.head1, not_valid_tail))

	def test_move_tail_towards_head_diag(self):
		head1 = solution.RopeNode(2, 1)
		tail1 = solution.RopeNode(0, 0)
		exp_result_x1 = 1
		exp_result_y1 = 1
		result1 = solution.move_tail_towards_head(head1, tail1)
		self.assertEqual(exp_result_x1, result1.x)
		self.assertEqual(exp_result_y1, result1.y)

		head2 = solution.RopeNode(0, 0)
		tail2 = solution.RopeNode(2, 1)
		exp_result_x2 = 1
		exp_result_y2 = 0
		result2 = solution.move_tail_towards_head(head2, tail2)
		self.assertEqual(exp_result_x2, result2.x)
		self.assertEqual(exp_result_y2, result2.y)

	def test_move_tail_towards_head_horiz(self):
		head1 = solution.RopeNode(2, 0)
		tail1 = solution.RopeNode(0, 0)
		exp_result_x1 = 1
		exp_result_y1 = 0
		result1 = solution.move_tail_towards_head(head1, tail1)
		self.assertEqual(exp_result_x1, result1.x)
		self.assertEqual(exp_result_y1, result1.y)

		head2 = solution.RopeNode(0, 0)
		tail2 = solution.RopeNode(2, 0)
		exp_result_x2 = 1
		exp_result_y2 = 0
		result2 = solution.move_tail_towards_head(head2, tail2)
		self.assertEqual(exp_result_x2, result2.x)
		self.assertEqual(exp_result_y2, result2.y)

	def test_move_tail_towards_head_vert(self):
		head1 = solution.RopeNode(0, 2)
		tail1 = solution.RopeNode(0, 0)
		exp_result_x1 = 0
		exp_result_y1 = 1
		result1 = solution.move_tail_towards_head(head1, tail1)
		self.assertEqual(exp_result_x1, result1.x)
		self.assertEqual(exp_result_y1, result1.y)

		head2 = solution.RopeNode(0, 0)
		tail2 = solution.RopeNode(0, 2)
		exp_result_x2 = 0
		exp_result_y2 = 1
		result2 = solution.move_tail_towards_head(head2, tail2)
		self.assertEqual(exp_result_x2, result2.x)
		self.assertEqual(exp_result_y2, result2.y)

	def test_process_move_set_right(self):
		head = solution.RopeNode(2, 1)
		tail = solution.RopeNode(1, 1)
		visited = {}
		direction = "R"
		num_moves = 4
		exp_head_x = 6
		exp_y = 1
		exp_tail_x = 5 
		solution.process_move_set(head, tail, visited, direction, num_moves)

		self.assertEqual(exp_head_x, head.x)
		self.assertEqual(exp_tail_x, tail.x)
		self.assertEqual(exp_y, head.y)
		self.assertEqual(exp_y, tail.y)
		self.assertEqual(len(visited.keys()), 4)

	def test_process_move_set_up(self):
		head = solution.RopeNode(1, 2)
		tail = solution.RopeNode(1, 1)
		visited = {}
		direction = "U"
		num_moves = 4
		exp_head_x = 1
		exp_head_y = 6
		exp_tail_x = 1
		exp_tail_y = 5 
		solution.process_move_set(head, tail, visited, direction, num_moves)

		self.assertEqual(exp_head_x, head.x)
		self.assertEqual(exp_tail_x, tail.x)
		self.assertEqual(exp_head_y, head.y)
		self.assertEqual(exp_tail_y, tail.y)
		self.assertEqual(len(visited.keys()), num_moves)

	def test_process_move_set_left(self):
		head = solution.RopeNode(1, 1)
		tail = solution.RopeNode(2, 1)
		visited = {}
		direction = "L"
		num_moves = 3
		exp_head_x = -2
		exp_head_y = 1
		exp_tail_x = -1
		exp_tail_y = 1
		solution.process_move_set(head, tail, visited, direction, num_moves)

		self.assertEqual(exp_head_x, head.x)
		self.assertEqual(exp_tail_x, tail.x)
		self.assertEqual(exp_head_y, head.y)
		self.assertEqual(exp_tail_y, tail.y)
		self.assertEqual(len(visited.keys()), num_moves)

	def test_process_move_set_down(self):
		head = solution.RopeNode(1, 1)
		tail = solution.RopeNode(1, 2)
		visited = {}
		direction = "D"
		num_moves = 1
		exp_head_x = 1
		exp_head_y = 0
		exp_tail_x = 1
		exp_tail_y = 1 
		solution.process_move_set(head, tail, visited, direction, num_moves)

		self.assertEqual(exp_head_x, head.x)
		self.assertEqual(exp_tail_x, tail.x)
		self.assertEqual(exp_head_y, head.y)
		self.assertEqual(exp_tail_y, tail.y)
		self.assertEqual(len(visited.keys()), num_moves)

	def test_process_all_move_sets(self):
		head = solution.RopeNode(0, 0)
		tail = solution.RopeNode(0, 0)
		visited = {}
		exp_head_x = 2
		exp_head_y = 2
		exp_tail_x = 1
		exp_tail_y = 2
		solution.process_all_move_sets(self.data, head, tail, visited)

		self.assertEqual(exp_head_x, head.x)
		self.assertEqual(exp_head_y, head.y)
		self.assertEqual(exp_tail_x, tail.x)
		self.assertEqual(exp_tail_y, tail.y)
		self.assertEqual(len(visited.keys()), 12)

	def test_calculate_num_unique_locations_tail_visits(self):
		exp_result = 13
		result = solution.calculate_num_unique_locations_tail_visits(self.data)

		self.assertEqual(exp_result, result)

	def test_process_all_move_sets_long_rope(self):
		rope = []
		for i in range(10):
			rope.append(solution.RopeNode(0, 0))
		visited = {}
		exp_head_x = 2
		exp_head_y = 2
		exp_tail_x = 0
		exp_tail_y = 0
		exp_num_visited = 0
		solution.process_all_move_sets_long_rope(self.data, rope, visited)

		self.assertEqual(exp_head_x, rope[0].x)
		self.assertEqual(exp_head_y, rope[0].y)
		self.assertEqual(exp_tail_x, rope[-1].x)
		self.assertEqual(exp_tail_y, rope[-1].y)
		self.assertEqual(len(visited.keys()), exp_num_visited)

	def test_process_all_move_sets_long_rope_long_data(self):
		rope = []
		for i in range(10):
			rope.append(solution.RopeNode(0, 0))
		visited = {}
		exp_head_x = -11
		exp_head_y = 15
		exp_tail_x = -11
		exp_tail_y = 6
		exp_num_visited = 35
		solution.process_all_move_sets_long_rope(self.long_data, rope, visited)

		self.assertEqual(exp_head_x, rope[0].x)
		self.assertEqual(exp_head_y, rope[0].y)
		self.assertEqual(exp_tail_x, rope[-1].x)
		self.assertEqual(exp_tail_y, rope[-1].y)
		self.assertEqual(len(visited.keys()), exp_num_visited)

	def test_calculate_num_unique_locations_tail_visits_long_rope(self):
		exp_result = 36
		num_nodes = 10
		result = solution.calculate_num_unique_locations_tail_visits_long_rope(self.long_data, num_nodes)

		self.assertEqual(exp_result, result)
