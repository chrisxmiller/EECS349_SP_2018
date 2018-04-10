from node import Node
import numpy as np

def ID3(examples, default):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''

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
  #Find the total number of points in the set
  total = len(ds)

  #define and zero variables. 
  numpos = 0.0
  numneg = 0.0
  numunk = 0.0

  #Count number of each republicans and democrats 
  for i in range (0, total):
    if ds[i][att] == att: 
      numpos += 1.0
    elif ds[i][att] == "?"
      numunk += 1.0 
    else:
      numneg += 1.0

  #Remove unknowns from the set
  total = total - numunk;

  #Calculate entropy and returns
  ent = -(numpos/total)*np.log2(numpos/total) - (numneg/total)*np.log2(numneg/total)
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
