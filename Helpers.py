import Dorm, Student, Room, Layouts

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
# the dorm, and a list of students. The only specification 
# is that only people of the same gender are together
# in a room.
# CRUCIAL FUNCTION
def generate_scheme(dorm_name, students):
	# first we need to grab students and build
	# a random list of rooms by gender.
	rooms = []
	dorm_scheme = Layouts.layouts[dorm_name]
	room_size = 1
	for num in dorm_scheme:
		for i in range(num):
			pass # TODO	

		room_size = room_size + 1
	

# In our implementation, Dorms get crossed over,
# and then mutated, emulating actual genetics.

# returns crossover of two dorm schemes
# CRUCIAL FUNCTION
def crossover(dorm_a, dorm_b):
	pass

def mutate(dorm):
	return dorm.mutate()

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

#############
### tests ###
#############

def test_dorm_size_by_name():
	assert(dorm_size_by_name("Apley") == 40)

def run_tests():
	test_dorm_size_by_name()


run_tests()

