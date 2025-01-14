# What does this piece of code do?
# Answer:do the loop for 10 times, print the number that the last time produced in a random integer between 1 and 100
#progress+=1 means valuable"progress=progress+1" for each time
#we import two packages(or functions) from 2 source.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
while progress<10:
	progress+=1
	n = randint(1,100)

print(n)
