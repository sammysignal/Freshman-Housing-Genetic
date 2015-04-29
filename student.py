
# Class that descibes a student and his/her attributes.
class Student:

	# initializes a 'student' with the following values.
	def __init__(self, gender='m', sleep=5, roommates=0, cleanliness=5, sociability=5, student_id=0):
		# gender either 'm', 'f', or 'o' for other/DNS
		self.gender = gender

		# Sleep schedule. On a scale from 1 to 10, 1 being early to bed
		# early to rise, and 10 being a night owl.
		self.sleep = sleep

		# size pref referring to preferred number of roommates. subject
		# to change. Assume number of roomates ranges from 0 to 5
		# (is that necessarily the case? Look into room setup for dorms)
		self.roommates = roommates

		# Self-perceived cleanliness, on a scale from 1 to 10.
		self.cleanliness = cleanliness

		# Self-perceived socialness/extrovertedness, on a 
		# scale from 1 to 10.
		self.sociability = sociability


		self.student_id = student_id
		
