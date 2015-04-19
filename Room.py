import Dorm, Student

# Class that descibes a room in a dorm.
class Room:

	# initializes a Room with the size. student list is passed in.
	def __init__(self, students):
		self.students = students
		self.size = len(students)

	## Gets the fitness for a given room. 
	# To do this, the function finds the given compatibility of any
	# two students within the room, and then averages all of those
	# compatibility levels. Thus, for a double there will be one
	# compatibility value which also represents the fitness of the 
	# room. In a room with three people, there will be three
	# compaitibility values, and these must be averaged to get the
	# total fitness of the room. 
	## A room with n students will have n-choose-2 compatibility values.
	# TODO what is the fitness of a single? Sammy thinks we should
	# 	not even take singles into consideration.
	# Use Helpers.n_choose_2(), and Helpers.compatibility(a, b)
	# CRUCIAL FUNCTION
	def room_fitness(self):
		pass

def run_tests():
	pass

run_tests()
