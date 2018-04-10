from node import Node
import math
#import ID3
import parse

#Christopher Miller
#Northwestern Univ 
#Winter 2018
#EECS 349


#Read in the data
data = [dict(a=1, b=0, Class=2), 
		dict(a=1, b=1, Class=1),
	    dict(a=2, b=0, Class=2), 	
	    dict(a=2, b=1, Class=3),
    	dict(a=3, b=0, Class=1),
    	dict(a=3, b=1, Class=3)]

tel = {'jack': 4098, 'sape': 4139}

a = dict(one=1, two=2, three=3)


#ent = ID3.entropy(data)
print data[1].keys()