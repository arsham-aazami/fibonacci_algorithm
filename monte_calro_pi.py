import math
import random

in_circle = 0
out_circle = 0

i = 0
while i < 10 ** 7:
	random_x = round(random.random(), 4)
	random_y = round(random.random(), 4)
	distance = math.sqrt(random_x ** 2 + random_y ** 2)
	if distance <= 1:
		in_circle += 1
	i += 1
pi = (in_circle / 10 ** 7) * 4
print(pi)
