import sqlite3

class BlogModel():
	def __init__ (self, db_file):
	self.db_file = db_file

	self.first_name = None
	self.last_name = None

def open(self):
	self.data = squlite3.connect(self.db_file)

def create_person_table(self):
	cursor = self.data.cursor()
	cursor.execute('''CREATE TABLE posts(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT)''')
	self.data.commit()

def create(self, first_name, last_name):
	cursor = self.data.cursor()	
	cursor.execute('''INSERT INTO posts(first_name, last_name) VALUES (?,?)''', 
(first_name, last_name))
	self.data.commit()

# def update(self, id, first_name, last_name):	
# 	cursor = self.data.cursor()
# 	cursor.execute('''UPDATE posts SET first_name = ?, last last_name = ? WHERE id = ?''', (first_name, last_name, id))

def create_pet_table(self):
	cursor = self.data.cursor()
	cursor.execute('''CREATE TABLE posts(id INTEGER PRIMARY KEY, pet_name TEXT, 
pet_species TEXT, pet_breed TEXT, person_id TEXT)''')
	self.data.commit()

def create_table_called_pets(self):
	cursor = self.data.cursor()
	cursor.execute('''CREATE TABLE posts(id INTEGER PRIMARY KEY, pet_name TEXT, 
pet_species TEXT, pet_breed TEXT)''')
	self.data.commit()



