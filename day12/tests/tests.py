import unittest
from pathlib import Path

from src import solution


class AoC_2022_Puzzle_12_Tests(unittest.TestCase):

	def setUp(self):
		filepath = Path(__file__).parent / "test_input.txt"
		with open(filepath, "r", encoding="utf8", newline=None) as file:
			self.data = file.readlines()

	def test_is_legal_move(self):
		node1 = solution.MapNode("a", 0, 0)
		node2 = solution.MapNode("b", 1, 0)
		node3 = solution.MapNode("c", 0, 1)
		node4 = solution.MapNode("a", 0, 1)

		self.assertTrue(solution.is_legal_move(node1, node2))
		self.assertTrue(solution.is_legal_move(node2, node1))
		self.assertFalse(solution.is_legal_move(node1, node3))
		self.assertTrue(solution.is_legal_move(node3, node1))
		self.assertTrue(solution.is_legal_move(node1, node4))

	def test_construct_path(self):
		node1 = solution.MapNode("a", 0, 0)
		node2 = solution.MapNode("b", 1, 0)
		node3 = solution.MapNode("c", 2, 0)
		node3.prev_node = node2
		node2.prev_node = node1
		node3.is_end = True
		node1.is_start = True
		path = solution.construct_path(node3)

		self.assertEqual(path[0].get_location(), (0,0))
		self.assertEqual(path[1].get_location(), (0,1))
		self.assertEqual(path[2].get_location(), (0,2))

	def test_create_map(self):
		start_node_elev = "a"
		start_node_col = 0
		start_node_row = 0
		end_node_elev = "z"
		end_node_col = 5
		end_node_row = 2
		last_node_r2_elev = "l"
		last_node_r2_col = 7
		last_node_r2_row = 1

		height_map, result_start_node, result_end_node = solution.create_map(self.data)

		node_start = height_map[0][0]
		self.assertEqual(node_start, result_start_node)
		self.assertEqual(start_node_elev, node_start.elevation)
		self.assertEqual(start_node_col, node_start.col)
		self.assertEqual(start_node_row, node_start.row)
		self.assertTrue(node_start.is_start)
		self.assertFalse(node_start.is_end)

		node_end = height_map[2][5]
		self.assertEqual(node_end, result_end_node)
		self.assertEqual(end_node_elev, node_end.elevation)
		self.assertEqual(end_node_col, node_end.col)
		self.assertEqual(end_node_row, node_end.row)
		self.assertFalse(node_end.is_start)
		self.assertTrue(node_end.is_end)

		node_r2 = height_map[1][7]
		self.assertEqual(last_node_r2_elev, node_r2.elevation)
		self.assertEqual(last_node_r2_col, node_r2.col)
		self.assertEqual(last_node_r2_row, node_r2.row)
		self.assertFalse(node_r2.is_start)
		self.assertFalse(node_r2.is_end)

	def test_get_node_neighbors(self):
		height_map, start_node, end_node = solution.create_map(self.data)
		other_node = height_map[4][7]

		exp_start_neighbors = [height_map[0][1], height_map[1][0]]
		exp_end_neighbors = [height_map[2][4], height_map[1][5], height_map[2][6], height_map[3][5]]
		exp_other_neighbors = [height_map[4][6], height_map[3][7]]

		self.assertEqual(exp_start_neighbors, solution.get_node_neighbors(height_map, start_node))
		self.assertEqual(exp_end_neighbors, solution.get_node_neighbors(height_map, end_node))
		self.assertEqual(exp_other_neighbors, solution.get_node_neighbors(height_map, other_node))

	def test_calculate_path(self):
		height_map, start_node, end_node = solution.create_map(self.data)
		exp_num_steps = 31

		result_node = solution.calculate_path(height_map, start_node, end_node)

		self.assertEqual(result_node, end_node)
		self.assertTrue(result_node.visited)
		self.assertEqual(exp_num_steps, result_node.cost_to_reach)

	def test_get_shortest_path(self):
		height_map, start_node, end_node = solution.create_map(self.data)
		exp_result = 31
		result = solution.get_shortest_path(height_map, start_node, end_node)
		
		self.assertEqual(exp_result, result)

	def test_get_all_nodes_of_height(self):
		height_map, start_node, end_node = solution.create_map(self.data)
		desired_height = "a"
		exp_result = [height_map[0][0], height_map[0][1], height_map[1][0], height_map[2][0], height_map[3][0], height_map[4][0]]
		result = solution.get_all_nodes_of_height(height_map, desired_height)

		self.assertEqual(exp_result, result)

	def test_reset_map_and_set_new_start(self):
		height_map, start_node, end_node = solution.create_map(self.data)
		new_start = height_map[2][0]
		solution.calculate_path(height_map, start_node, end_node)
		result_map = solution.reset_map_and_set_new_start(height_map, start_node, new_start)

		for row in result_map:
			for node in row:
				if node == new_start:
					self.assertTrue(node.is_start)
					self.assertEqual(node.cost_to_reach, 0)
				else:
					self.assertFalse(node.is_start)
					self.assertEqual(node.cost_to_reach, -1)
				if node == end_node:
					self.assertTrue(node.is_end)
				self.assertFalse(node.visited)
				self.assertEqual(node.prev_node, None)

	def test_get_shortest_path_all_possible_starts(self):
		exp_result = 29
		result = solution.get_shortest_path_all_possible_starts(self.data)

		self.assertEqual(exp_result, result)

