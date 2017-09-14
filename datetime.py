# The datetime Library
#A lot of times you want to keep track of when something happened. We can do so in Python using datetime.

#Here we'll use datetime to print the date and time in a nice format.

from datetime import datetime

now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

print datetime.now()
print "%s-%s-%s" % (current_month, current_day, current_year)
print '%s/%s/%s' % (now.month, now.day, now.year)
print '%s:%s:%s' % (now.hour, now.minute, now.second)

# Combined:
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
# yields: 9/12/2017 17:50:52
