# NOte:
# DST - Day Saving Time
# UTC = Coordinated Universal Time; aka Zulu time

# Python library provides 3 standard modules to deal with dates and times;
# time, datetime and calender modules. 

# epok - c libraries work by storing the number of seconds since start date i.e epok
# in Python, on Linux, WIndows and Mac this is January 1 1970. Dates before this are 
# represented by negative number. There's a probability those dates wont be handled. 
# Thus if dealing with historical dtaes, it's best to store them as strings


import time


print(time.gmtime(0))
# This specifies the number of seconds to zero, i.e gonna represent the start of the epoc
# gmtime function implements it into a tuple and GMT time always works in UTC. 

print(time.localtime())
# To get local time and converts the time in seconds as the start of epoc as well as into a tuple


print(time.time())
# This pretented ouut the number of seconds since the start of epoc. ie the number of seconds since
# the first in 1970

print(time.localtime(time.time()))
# this calls the time function 

print("==" * 40)

"""
The documentation for time states that the GMT time and local time, converts the 
number of seconds into a struct_time and thats actually named tuple.
They are like ordered tuples and allows individual items in a tuple to be 
accessed using a name.
"""

time_here = time.localtime() # to get the local time
print(time_here)


print("Year:", time_here[0], time_here.tm_year)
print("Month:", time_here[1], time_here.tm_mon)
print("Day:", time_here[2], time_here.tm_mday)


print("==" * 40)

"""
Creating a simple reaction time game; Once the game starts, it waits for a random
number of second before displaying a message on the screen, and it'll measure the 
time it takes the player to press enter.
Python provides a number of ways to measure the elapse time
"""

from time import perf_counter as my_timer 
# You can use time or perf_counter or monotonic
# perf_counter is the most precise clock used for bench marking codes
# another is monotonic function whcich behaves similarly, most times 
# difficult to see an differences between them  but perf_counter has a higher
# resolution on some systems. 
import random 


"""
If a clock is monotonic, it means that the time can't go backwards
and it's always rules out any adjustments as a result of daylight saving 
but also means that adjustments to the computer clock will not affect the 
times returned by a monotonic clock.

Another example is process_time which isn't appropraite for this because it 
returns the time that CPU spnds executing the current process rather than the
actual elapsed time. This is useful for profiling code and used by Python 
profile module.

Note that both perf_counter and process_time are monotonic. More in PEP 0418.
"""

input("Press enter to start")

wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = my_timer()

input("Press enter to stop")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))
# STR stands for String from time, used to format the local time tuple
# into a more readable form according to a format string.

print("Your reaction time was {} seconds".format(end_time - start_time))