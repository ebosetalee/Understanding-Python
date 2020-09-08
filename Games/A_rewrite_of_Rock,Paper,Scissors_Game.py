rock = 0
scissors = 2
paper = 5

import random
from random import shuffle
x = [i for i in range(0,15,3)]
print(random.shuffle(x))

shuffle(x)
print(x)

y = [0,3,6,9,12,15]
print(shuffle(y))
shuffle(y)
print(y)
