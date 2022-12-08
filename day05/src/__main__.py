from src import solution


print("Do you want solution 1 or solution 2?")
user_choice = input("1 or 2: ")

if user_choice == "1":
	solution.run_solution_1("input.txt")
elif user_choice == "2":
	solution.run_solution_2("input.txt")
else:
	print("Not a valid selection. Please enter 1 for solution 1 or 2 for solution 2.")