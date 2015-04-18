import Room, Student

# Class that descibes a dorm.
class Dorm:

	# initializes a Dorm with the size.
	def __init__(self, rooms, accessible=False):
		self.rooms = rooms
		self.accessible = False
		self.has_fitness = False

	# Gets the fitness value of the dorm based on its students
	def get_fitness(self):
		self.has_fitness = True

		# evaluate fitness. Once done, set fitness value so it
		# does not have to be calculated again

		#self.fitness =  TODO


	# Mutates dorma nd returns a brand spanking new dorm, with slight modifications
	def mutate(self):
		pass


def run_tests():
	pass

run_tests()
