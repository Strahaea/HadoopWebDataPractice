#!/usr/bin/python
#reducer finding most popular path
import sys
hits = 0
oldPage = None #used to keep track of the last page
mostPage = None #used to keep track of the page with the most hits
mostHits = 0
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
    # Something has gone wrong. Skip this line.
	continue

    thisPage, thisPageHits = data_mapped

    if oldPage and oldPage != thisPage: #means we've switched to a new page
	if hits > mostHits: #checks to see if the last page had the most hits
		mostPage, mostHits = oldPage, hits
	oldPage = thisPage
	hits = 0

    oldPage = thisPage
    hits += 1

if oldPage != None:
    if hits > mostHits:
	mostPage, mostHits = oldPage, hits

print mostPage, "\t", mostHits
	
