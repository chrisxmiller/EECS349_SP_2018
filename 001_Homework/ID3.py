from node import Node
import numpy as np

def ID3(examples, default):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''
  if len(examples) == 0:
    return node(default)
  elif sameClass(examples):
    return node(mode(examples))
  else:
    best = bestAttribute(examples)
    #Find different values in for attribute best
    values = list(set(list([example[best] for example in examples])))
    t = node() with root best
    for value in values:
      #split examples for the different values of best
      newExamples = splitExamples = [example for example in examples if example[attribute] == value]
      subtree = ID3(newExamples,mode(newExamples))
      t = add branch subtree with label value to t
  return t

#Returns the mode classification from the examples
def mode(examples):
  #Get list of all classification for the examples
  values = list([example['Class'] for example in examples])
  #Get the list of possible classification
  labels = list(set(values))
  #Find number of instances of each label
  counts = [0]*len(labels)
  for label in labels:
    for val in values:
      if label == val:
        counts[labels.index(label)] +=1
  #Returns mode of the classification
  return labels[counts.index(max(counts))]

#Tests if the classifications of the examples are homogeneous
def sameClass(examples):
  testClass = examples[0]['Class']
  for example in examples:
    if example['Class'] != testClass:
      return False
  return True

#Decides which attribute is the best to split on by comparing entropy gain
def findBestAttribute(examples):
  attributes = examples[0].keys()
  attributes.remove('Class')
  bestAttribute = "None"
  bestGain = 0
  #Loop through all attributes and check the entropy gained from the split
  #New entropy will be a weighted average on the entropy
  for attribute in attributes:
    totalEntropy = entropy(examples,attribute)
    values = list(set(list([example[attribute] for example in examples])))
    counts = len(values)*[0]
    newEnts = len(values)*[0]
    for value in values:
      #splits the examples for the different values of attribute
      #I am most proud of this line
      splitExamples = [example for example in examples if example[attribute] == value]
      counts[values.index(value)] = float(len(splitExamples))
      newEnts[values.index(value)] = entropy(splitExamples,attribute)
    total = sum(counts)
    #Calculated weight average new entropy value
    newEnt = 0
    for i in range(0,len(counts)):
      newEnt += counts[i]*newEnts[i]/total
    entGained = totalEntropy-newEnt
    if entGained > bestGain:
      bestAttribute = attribute
      bestGain = entGained 
  return bestAttribute

def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''

def entropy(ds, att):
  '''
  Calculates the entropy for an array of examples, ds, in dictionary form with the
  defining attribute, att. att is a string. 

  Values unknown, denoted at "?" are tallied and the entropy calculation 
  removes data points with "?" from the set (e.g. total = 5, two ?'s causes total = 3)

  '''
  #List of all possible characteristics
  labels = list(set(list([example['Class'] for example in ds])))
  #Counts of each type of characteristic
  num = len(labels)
  counts = [0]*num
  #Count number of known attributes, and number of each characteristic
  total = 0;
  for ex in ds:
    if ex[att] != '?':
      total += 1
      for label in labels:
        if ex['Class'] == label:
        counts[labels.index(label)] +=1

 
  #Calculate entropy and returns
  ent = 0
  for i in range(0,num):
    p = float(counts[1])/float(total)
    ent += - p*math.log(p,num)
  return ent

def infoGain(ds):
  '''
  Takes in an array of values, and calculates the information gain for each possible split 
  returns the highest valued first. 
  ''' 

def dicParse(data):
  '''
  Reads in an array of dictionary values and does shit to them. Working on this...
  '''
