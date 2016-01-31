#!/usr/bin/python
#mapper to find the most popular path

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
    to_filter = "the-associates.co.uk"
    if page.find(to_filter) != -1: #this line is necessary as hinted in project submission as it solves an issue of some of the same paths looking different
	page = page[page.find(to_filter) + len(to_filter):]
    print "{0}\t{1}".format(page, '1')
