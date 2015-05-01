from helpers import *
import sys

# Settings

DORM_NAME = "Apley"
INPUT_FILE = "csv/auto_input.csv"
OUTPUT_FILE = "csv/auto_output.csv"

MAX_ITER = 100

MIN_FIT = 9.0

population_size = 50



# get the number of students that fit into the dorm.
d_size = dorm_size_by_name(DORM_NAME)

# generate that many students.
#students = import_students(INPUT_FILE)

students = generate_students(d_size)

# generate a single scheme
scheme_list = [generate_scheme(DORM_NAME, students) for i in range(population_size)]
#print(scheme_list[0].fitness)
iters = 0
while iters < MAX_ITER:
	print iters
	crossovers = []
	for i in range(population_size):
		val = crossover(scheme_list[0], scheme_list[1])
		crossovers.append(val)
		first = scheme_list.pop(0)
		scheme_list.append(first)

	to_mutate = scheme_list + crossovers

	#display_output(scheme_list[0],'csv/output.csv')

	#to_mutate = scheme_list

	mutations = [mutate(i) for i in to_mutate]
	

	result_list = mutations + to_mutate

	result_list.sort(key=lambda x: x.fitness, reverse=True)
	print(result_list[0].fitness)
	if result_list[0].fitness > MIN_FIT:
		break

	sys.stdout.flush()

	scheme_list = result_list[:population_size]


	iters = iters + 1


# end of loop


display_output(result_list[0], OUTPUT_FILE)






