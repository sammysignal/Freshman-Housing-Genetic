import room, dorm, layouts
from helpers import *
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
fittest = None
for i in range(100):
	mutations.append(mutate(scheme))

for i in range(10):
	fittest = get_fittest(mutations)
	print("len(fittest) = " + str(len(fittest)))
	mutations = []
	for fit in fittest:
		for j in range(10):
			mutations.append(mutate(fit))

	for fit in fittest:
		mutations.append(fit)

	print((str(i+1)) + " iterations done.")
	sys.stdout.flush()
	fittest = get_absolute_fittest(mutations)
	print("Fittest fitness value is: " + str(fittest.dorm_fitness()))
	sys.stdout.flush()




