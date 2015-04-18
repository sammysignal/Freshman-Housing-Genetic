import Dorm, Student, Room
# Helper functions


# In our implementation, Dorms get crossed over,
# and then mutated, emulating actual genetics.

# returns crossover
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


