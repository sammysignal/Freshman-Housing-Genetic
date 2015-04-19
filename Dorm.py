import Room, Student, Helpers, Layouts

# Class that descibes a dorm.
class Dorm:

	# initializes a Dorm with the size.
	def __init__(self, name, rooms, accessible=False):
		self.name = name
		self.rooms = rooms
		self.accessible = False
		self.has_fitness = False

	# Gets the fitness value of the dorm based on its students.
	def dorm_fitness(self):
		self.has_fitness = True
		total = 0
		# Sum all the fitnesses of individual rooms, weighted by
		# number of people in each room, then divide by total
		# size of that dorm to get a weighted average fitness.
		for room in self.rooms:
			total = total + (room.room_fitness() * room.size)

		return (total / (float(self.count_students)))


		# evaluate fitness. Once done, set fitness value so it
		# does not have to be calculated again
		#self.fitness =  TODO

	def count_rooms(self):
		return len(self.rooms)

	def count_students(self):
		s = 0
		for room in self.rooms:
			s = s + room.size
		return s

	# Mutates dorm and returns a brand spanking new dorm
	# with slight modifications.
	# CRUCIAL FUNCTION
	def mutate(self):
		pass


def run_tests():
	pass

run_tests()
