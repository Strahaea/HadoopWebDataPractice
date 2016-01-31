#!/usr/bin/python
#mapper for to find the number of ip hits


import re
import sys

p = re.compile('([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)')
for line in sys.stdin:
    m = p.match(line)
    if not m:
	continue
    host, ignore, user, date, request, status, size = m.groups()

    #turn the request into a page
    ip = m.group(1)
    
    print "{0}\t{1}".format(ip, '1')

