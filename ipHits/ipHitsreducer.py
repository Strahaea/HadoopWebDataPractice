#!/usr/bin/python
#reducer for to find the number of hits to the page
import sys
hits = 0
oldIP = None

from_mapper = "10.223.157.186	1"
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
    # Something has gone wrong. Skip this line.
	continue

    thisIP, thisIPhits = data_mapped

    if oldIP and oldIP != thisIP: #means we've switched to a new page
	print oldIP, "\t", hits
	oldIP = thisIP
	hits = 0

    oldIP = thisIP
    hits += 1

if oldIP != None:
    print oldIP, "\t", hits #to print out last page
	
