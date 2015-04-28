# Application of a Genetic Algorithm to Rooming Optimization

## Introduction and Overview 
The essential problem that this project will address is that of optimizing a variety of preferences and requirements within certain constraints. In other words, finding an “ideal” solution among many, many possibilities. In this case, we will be applying a genetic algorithm to best sort incoming Harvard freshman into rooming accommodations that fit their preferences, not just with regard to the rooms themselves but also with regard to their roommates. 

Before matriculating at Harvard, all incoming freshman are required to take a housing survey. Data points from this survey will be used to best match students with rooms and roommates. Our goal is to apply a genetic algorithm to this process to achieve an “optimized” assignment scheme that best satisfies student preferences. Provided the aforementioned data points, the algorithm will first create a population of a number of random solution candidates. The fitness of each of the candidates will be assessed, after which a new population will be created by breeding the fittest candidates. Once a certain fitness level is reached, or a certain number of population “breedings” in reached, a final rooming configuration will be submitted.

## Contents

**Student.py** contains the student class, which has important attributes that will determine the level of compatability between different students.

**Room.py** contains the room class, which contains a list of students, and thus has a given fitness level that corresponds to the relationship between the students in that room.

**Dorm.py** contains the dorm class, which is the level we are operating mutations and crossovers on. dorms contain a list of rooms

**Helpers.py** Has a lot of core functionality in the following functions
  - crossover
  	- Crossover occurs between two schemes of the same dorm. 
  	- The "DNA" for a given schema can be interpreted as a list of student_ids.
  	  - Thus, what does crossing over actually mean in our schema?
  - Tests
  	- Test your own function

  - interface
  	1. file called input.csv 
  	2. input function
  		- reads a csv file and converts it to a list of student objects.
  	3. output function
  		- takes a Dorm scheme and displays it as a csv file
  	4. python students -> csv students
  		- used with generate_students. Takes a list of student objects and writes to a csv file in the same format as the input function requires.
  	
### Optional
	1. More dorms
	2. Test against other algorithm



