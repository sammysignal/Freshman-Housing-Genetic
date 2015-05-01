import student, layouts
import random, copy, csv

## Helper functions ##

# gets the number of students that can fit in a dorm by
# the name of that dorm. See Layouts.py.
def dorm_size_by_name(dorm_name):
	total = 0
	dorm_scheme = layouts.Layouts[dorm_name]
	room_size = 1
	for num in dorm_scheme:
		total = total + (room_size * num)
		room_size = room_size + 1
	return total

# Generates a random Dorm scheme given the name of
# the dorm, and a list of students.
# CRUCIAL FUNCTION
def generate_scheme(dorm_name, students):
	import room, dorm
	from random import shuffle
	# first we need to grab students and build
	# a random list of rooms  by gender.
	students_copy = copy.deepcopy(students)
	if dorm_size_by_name(dorm_name) != len(students):
		raise Exception("Dorm size and number of students don't match")
	rooms = []
	dorm_scheme = layouts.Layouts[dorm_name]
	room_size = 1
	counter = 0
	shuffle(students)
	for num in dorm_scheme:
		for i in range(num):
			students_per_room = []
			for i in range(room_size):
				students_per_room.append(students_copy.pop())
			rooms.append(room.Room(students_per_room, counter))
			counter = counter + 1
		room_size = room_size + 1
	return dorm.Dorm(dorm_name, rooms, layouts.Accessible[dorm_name])
	

# In our implementation, Dorms get crossed over,
# and then mutated, emulating actual genetics.

# returns crossover of two dorm schemes
# CRUCIAL FUNCTION
def crossover(dorm_a, dorm_b):
	return dorm_a
	# TODOTODOTODOTODOTODOTODOTODOTODO
	# TODOTODOTODOTODOTODOTODOTODOTODO
	# TODOTODOTODOTODOTODOTODOTODOTODO


# Helper for mutate that takes two lists,
# and randomly switches two items. This alters
# the lists that were passed in, and thus does
# not have a return value.
def switch_items(list_a, list_b):
	to_b = list_a.pop(random.randrange(len(list_a)))
	to_a = list_b.pop(random.randrange(len(list_b)))
	list_a.append(to_a)
	list_b.append(to_b)
	return

# Mutates dorm and returns a brand spanking new dorm
# with slight modifications, namely that two students
# of the same gender have been switched between rooms
# CRUCIAL FUNCTION

# def mutate(self, dorm_name=""):
# 	student_a, student_b = random.sample(Dorm.Dorm(rooms), 2)
# 	a[student_a], a[student_b] = a[student_b], a[student_a]

	
# 	student_gender = [item for item in self.rooms if (item[0] == male)]
# 	random.sample(student_gender, 2)

# 	student_a = random.choice(self.rooms)
# 	student_b = random.choice(self.rooms)

# 	new_dorm = [item for item in new_dorm if item[2] >= 5 or item[3] >= 0.3]

## Sammy's attempt. ##
def mutate(d):
	drm = copy.deepcopy(d)
	weighted_rooms = []
	for rm in drm.rooms:
		for i in range(rm.size):
			weighted_rooms.append(rm)

	index = random.randrange(len(weighted_rooms))
	rm1 = weighted_rooms[index]
	index2 = random.randrange(len(weighted_rooms))
	while index == index2:
		index2 = random.randrange(len(weighted_rooms))

	rm2 = weighted_rooms[index2]

	switch_items(rm1.students, rm2.students)
	return drm

	# rm1 = weighted_rooms.pop(random.randrange(len(weighted_rooms)))
	# rm2 = weighted_rooms.pop(random.randrange(len(weighted_rooms)))
	# while (rm1 == rm2):
	# 	rm2 = weighted_rooms.pop(random.randrange(len(weighted_rooms)))
	# switch_items(rm1.students, rm2.students)
	# drm.dorm_fitness()
	# return drm

# Gets the fittest 10% of dorm schemes in a list of
# filled dorms. Returns items in a list.
def get_fittest(dorm_lst):
	if dorm_lst == []:
		return []

	# sort list descending by fitness value
	dorm_lst.sort(key=lambda x: x.fitness, reverse=True)
	num = (len(dorm_lst) / 10)
	if num == 0:
		return [dorm_lst[0]]
	else:
		ret = []
		for i in range(num):
			ret.append(dorm_lst[i])
		return ret

# Gets the one fittest dorm scheme in a list of
# filled dorms. Returns the dorm object.
def get_absolute_fittest(dorm_lst):
	if dorm_lst == []:
		return []

	# sort list descending by fitness value
	dorm_lst.sort(key=lambda x: x.fitness, reverse=True)
	return dorm_lst[0]


