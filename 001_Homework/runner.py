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
data2 = [dict(a=1, b=1, Class='r'),
		dict(a=1, b=1, Class='d'),
	    dict(a=1, b=0, Class='d'),	
	    dict(a=1, b=0, Class='d'),
    	dict(a=1, b=0, Class='d'),
    	dict(a=0, b=1, Class='d'), 
		dict(a=0, b=1, Class='r'),
	    dict(a=0, b=1, Class='r'), 	
	    dict(a=0, b=0, Class='r'),
    	dict(a=0, b=0, Class='r')]


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

tree = ID3.ID3(trainingData,'r')

def count(tree,n):
	if isEnd(tree):
		return 1
	else:
		for child in tree.children:
			if isinstance(child,Node):
				n += count(child,n)
	return n




def isEnd(tree):
	for child in tree.children:
		if isinstance(child,Node):
			return False
	return True

def prime_factors(n):
	for i in range(2,n):
		if n % i == 0:
			return [i] + prime_factors(n/i)
	return [n]


def findEnd(tree,path=[]):
	paths =[]
	if isEnd(tree):
		return [path]
	for child in tree.children:
		if isinstance(child,Node):
			newPath = path
			newPath = newPath + [tree.children.index(child)]
			paths.extend(findEnd(child,newPath))
	return paths


paths = findEnd(tree)
print tree.children[0].children[1].children[0].children
#print tree.children[1].children[1].children[1].children[1].children[0].children[0].children

def followPath(tree,path,n=0):
	newTree = tree
	if n < len(path):
		branch = tree.children[path[n]]
		newTree.children[path[n]] = followPath(branch,path,n+1)
	else:
		df = tree.default
		ind = tree.parentchar.index(df)
		mode = tree.children[ind]
		print mode
		return mode
	return newTree

newTree =  followPath(tree,paths[0])
print newTree.children[0].children[1].children[0].children


#print ID3.evaluate(tree,trainingData[169])
percent = .70
randIndices = random.sample(range(len(trainingData)),int(percent*len(trainingData)))
training = [trainingData[i] for i in randIndices]
testing = [trainingData[i] for i in range(len(trainingData)) if i not in randIndices]
#print len(testing)
#print len(training)

#print ID3.test(ID3.ID3(training,0),testing)

