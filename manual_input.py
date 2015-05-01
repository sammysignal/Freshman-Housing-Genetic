from helpers import *

# Settings

DORM_NAME = "Apley"
INPUT_FILE = "csv/manual_input.csv"
OUTPUT_FILE


# get the number of students that fit into the dorm.
d_size = dorm_size_by_name(dorm_name)

# generate that many students.
students = import_students(INPUT_FILE)

# generate a single scheme
scheme = generate_scheme(dorm_name, students)




