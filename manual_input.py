from helpers import *
import sys, copy

# Settings

DORM_NAME = "Apley"
INPUT_FILE = "csv/manual_input.csv"
OUTPUT_FILE = "csv/manual_output.csv"

MAX_ITER = 100

MIN_FIT = 9.0

population_size = 50


# generate that many students.
st = copy.deepcopy(import_students(INPUT_FILE))

# generate a list of schemes
scheme_list = [generate_scheme(DORM_NAME, st) for i in range(population_size)]

iters = 0
while iters < MAX_ITER:
	print(iters)
	crossovers = []
	for i in range(population_size):
		val = crossover(scheme_list[0], scheme_list[1])
		crossovers.append(val)
		first = scheme_list.pop(0)
		scheme_list.append(first)

	to_mutate = scheme_list + crossovers

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

print("Wrote result to " + OUTPUT_FILE)
display_output(result_list[0], OUTPUT_FILE)







