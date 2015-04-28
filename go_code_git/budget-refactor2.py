
def print_commands():
	print "CSV Budget Application Commands"
	print "n: new"
 	print "o: open"
	print "a: add"
	print "c: calculate"
	print "v: view"
	print "s: save"
	print "d: delete"
	print "q: quit"

print_commands()

def user_interface():
	data_stored = []
	while True:

		user_command = raw_input("Give me a command. For example: 'o' 'a' etc. ")
		if user_command == "n":
			new_budget()
		if user_command == "o":
			open_budget(data_stored)
		if user_command == "v":
			view_budget(data_stored)	
		if user_command == "a":
			append_budget(data_stored)
		if user_command == "s":
			save_budget(data_stored)
		if user_command == "c":
			calc_budget(data_stored)	
		if user_command == "d":
			delete_budget(data_stored)
		if user_command == "q":
			print "Quit"
			break						
	

def new_budget():
	filename = raw_input("Enter filename: ")
	with open(filename, "w") as f:
		f.write("")	

def open_budget(data_stored):
	filename = raw_input("Enter filename: ")
	with open(filename, "r") as f:
		data_stored.extend(f.readlines())	

def view_budget(data_stored):
	filename = raw_input("Enter filename: ")
	with open(filename, "r") as f:
		print data_stored

def append_budget(data_stored):	
	add_item = raw_input("Add an item, amount, and 'y' or 'n' if it's a repeated monthly expense. ")
	return data_stored.append(add_item + "\n")
	
def save_budget(data_stored): 
	filename = raw_input("Enter filename: ")
	with open(filename, "w") as f:
		for x in data_stored: 
			f.write(x)

def delete_budget(data_stored):
	delete_item = int(raw_input("Which line you would like to delete? "))
	del data_stored[delete_item]
	print data_stored				
		
def calc_budget(data_stored):	
	amount_sum = 0
	for strings in data_stored:
		strings_to_array = strings.split(",")
		amounts = strings_to_array[1]
		amount_sum += float(amounts)
	print amount_sum
		
	
user_interface()

		
