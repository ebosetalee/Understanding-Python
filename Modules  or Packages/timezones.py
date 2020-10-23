""" NOte: Tutor in Australia:
With datetime module and time module, we can get information
on time zone and current time zone using time.timezone and time.tzedname

These aren't functions timezone returns a number of seconds offset from 
UTC. i.e it will be negative for a countr's east of the Greenwich Meridian

tzedname returns a tuple containing two strings; the name of the dst timezone 
and the name of the DST time zone.

Note: Before relying on the DST timezone name, we need to check the value of 
time.daylight if it is non-zero then a DST timezone is defined.
"""

import time


print("The epoch on this system starts at " + time.strftime("%c", time.gmtime(0)))
# %c makes sure your typing in lower case because it makes a difference.

print("The current time timezone is {0} with an offset of {1}"
.format(time.tzname[0], time.timezone))
# current time zone

if time.daylight != 0:
    print("\tDaylight Saving Time is in effect for this location")
    print("\tThe DST timezone is " + time.tzname[1])
    print("Yayyy!!! you're in Australia")

print("local time is " + time.strftime("%Y-%m-%d %H: %M: %S", time.localtime()))
print("local time is " + time.strftime("%Y-%m-%d %H: %M: %S", time.gmtime()))

