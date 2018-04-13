from node import Node
import math
#import ID3
import parse

#Christopher Miller
#Northwestern Univ 
#Winter 2018
#EECS 349


#Read in the data
data2 = [dict(a=1, b=0, Class=2), 
		dict(a=1, b=1, Class=1),
	    dict(a=2, b=0, Class=2), 	
	    dict(a=2, b=1, Class=3),
    	dict(a=3, b=0, Class=1),
    	dict(a=3, b=1, Class=3)]

data =  [dict(a=1, b=0,   c='?', Class=1), 
		 dict(a=1, b=3,   c=2,   Class=1),
		 dict(a=2, b='?', c=1,   Class=2), 
		 dict(a=2, b=1,   c=3,   Class=2),
         dict(a=3, b=0,   c=1,   Class=3), 
         dict(a=3, b=2,   c='?', Class=3)]


#Num keys -1 (last is the class)
num_attributes = len(data[1].keys())-1


#Find index in the loop
classidx = 0
for i in range(0, num_attributes+1):
	if(data[1].keys()[i] == "Class"):
		classidx = i
		break








#ent = ID3.entropy(data)
print classidx