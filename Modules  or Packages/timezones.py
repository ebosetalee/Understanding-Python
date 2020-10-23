"""
With datetime module and time module, we can get information
on time zone and current time zone using time.timezone and time.tzedname

These aren't functions timezone returns a number of seconds offset from 
UTC. i.e it will be negative for a countr's east of the Greenwich Meridian

tzedname returns a tuple containing two strings; the name of the dst timezone 
and the name of the DST time zone now before relying on the DST timezone name.
"""