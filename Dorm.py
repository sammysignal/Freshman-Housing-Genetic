import Room, Student

# Class that descibes a dorm.
class Dorm:

	# initializes a Dorm with the size.
	def __init__(self, rooms, accessible=False):
		self.rooms = rooms
		self.accessible = False

	# Gets the fitness value of the dorm based on its students
	def get_fitness(self):
		pass

	# Mutates dorma nd returns a brand spanking new dorm, with slight modifications
	def mutate(self):
		pass


def run_tests():
	pass

run_tests()
