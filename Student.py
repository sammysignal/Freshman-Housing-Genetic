import random, Dorm, Room

# Class that descibes a student and his/her attributes.
class Student:

	# initializes a 'student' with the following values.
	def __init__(self):
		# gender either 'm', 'f', or 'o' for other/DNS
		# Initialize to male, because Harvard does have more
		# male students than female students.
		self.gender = 'm'

		# Sleep schedule. On a scale from 1 to 10, 0 being early to bed
		# early to rise, and 10 being a night owl.
		self.sleep = 5

		# size pref referring to preferred number of roommates. subject
		# to change. Assume number of roomates ranges from 0 to 3
		# (is that necessarily the case? Look into room setup for dorms)
		self.roommates = 1

		# Self-perceived cleanliness, on a scale from 1 to 10.
		self.cleanliness = 5

		# Self-perceived socialness/extrovertedness, on a 
		# scale from 1 to 10.
		self.sociability = 5


# Generates a list of 100 random gender-specified students. 
def hundred_students():
	lst = []
	for i in range(100):
		st = Student()
		male = ('m' if (random.random() > .500000) else 'f')
		r = int(random.random() * 4)
		sl = int(random.random() * 10) + 1
		c = int(random.random() * 10) + 1
		soc = int(random.random() * 10) + 1
		st.gender = male
		st.sleep = sl
		st.roommates = r
		st.cleanliness = c
		st.sociability = soc
		lst.append(st)
	return lst


# Quick test to show you how class attributes are accesses/changed.
def attribute_test():
	Sammy = Student()
	assert (Sammy.cleanliness == 5)
	Sammy.cleanliness = 10
	assert (Sammy.cleanliness == 10)


def test_hundred_students():
	a = hundred_students()
	assert (len(a) == 100)

def run_tests():
	attribute_test()
	test_hundred_students()

run_tests()
