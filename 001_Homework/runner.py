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
data = parse('house_votes_84.data')
#populate sizes
sizes = range(10,300,5)

withPruning = []
withoutPruning = []

withPruningV = []
withoutPruningV = []

#---- Means ----
withPruningMean =[]
withoutPruningMean = []

withPruningVMean = []
withoutPruningVMean = []

for size in sizes:
	for i in range(100):
		random.shuffle(data)
		train = data[:size]
		valid = data[300:335]
		test = data[335:]
		tree = ID3.ID3(train, 'democrat')
		acc = ID3.test(tree, valid)
    	withoutPruningV.append(acc)
    	acc = ID3.test(tree, test)
    	withoutPruning.append(acc)
  
    	ID3.prune(tree, valid)
    	acc = ID3.test(tree, valid)
    	withPruningV.append(acc)
    	acc = ID3.test(tree, test)
    	withPruning.append(acc)

	withPruningMean.append(np.mean(withPruning))
	withoutPruningMean.append(np.mean(withoutPruning))

	withPruningVMean.append(np.mean(withPruningV))
	withoutPruningVMean.append(np.mean(withoutPruningV))

	withPruning = []
	withoutPruning = []
	withPruningV = []
	withoutPruningV = []

plt.figure(1)
plt.plot(sizes, withoutPruningMean, 'r', sizes, withPruningMean, 'b')
plt.xlabel('Number of Training Points')
plt.ylabel('Accuracy')
plt.title('Mean Accuracy (100 runs) vs. Number of Training Points on Test Data')
plt.show()

plt.figure(2)
plt.plot(sizes, withoutPruningVMean, 'r', sizes, withPruningVMean, 'b')
plt.xlabel('Number of Training Points')
plt.ylabel('Accuracy')
plt.title('Mean Accuracy (100 runs) vs. Number of Training Points on Validation Data')
plt.show()



