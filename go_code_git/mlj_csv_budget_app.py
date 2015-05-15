#print commands

def budget_commands():
	print "CSV Budget Commands"
	print "o: open"
	print "v: view and calculate"
	print "s: save"
	print "a: add an item"
	print "d: delete an item"
	print "q: quit"

budget_commands()

def user_commands():
	data_stored = []
	while True: 
		user_input = raw_input("Enter a command. For example 'o' 'a' etc. ")
		if user_input == "o":
			open_budget(data_stored)
		if user_input == "v":
			view_budget(data_stored)
		if user_input == "s":
			save_budget(data_stored)
		if user_input == "a":
			add_budget_item(data_stored)
		if user_input == "d":
			delete_budget_item(data_stored)
		if user_input == "q":
			print "Quit"
			break 

def open_budget(data_stored):
	existing_budget = raw_input("Are you opening an existing_budget? Y or N? ")
	if existing_budget == "y":
		filename = raw_input("Enter filename: ")
		with open(filename, "r") as f:
			data_stored.extend(f.readlines())
	else:
		filename = raw_input("What is the name for your new budget? ")
		with open(filename, "w") as f:
			f.write("")		

def view_budget(data_stored):
	print data_stored
	amount_sum = 0
	for strings in data_stored:
		strings_to_arrays = strings.split(",")
		amounts = strings_to_arrays[1]
		amount_sum += float(amounts)
	print "Total sum: $" + str(amount_sum)
	

def save_budget(data_stored):
	filename = raw_input("Enter filename: ")
	with open(filename, "w") as f:
		for x in data_stored:
			f.write(x)


def add_budget_item(data_stored):
	add_item = raw_input("Add an item, amount and 'y' or 'n' if the item is a repeated monthly expense. ")
	data_stored.append(add_item + "\n")
	print data_stored


def delete_budget_item(data_stored):
	delete_item = raw_input("Which line item would you like to delete? ")
	del data_stored[int(delete_item)]
	print data_stored


user_commands()
