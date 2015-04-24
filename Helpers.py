import Dorm, Student, Room, Layouts
import random

## Helper functions ##

# gets the number of students that can fit in a dorm by
# the name of that dorm. See Layouts.py.
def dorm_size_by_name(dorm_name):
	total = 0
	dorm_scheme = Layouts.layouts[dorm_name]
	room_size = 1
	for num in dorm_scheme:
		total = total + (room_size * num)
		room_size = room_size + 1
	return total

# Generates a random Dorm scheme given the name of
# the dorm, and a list of students.
# CRUCIAL FUNCTION
def generate_scheme(dorm_name, students):
	# first we need to grab students and build
	# a random list of rooms  by gender.
	if dorm_size_by_name(dorm_name) != len(students):
		raise Exception("Dorm size and number of students don't match")
	rooms = []
	dorm_scheme = Layouts.layouts[dorm_name]
	room_size = 1
	for num in dorm_scheme:
		for i in range(num):
			students_per_room = []
			for i in range(room_size):
				students_per_room.append(students.pop())
			rooms.append(Room.Room(students_per_room))
		room_size = room_size + 1

	return Dorm.Dorm(dorm_name, rooms, Layouts.accessible[dorm_name])
	

# In our implementation, Dorms get crossed over,
# and then mutated, emulating actual genetics.

# returns crossover of two dorm schemes
# CRUCIAL FUNCTION
def crossover(dorm_a, dorm_b):
	pass

# Takes in a dorm, and mutates it. Actual
# implementation can be found in Dorm.py.
def mutate(d):
	return d.mutate()

# Gets the fittest 10% of dorm schemes in a list of
# filled dorms. Returns items in a list.
def get_fittest(dorm_lst):
	if dorm_lst == []:
		return []
	for d in dorm_lst:
		if not d.has_fitness:
			# does this change the objects in the list
			# in place?
			d.get_fitness()

	# sort list descending by fitness value
	dorm_lst.sort(key=lambda x: x.fitness, reverse=True)
	num = (len(dorm_lst) / 10)
	if num == 0:
		return dorm_lst[0]
	else:
		ret = []
		for i in range(num):
			ret.append(dorm_list[i])
		return ret


# Determines the compatibility level of a given two students.
# Gender should be weighted higher than every other student
# attribute.
# CRUCIAL FUNCTION
def compatibility(student_a, student_b):
	def gscore(x, y):
		if (x == y):
			return 10.0
		elif (x != y):
			return 0.0
	def pscore(x,y):
		return 10.0 - abs(float(x) - float(y))
	def rscore(x,y):
		return 10.0 - (2.0 * abs(float(x) - float(y)))
	a = (0.5 * gscore(student_a.gender, student_b.gender))
	b = (0.15 * pscore(student_a.sleep, student_b.sleep))
	c = (0.15 * pscore(student_a.cleanliness, student_b.cleanliness))
	d = (0.15 * pscore(student_a.sociability, student_b.sociability))
	e = (0.05 * rscore(student_a.roommates, student_b.roommates))
	return (a + b + c + d + e)

# Generates a list of n random students. 
def generate_students(n):
	lst = []
	for i in range(n):
		male = ('m' if (random.random() > .500000) else 'f')
		r = int(random.random() * 4)
		sl = int(random.random() * 10) + 1
		c = int(random.random() * 10) + 1
		soc = int(random.random() * 10) + 1
		s_id = i
		st = Student.Student(male, sl, r, c, soc, s_id)
		lst.append(st)
	return lst

# Could have written a combonation algorithm, but
# that would just be unneccessary calculation given
# that rooms have a limited size.
def n_choose_2(n):
	if n == 1:
		raise Exception("Attempted to choose 2 from 1")
	elif n == 2:
		return 1
	elif n == 3:
		return 3
	elif n == 4:
		return 6
	elif n == 5:
		return 10
	elif n == 6:
		return 15
	

#############
### tests ###
#############

def test_dorm_size_by_name():
	assert(dorm_size_by_name("Apley") == 34)

def test_generate_students():
	a = generate_students(100)
	assert (len(a) == 100)

def run_tests():
	test_dorm_size_by_name()
	test_generate_students()


run_tests()

