#!/usr/bin/python
#reducer for to find the number of hits to the page
import sys
hits = 0
oldPage = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
    # Something has gone wrong. Skip this line.
	continue

    thisPage, thisPageHits = data_mapped

    if oldPage and oldPage != thisPage: #means we've switched to a new page
	print oldPage, "\t", hits
	oldPage = thisPage
	hits = 0

    oldPage = thisPage
    hits += 1

if oldPage != None:
    print oldPage, "\t", hits #to print out last page
	
