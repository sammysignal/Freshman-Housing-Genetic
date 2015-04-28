import Room, Dorm, Layouts
from Helpers import *
import sys

# Dorm name.
dorm_name = "Apley"

# get the number of students that fit into the dorm.
d_size = dorm_size_by_name(dorm_name)

# generate that many students.
students = generate_students(d_size)

# generate a single scheme
scheme = generate_scheme(dorm_name, students)

mutations = []
mutations.append(scheme)
for i in range(100):
	mutations.append(mutate(scheme))

for i in range(10):
	fittest = get_fittest(mutations)

	mutations = []
	for fit in fittest:
		for i in range(10):
			mutations.append(mutate(fit))

	for fit in fittest:
		mutations.append(fit)

	print((str(i+1)) + " iterations done.")
	sys.stdout.flush()


