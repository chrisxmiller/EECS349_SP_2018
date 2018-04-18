import math
from parse import parse
import ID3
import sys
from node import Node
import random
import copy



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
	if isinstance(tree,str):
		return paths
	if isEnd(tree):
		return [path]
	for child in tree.children:
		if isinstance(child,Node):
			newPath = path
			newPath = newPath + [tree.children.index(child)]
			paths.extend(findEnd(child,newPath))
	return paths


#paths = findEnd(tree)
#print tree.children[0].children[1].children[0].children
#print tree.children[1].children[1].children[1].children[1].children[0].children[0].children

def prunePath(tree,path,n=0):
	newTree = tree
	if n < len(path):
		branch = tree.children[path[n]]
		newTree.children[path[n]] = prunePath(branch,path,n+1)
	else:
		df = tree.default
		ind = tree.parentchar.index(df)
		mode = tree.children[ind]
		return mode
	return newTree


def _prune(tree,ex):
	bestTree = copy.deepcopy(tree)
	bestAcc = ID3.test(tree,ex)
	paths = findEnd(tree)
	change = False
	for path in paths:
		newTree = prunePath(copy.deepcopy(tree),path)
		newAcc = ID3.test(newTree,ex)
		if (newAcc - bestAcc) > 0.001:
			bestAcc = newAcc
			bestTree = copy.deepcopy(newTree)
			change = True
	if change:
		bestTree = _prune(bestTree,ex)
	return bestTree

def charts(data):
	sizes = [10,50,100,150,200,250,300]
	results = len(sizes)*[None]
	accuracies = len(sizes)*[None]
	accuraciesP = len(sizes)*[None]
	for sampleSize in sizes:
		acc = 0.0
		accP = 0.0
		for tests in range(0,100):
			randIndices = random.sample(range(len(data)),sampleSize)
			trainVal = [data[i] for i in randIndices]
			testing = [data[i] for i in range(len(data)) if i not in randIndices]
			pTrain = .90
			randIndices = random.sample(range(len(trainVal)),int(pTrain*len(trainVal)))
			train = [trainVal[i] for i in randIndices]
			val = [trainVal[i] for i in range(len(trainVal)) if i not in randIndices]
			tree = ID3.ID3(train)
			treePrune = _prune(tree,val)
			acc += ID3.test(tree,testing)
			accP += ID3.test(treePrune,testing)
		accuracies[sizes.index(sampleSize)] = acc / 100.0
		accuraciesP[sizes.index(sampleSize)] = accP / 100.0
	results = [sizes,accuracies,accuraciesP]
	return results

print charts(trainingData)

#print ID3.evaluate(tree,trainingData[169])
sampleSize = 10
randIndices = random.sample(range(len(trainingData)),sampleSize)
trainVal = [trainingData[i] for i in randIndices]
testing = [trainingData[i] for i in range(len(trainingData)) if i not in randIndices]
pTrain = .90
randIndices = random.sample(range(len(trainVal)),int(pTrain*len(trainVal)))
train = [trainVal[i] for i in randIndices]
val = [trainVal[i] for i in range(len(trainVal)) if i not in randIndices]

#print len(testing)
#print len(training)
#print ID3.test(ID3.ID3(training,0),testing)

tree = ID3.ID3(train,'y')
newTree = _prune(tree,val)

print ID3.test(tree,testing)
print ID3.test(newTree,testing)