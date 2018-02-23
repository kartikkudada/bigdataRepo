#!/usr/bin/python

import sys

for line in sys.stdin:
 splits = line.split(',')
 if len(splits) > 20:
  if len(splits[3]) and len(splits[4]):
    if splits[3] == 'H':
	   print '{0},{1}'.format(splits[4],1)
	  