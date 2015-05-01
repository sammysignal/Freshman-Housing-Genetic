import student
from helpers import compatibility, n_choose_2
import copy

# Class that descibes a room in a dorm.
class Room:

	# initializes a Room with the size. student list is passed in.
	def __init__(self, students, room_id=0):
		self.students = students
		self.size = len(students)
		self.room_id = room_id
		self.fitness = self.room_fitness()

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
	# CRUCIAL FUNCTION
	def room_fitness(self):
		from helpers import display_student
		if self.size == 1:
			return compatibility(student.Student(), student.Student())
		total = 0
		st = copy.deepcopy(self.students)
		print self.students
		for i in range(self.size - 1):
			last = st.pop()
			for comp in st:
				print comp
				print last
				display_student(comp)
				display_student(last)
				total = total + compatibility(last, comp)
			#st.insert(0, last)
		val = (total / float(n_choose_2(self.size)))
		self.fitness = val
		return val




#def run_tests():
#	pass

#run_tests()
