import math
from parse import parse
import ID3
import sys
from node import Node
import random



#Christopher Miller
#Northwestern Univ 
#Winter 2018
#EECS 349

#Parse the voting training data
trainingData = parse('house_votes_84.data')

#Read in the data
data2 = [dict(a=1, b=1, Class='a'),
		dict(a=1, b=1, Class='b'),
	    dict(a=1, b=0, Class='b'),	
	    dict(a=1, b=0, Class='b'),
    	dict(a=1, b=0, Class='b'),
    	dict(a=0, b=1, Class='b'), 
		dict(a=0, b=1, Class='a'),
	    dict(a=0, b=1, Class='a'), 	
	    dict(a=0, b=0, Class='a'),
    	dict(a=0, b=0, Class='a')]


data4 =  [dict(a=1, b=0,   c='?', Class='a'), 
		 dict(a=1, b=3,   c=2,   Class=1),
		 dict(a=2, b='?', c=1,   Class=2), 
		 dict(a=2, b=1,   c=3,   Class=3),
         dict(a=3, b=0,   c=1,   Class=3), 
         dict(a=3, b=2,   c='?', Class=3)]

data3 = [dict(a=1, b=0, Class=1), dict(a=1, b=1, Class=1)]


data = [dict(a=1, b=0,  c='?', Class=1), 
		dict(a=1, b=3,  c=2,   Class=1),
        dict(a=2, b='?',c=1,   Class=2), 
        dict(a=2, b=1,  c=3,   Class=2),
        dict(a=3, b=0,  c=1,   Class=3), 
        dict(a=3, b=2,  c='?', Class=3)]

tree = ID3.ID3(trainingData,0)

#print tree.children[0]
print trainingData[169]['Class']

print ID3.evaluate(tree,trainingData[169])
percent = .70
randIndices = random.sample(range(len(trainingData)),int(percent*len(trainingData)))
training = [trainingData[i] for i in randIndices]
testing = [trainingData[i] for i in range(len(trainingData)) if i not in randIndices]
print len(testing)
print len(training)

print ID3.test(ID3.ID3(training,0),testing)

