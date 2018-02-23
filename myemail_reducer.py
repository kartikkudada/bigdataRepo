#!/usr/bin/python

import sys
a_dict={}
counter = 0
for line in sys.stdin:
  email,value = line.split(',')
  email = str(email)
  value = int(value)
  if(counter == 0):
   a_dict[email] = value
   counter = counter + 1
  else:
   list_keys = [key for key in a_dict]
   if (email in list_keys):
    a_dict[email] = a_dict[fromemail] + value
   else:
    a_dict[email] = value

	
desc_order_list=sorted(a_dict,key=a_dict.get,reverse=True)
for i in range(0,3):
 print(desc_order_list[i],a_dict[desc_order_list[i]])
 
 