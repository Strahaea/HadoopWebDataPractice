#!/usr/bin/python
#mapper for to find the number of hits to the page

import re
import sys

p = re.compile('([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)')

for line in sys.stdin:
    m = p.match(line)
    if not m:
	continue
    host, ignore, user, date, request, status, size = m.groups()

    #turn the request into a page
    page = m.group(5)[m.group(5).find('/'):m.group(5).find('HTTP')-1] 
    print "{0}\t{1}".format(page, '1')