# Determines the compatibility level of a given two students.
# Gender should be weighted higher than every other student
# attribute.
# Rating system out of 10, with 10 being the best possible score
# CRUCIAL FUNCTION
def gscore(x, y):
	if (x == y):
		return 10.0
	else:
		return 0.0

def pscore(x,y):
	return (10.0 - abs(float(x) - float(y)))

def rscore(x,y):
	return (10.0 - (2.0 * abs(float(x) - float(y))))

def compatibility(student_a, student_b):
	a = (0.5 * gscore(student_a.gender, student_b.gender))
	b = (0.15 * pscore(student_a.sleep, student_b.sleep))
	c = (0.15 * pscore(student_a.cleanliness, student_b.cleanliness))
	d = (0.15 * pscore(student_a.sociability, student_b.sociability))
	e = (0.05 * rscore(student_a.roommates, student_b.roommates))
	result = (a + b + c + d + e)
	return result

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
		st = student.Student(male, sl, r, c, soc, s_id)
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

# takes a dorm scheme and creates a list of lists with 
# each student id and attribute
# skips header row 
# called 'input.csv'
# adopted from http://stackoverflow.com/questions/22242181/csv-row-import-into-python-array
# def import_dorm(input.csv):
# 	with open('input.csv') as f:
# 		data = csv.reader(f)
# 		skip = next(data)
# 		print [map(float, l) for l in cr] #not sure how to output an array but this will print it

# takes a csv file name and returns a list of students.
# csv format:
# STUDENT_ID | GENDER | SLEEP | ROOMMATES | CLEANLINESS | SOCIABILITY
def import_students(filename):
	with open(filename, 'rb') as f:
		reader = csv.reader(f)
		lst = list(reader)
		first = True
		student_lst = []
		for row in lst:
			if first != True:
				st = student.Student()
				for i in range(6):
					if i == 0:
						st.student_id = row[i]
					if i == 1:
						st.gender = row[i]
					if i == 2:
						st.sleep = row[i]
					if i == 3:
						st.roommates = row[i]
					if i == 4:
						st.cleanliness = row[i]
					if i == 5:
						st.sociability = row[i]
				student_lst.append(st)
			first = False
		return student_lst

# takes a list of students and writes them to a csv file.
# csv format:
# STUDENT_ID | GENDER | SLEEP | ROOMMATES | CLEANLINESS | SOCIABILITY
def export_students(student_list, filename):
	student_list.sort(key=lambda x: x.student_id, reverse=False)
	with open(filename, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["Student ID", "Gender", "Sleep", "Roommate Preference",
						"Cleanliness", "Sociability"])
		for st in student_list:
			writer.writerow(
				[st.student_id, st.gender, st.sleep, st.roommates, st.cleanliness, st.sociability]
			)
	f.close()

		
		
# takes a dorm scheme and displays it in a csv file
# called 'output.csv'.
# csv format:
# ROOM_ID | ROOM_SIZE | STUDENT_ID
def display_output(d, filename):
	with open(filename, 'wb') as output:
	    student_writer = csv.writer(output, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

	    for rm in d.rooms:
	    	for st in rm.students:
	    		student_writer.writerow([rm.room_id, rm.size, st.student_id])

	    output.close()

def run_algorithm(student_list, dorm_name, cutoff=0.9, max_iter=100):
	population_size = 100
	schemes = [generate_scheme(dorm_name, student_list) for i in range(population_size)]
	for i in range(max_iter):
		schemes.sort(key=lambda x: x.fitness, reverse=True)




#############
### tests ###
#############
#gender='m', sleep=5, roommates=0, cleanliness=5, sociability=5, student_id=0):

def test_compatibility():
	a = student.Student('m',1,1,1,1,1)
	b = student.Student('m',1,1,1,1,2)
	c = student.Student('m',5,3,5,5,5)
	d = student.Student('m',10,5,10,10,10)
	e = student.Student('f',1,1,1,1,1)
	x = compatibility(a,b)
	y = compatibility(a,c)
	z = compatibility(a,d)
	k = compatibility(a,e)
	assert((x>y>z>k) == True)

	# Identical students should have 
	# ideal compatibility of 10.0
	assert(compatibility(a, a) > 9.99)

def test_dorm_size_by_name():
	assert(dorm_size_by_name("Apley") == 34)

def test_generate_students():
	a = generate_students(100)
	assert (len(a) == 100)

# def test_get_fittest():
# 	dorm_name = "Apley"
# 	sz = dorm_size_by_name(dorm_name)
# 	students = generate_students(sz)
# 	d = generate_scheme(dorm_name, students)
# 	print(d.dorm_fitness())

def run_tests():
	test_dorm_size_by_name()
	test_generate_students()
	test_compatibility()
	#test_get_fittest()

run_tests()

