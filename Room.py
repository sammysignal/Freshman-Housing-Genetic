import Dorm, Student

# Class that descibes a room in a dorm.
class Room:

	# initializes a Room with the size. student list is passed in.
	def __init__(self, students):
		self.students = students
		self.size = len(students)

	# Gets the fitness for a given room. 
	# CRUCIAL FUNCTION
	def room_fitness(self):
		pass

def run_tests():
	pass

run_tests()
