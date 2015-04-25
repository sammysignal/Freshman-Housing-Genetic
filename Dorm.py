import Room, Student, Helpers, Layouts
import random

# Class that descibes a dorm.
class Dorm:

	# initializes a Dorm with the size.
	def __init__(self, name, rooms, accessible=False):
		self.name = name
		self.rooms = rooms
		self.accessible = accessible
		self.has_fitness = False
		self.fitness = None

	# Gets the fitness value of the dorm based on its students.
	def dorm_fitness(self):
		total = 0
		# Sum all the fitnesses of individual rooms, weighted by
		# number of people in each room, then divide by total
		# size of that dorm to get a weighted average fitness.
		for room in self.rooms:
			total = total + (room.room_fitness() * room.size)

		# Once done, set fitness value so it
		# does not have to be calculated again
		f = (total / (float(self.count_students)))
		self.has_fitness = True
		self.fitness = f
		return f

	def count_rooms(self):
		return len(self.rooms)

	def count_students(self):
		s = 0
		for room in self.rooms:
			s = s + room.size
		return s

	# Mutates dorm and returns a brand spanking new dorm
	# with slight modifications, namely that two students
	# of the same gender have been switched between rooms
	# CRUCIAL FUNCTION
	
	# def mutate(dorm_name):
	# 	student_a, student_b = random.sample(Dorm.Dorm(rooms), 2)
	# 	a[student_a], a[student_b] = a[student_b], a[student_a]

		
	# 	student_gender = [item for item in self.rooms if item[0] = male]
	# 	random.sample(student_gender, 2)

	# 	student_a = random.choice(self.rooms)
	# 	student_b = random.choice(self.rooms)

	# 	new_dorm = [item for item in new_dorm if item[2] >= 5 or item[3] >= 0.3]

	
		


def run_tests():
	pass

run_tests()
