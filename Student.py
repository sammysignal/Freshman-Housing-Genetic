import Dorm, Room

# Class that descibes a student and his/her attributes.
class Student:

	# initializes a 'student' with the following values.
	def __init__(self, gender, sleep, roommates, cleanliness, sociability):
		# gender either 'm', 'f', or 'o' for other/DNS
		self.gender = gender

		# Sleep schedule. On a scale from 1 to 10, 0 being early to bed
		# early to rise, and 10 being a night owl.
		self.sleep = sleep

		# size pref referring to preferred number of roommates. subject
		# to change. Assume number of roomates ranges from 0 to 3
		# (is that necessarily the case? Look into room setup for dorms)
		self.roommates = roommates

		# Self-perceived cleanliness, on a scale from 1 to 10.
		self.cleanliness = cleanliness

		# Self-perceived socialness/extrovertedness, on a 
		# scale from 1 to 10.
		self.sociability = sociability



