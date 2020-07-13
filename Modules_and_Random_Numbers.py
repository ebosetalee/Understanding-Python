# The Random Module implements pseudo-random number generators for different distributors.
# In other words, Rando, module provides access to functions that support many operations.
# but importantly, it allows you to generate random numbers.
# Before using random, you must type "import random" at the beginning or top of file;
# which means you are allowing Python program to use a module called random in the rest of the code.  
import random
# Other functions under Random is:
# a. Randint: a function used to generate random integer Using 2 parameter i.e(start, stop)
print(random.randint(1,9))
# b. random: to generate a larger number or a random floating number , by mutiplying it
print(random.random()*100)
# c. uniform: generates a random floating number (a,b) where b may or maynot be included
print(random.uniform(0,2))
# d. randrange: generates a randomly selected element from range(start, stop, step)stated as randrange(start,
#               stop, step) equivalent to choice(range(start, stop,step)).
print(random.randrange(0, 101, 5))
# e. choice: returns a random element from the non-empty sequence(statements or words).
myList = [2,"anna", "God Mother", 24, 26, "Raymond"]
print(random.choice(myList))
# f. shuffle: seen as (random.shuffle(x,[random])): thus shuffle the sequence x in place. To shuffle an 
#            unchanging sequence and return a new shuffled list, use sample(x, k = len(x)). Use import random
#            or "from random import shuffle".
from random import shuffle
x = [i for i in range(20)]
shuffle(x)
print(x)
# g. sample: e.g (random.sample(poluation, k)): it returns a  k length list of unique elements chosen from
#           polulation sequence or set. In other words, it creates a new list containing elements from a
#           given sequence without changing the original sequence. Thus, its Used for random 
#           sampling without replacement.
a = random.sample(range(100),10)
print(a)
# Note that : s.count(x) means total number of occurences of x in s
# Remeber min(s) means smallest item in s and max(s) means largest item in s
