import math
from parse import parse
import ID3
import sys
from node import Node
import random
import copy
import numpy as np

import matplotlib.pyplot as plt



#Christopher Miller
#Northwestern Univ 
#Winter 2018
#EECS 349

#Parse the voting training data
trainingData = parse('house_votes_84.data')
data = parse('house_votes_84.data')
#populate sizes
#sizes = range(8,270,10)
sizes = [10,40]
withPruning = []
withoutPruning = []

withPruningV = []
withoutPruningV = []

#---- Means ----
withPruningMean =[]
withoutPruningMean = []

withPruningVMean = []
withoutPruningVMean = []


def chart(data):
	sizes = [10,12,14,16,19,24,30,40,50,65,80,100,120,150,180,210,240,265,300]
	#sizes = [50,65,80,100,120,150,180,210,240,265,300]
	results = len(sizes)*[None]
	accuracies = len(sizes)*[None]
	accuraciesP = len(sizes)*[None]
	for sampleSize in sizes:
		acc = 0.0
		accP = 0.0
		num = 100.0
		count = 0.0
		for tests in range(0,int(num)):
			randIndices = random.sample(range(len(data)),sampleSize)
			trainVal = [data[i] for i in randIndices]
			testing = [data[i] for i in range(len(data)) if i not in randIndices]
			pTrain = .90
			randIndices = random.sample(range(len(trainVal)),int(pTrain*len(trainVal)))
			train = [trainVal[i] for i in randIndices]
			val = [trainVal[i] for i in range(len(trainVal)) if i not in randIndices]
			tree = ID3.ID3(train,'y')
			acc += ID3.test(tree,testing)
			try:
				newTree = ID3.prune(tree,val)
				accP += ID3.test(tree,testing)
			except RuntimeError:
				count += 1.0
		accuracies[sizes.index(sampleSize)] = acc / num
		accuraciesP[sizes.index(sampleSize)] = accP / (num-count)
	results = [sizes,accuracies,accuraciesP]
	return results

sampleSize = 5
randIndices = random.sample(range(len(trainingData)),sampleSize)
trainVal = [trainingData[i] for i in randIndices]
testing = [trainingData[i] for i in range(len(trainingData)) if i not in randIndices]
pTrain = .90
randIndices = random.sample(range(len(trainVal)),int(pTrain*len(trainVal)))
train = [trainVal[i] for i in randIndices]
val = [trainVal[i] for i in range(len(trainVal)) if i not in randIndices]

tree = ID3.ID3(train,'y')
print ID3.test(tree,testing)
ID3.prune(tree,val)
print ID3.test(tree,testing)


results = chart(data)
plt.figure(1)
plt.plot(results[0], results[1], 'r', results[0], results[2], 'b')
plt.xlabel('Number of Training Points')
plt.ylabel('Accuracy')
plt.title('Mean Accuracy (100 runs) vs. Number of Training Points on Test Data')
plt.show()

# for size in sizes:
# 	for i in range(100):
# 		random.shuffle(data)
# 		train = data[:size]
# 		valid = data[300:370]
# 		test = data[370:]
# 		tree = ID3.ID3(train, 'democrat')
# 		acc = ID3.test(tree, valid)
#     	withoutPruningV.append(acc)
#     	acc = ID3.test(tree, test)
#     	withoutPruning.append(acc)
  
#     	ID3.prune(tree, valid)
#     	acc = ID3.test(tree, valid)
#     	withPruningV.append(acc)
#     	acc = ID3.test(tree, test)
#     	withPruning.append(acc)

# 	withPruningMean.append(np.mean(withPruning))
# 	withoutPruningMean.append(np.mean(withoutPruning))

# 	withPruningVMean.append(np.mean(withPruningV))
# 	withoutPruningVMean.append(np.mean(withoutPruningV))
# 	print withPruning
# 	withPruning = []
# 	withoutPruning = []
# 	withPruningV = []
# 	withoutPruningV = []


# plt.figure(2)
# plt.plot(sizes, withoutPruningVMean, 'r', sizes, withPruningVMean, 'b')
# plt.xlabel('Number of Training Points')
# plt.ylabel('Accuracy')
# plt.title('Mean Accuracy (100 runs) vs. Number of Training Points on Validation Data')
# plt.show()



