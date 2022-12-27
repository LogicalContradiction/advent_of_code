import unittest
from pathlib import Path
import operator

from src import solution


class AoC_2022_Puzzle_11_Tests(unittest.TestCase):

	def setUp(self):
		filepath = Path(__file__).parent / "test_input.txt"
		with open(filepath, "r", encoding="utf8", newline=None) as file:
			self.data = file.readlines()

	def test_monkey_init_mul_other_op(self):
		id = 0
		starting_items = [79, 98]
		worry_operator = "*"
		other_operator = 19
		divisor_true = 2
		divisor_false = 3
		test_divisor = 23
		monkey = solution.Monkey(id, starting_items, worry_operator, other_operator, test_divisor, divisor_true, divisor_false)

		self.assertEqual(operator.mul, monkey.operation)
		self.assertFalse(monkey.use_worry_as_other_operator)

	def test_monkey_init_add_no_other_op(self):
		id = 7
		starting_items = [79, 60, 97]
		worry_operator = "+"
		other_operator = None
		divisor_true = 1
		divisor_false = 3
		test_divisor = 13
		monkey = solution.Monkey(id, starting_items, worry_operator, other_operator, test_divisor, divisor_true, divisor_false)

		self.assertEqual(operator.add, monkey.operation)
		self.assertTrue(monkey.use_worry_as_other_operator)

	def test_monkey_inspect(self):
		id = 0
		starting_items = [79, 98]
		worry_operator = "*"
		other_operator = 19
		divisor_true = 2
		divisor_false = 3
		test_divisor = 23
		exp_result = 500
		monkey = solution.Monkey(id, starting_items, worry_operator, other_operator, test_divisor, divisor_true, divisor_false)
		result = monkey.inspect()

		self.assertEqual(exp_result, result)
		self.assertEqual([98], list(monkey.items))
		self.assertEqual(monkey.num_inspections, 1)

	def test_monkey_get_monkey_id_to_throw_to(self):
		id = 0
		starting_items = [79, 98]
		worry_operator = "*"
		other_operator = 19
		divisor_true = 2
		divisor_false = 3
		test_divisor = 23
		exp_result = 3
		monkey = solution.Monkey(id, starting_items, worry_operator, other_operator, test_divisor, divisor_true, divisor_false)
		result = monkey.get_monkey_id_to_throw_to(500)

		self.assertEqual(exp_result, result)

	def test_monkey_do_single_item(self):
		id = 0
		starting_items = [79, 98]
		worry_operator = "*"
		other_operator = 19
		divisor_true = 2
		divisor_false = 3
		test_divisor = 23
		exp_result = (3, 500)
		monkey = solution.Monkey(id, starting_items, worry_operator, other_operator, test_divisor, divisor_true, divisor_false)
		result = monkey.do_single_item()

		self.assertEqual(exp_result, result)
		self.assertEqual([98], list(monkey.items))
		self.assertEqual(monkey.num_inspections, 1)

	def test_monkey_do_turn(self):
		id = 0
		starting_items = [79, 98]
		worry_operator = "*"
		other_operator = 19
		divisor_true = 2
		divisor_false = 3
		test_divisor = 23
		exp_result = [(3, 500), (3, 620)]
		monkey = solution.Monkey(id, starting_items, worry_operator, other_operator, test_divisor, divisor_true, divisor_false)
		result = monkey.do_turn()

		self.assertEqual(exp_result, result)
		self.assertEqual([], list(monkey.items))
		self.assertEqual(monkey.num_inspections, 2)

	def test_convert_input_to_monkey_other_op(self):
		id = 0
		starting_items = [79, 98]
		worry_operator = "*"
		other_operator = 19
		divisor_true = 2
		divisor_false = 3
		test_divisor = 23
		test_input = self.data[:6]
		monkey = solution.convert_input_to_monkey(test_input)

		self.assertEqual(monkey.id, id)
		self.assertEqual(list(monkey.items), starting_items)
		self.assertEqual(monkey.operation, operator.mul)
		self.assertEqual(monkey.other_operator, other_operator)
		self.assertFalse(monkey.use_worry_as_other_operator)
		self.assertEqual(monkey.test_divisor, test_divisor)
		self.assertEqual(monkey.divisor_true, divisor_true)
		self.assertEqual(monkey.divisor_false, divisor_false)
		self.assertEqual(monkey.num_inspections, 0)

	def test_convert_input_to_monkey_same_op(self):
		id = 2
		starting_items = [79, 60, 97]
		worry_operator = "*"
		other_operator = None
		divisor_true = 1
		divisor_false = 3
		test_divisor = 13
		test_input = self.data[14:20]
		monkey = solution.convert_input_to_monkey(test_input)

		self.assertEqual(monkey.id, id)
		self.assertEqual(list(monkey.items), starting_items)
		self.assertEqual(monkey.operation, operator.mul)
		self.assertTrue(monkey.use_worry_as_other_operator)
		self.assertEqual(monkey.test_divisor, test_divisor)
		self.assertEqual(monkey.divisor_true, divisor_true)
		self.assertEqual(monkey.divisor_false, divisor_false)
		self.assertEqual(monkey.num_inspections, 0)

	def test_create_all_monkies(self):
		id1 = 0
		starting_items1 = [79, 98]
		worry_operation1 = operator.mul
		other_operator1 = 19
		divisor_true1 = 2
		divisor_false1 = 3
		test_divisor1 = 23

		id3 = 3
		starting_items3 = [74]
		worry_operation3 = operator.add
		other_operator3 = 3
		divisor_true3 = 0
		divisor_false3 = 1
		test_divisor3 = 17

		result = solution.create_all_monkies(self.data)
		monkey1 = result[0]
		monkey3 = result[3]

		self.assertEqual(monkey1.id, id1)
		self.assertEqual(list(monkey1.items), starting_items1)
		self.assertEqual(monkey1.operation, worry_operation1)
		self.assertEqual(monkey1.other_operator, other_operator1)
		self.assertFalse(monkey1.use_worry_as_other_operator)
		self.assertEqual(monkey1.test_divisor, test_divisor1)
		self.assertEqual(monkey1.divisor_true, divisor_true1)
		self.assertEqual(monkey1.divisor_false, divisor_false1)
		self.assertEqual(monkey1.num_inspections, 0)
		
		self.assertEqual(monkey3.id, id3)
		self.assertEqual(list(monkey3.items), starting_items3)
		self.assertEqual(monkey3.operation, worry_operation3)
		self.assertEqual(monkey3.other_operator, other_operator3)
		self.assertFalse(monkey3.use_worry_as_other_operator)
		self.assertEqual(monkey3.test_divisor, test_divisor3)
		self.assertEqual(monkey3.divisor_true, divisor_true3)
		self.assertEqual(monkey3.divisor_false, divisor_false3)
		self.assertEqual(monkey3.num_inspections, 0)
		
	def test_simulate_rounds(self):
		monkies = solution.create_all_monkies(self.data)
		num_rounds = 20

		monkey0_exp_result = [10, 12, 14, 26, 34]
		monkey1_exp_result = [245, 93, 53, 199, 115]
		monkey2_exp_result = []
		monkey3_exp_result = []

		monkey0_inspect = 101
		monkey1_inspect = 95
		monkey2_inspect = 7
		monkey3_inspect = 105

		result = solution.simulate_rounds(monkies, num_rounds)

		self.assertEqual(list(result[0].items), monkey0_exp_result)
		self.assertEqual(list(result[1].items), monkey1_exp_result)
		self.assertEqual(list(result[2].items), monkey2_exp_result)
		self.assertEqual(list(result[3].items), monkey3_exp_result)

		self.assertEqual(monkey0_inspect, result[0].num_inspections)
		self.assertEqual(monkey1_inspect, result[1].num_inspections)
		self.assertEqual(monkey2_inspect, result[2].num_inspections)
		self.assertEqual(monkey3_inspect, result[3].num_inspections)

	def test_get_most_active_monkies(self):
		monkies = solution.create_all_monkies(self.data)
		num_rounds = 20
		final_monkies = solution.simulate_rounds(monkies, num_rounds)
		num_active_monkies = 2
		exp_num_inspections = [105, 101]
		exp_monkey_ids = [3, 0]
		result_num_inspections = solution.get_most_active_monkies_info(final_monkies, num_active_monkies, False)
		result_monkey_ids = solution.get_most_active_monkies_info(final_monkies, num_active_monkies, True)

		self.assertEqual(exp_num_inspections, result_num_inspections)
		self.assertEqual(exp_monkey_ids, result_monkey_ids)

	def test_calculate_monkey_business(self):
		monkies = solution.create_all_monkies(self.data)
		num_rounds = 20
		final_monkies = solution.simulate_rounds(monkies, num_rounds)
		num_active_monkies = 2
		num_inspections = solution.get_most_active_monkies_info(final_monkies, num_active_monkies, False)
		exp_result = 10605
		result = solution.calculate_monkey_business(num_inspections)

		self.assertEqual(exp_result, result)