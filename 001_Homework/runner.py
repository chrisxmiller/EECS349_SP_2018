import math
from parse import parse
import ID3

#Christopher Miller
#Northwestern Univ 
#Winter 2018
#EECS 349

#Find the most common characteristic of the examples
# def mode(examples):
	# #Get list of all characteristics for the examples
	# values = list([example['Class'] for example in examples])
	# #Get the list of possible characteristics
	# labels = list(set(values))
	# #Find number of instances of each label
	# counts = [0]*len(labels)
	# for label in labels:
	# 	for val in values:
	# 		if label == val:
	# 			counts[labels.index(label)] +=1
	# #Returns mode of the characteristics
	# return labels[counts.index(max(counts))]

# def sameClass(examples):
# 	testClass = examples[0]['Class']
# 	for example in examples:
# 		if example['Class'] != testClass:
# 			return False
# 	return True

# #Decides which attribute is the best to split on by comparing entropy gain
# def findBestAttribute(examples):
# 	attributes = examples[0].keys()
# 	attributes.remove('Class')
# 	bestAttribute = "None"
# 	bestGain = 0
# 	#Loop through all attributes and check the entropy gained from the split
# 	#New entropy will be a weighted average on the entropy
# 	for attribute in attributes:
# 		totalEntropy = entropy(examples,attribute)
# 		values = list(set(list([example[attribute] for example in examples])))
# 		counts = len(values)*[0]
# 		newEnts = len(values)*[0]
# 		for value in values:
# 			splitExamples = [example for example in examples if example[attribute] == value]
# 			counts[values.index(value)] = float(len(splitExamples))
# 			newEnts[values.index(value)] = entropy(splitExamples,attribute)
# 		total = sum(counts)
# 		#Calculated weight average new entropy value
# 		newEnt = 0
# 		for i in range(0,len(counts)):
# 			newEnt += counts[i]*newEnts[i]/total
# 		entGained = totalEntropy-newEnt
# 		if entGained > bestGain:
# 			bestAttribute = attribute
# 			bestGain = entGained 
# 	print bestGain
# 	print bestAttribute

# def entropy(ds, att):
#   '''
#   Calculates the entropy for an array of examples, ds, in dictionary form with the
#   defining attribute, att. att is a string. 

#   Values unknown, denoted at "?" are tallied and the entropy calculation 
#   removes data points with "?" from the set (e.g. total = 5, two ?'s causes total = 3)

#   '''
#   #List of all possible characteristics
#   labels = list(set(list([example['Class'] for example in ds])))
#   #Counts of each type of characteristic
#   num = len(labels)
#   counts = [0]*num
#   #Count number of known attributes, and number of each characteristic
#   total = 0;

#   for ex in ds:
#   	if ex[att] != '?':
#   		total += 1
#   		for label in labels:
#   			if ex['Class'] == label:
# 				counts[labels.index(label)] +=1

#   #Calculate entropy and returns
#   ent = 0
#   for i in range(0,num):
#   	if total == 0:
#   		ent = 1
#   	else:
#   		p = float(counts[i])/float(total)
#   		ent += - p*math.log(p,num)
#   return ent

  
#Read in the data
data2 = [dict(a=1, b=1, Class=1),
		dict(a=1, b=1, Class=1),
	    dict(a=1, b=0, Class=1),	
	    dict(a=1, b=0, Class=1),
    	dict(a=1, b=0, Class=1),
    	dict(a=0, b=1, Class=1), 
		dict(a=0, b=1, Class=1),
	    dict(a=0, b=1, Class=0), 	
	    dict(a=0, b=0, Class=0),
    	dict(a=0, b=0, Class=0)]


data =  [dict(a=1, b=0,   c='?', Class='a'), 
		 dict(a=1, b=3,   c=2,   Class=1),
		 dict(a=2, b='?', c=1,   Class=2), 
		 dict(a=2, b=1,   c=3,   Class=3),
         dict(a=3, b=0,   c=1,   Class=3), 
         dict(a=3, b=2,   c='?', Class=3)]





#Parse the voting training data
trainingData = parse('house_votes_84.data')

a = ID3.ID3(data2,1)

print a.default