'''
Christopher Miller
EECS349 - Spring 2018
Northwestern University
Homework 4 - Part II - Q5 Runner
Cosine similarity function
''' 

import math
import numpy as np
import ps4
import json

#Test the function with othogonal arrays
vec1 = np.array([1,0,0])
vec2 = np.array([0,1,0])
output = ps4.cosine_similarity(vec1, vec2)
print output

#import the *.json file and compute the cosine similarity for both VGG and RGB representations
with open('cnn_dataset.json') as cnn_dataset:
	data = json.load(cnn_dataset)
	#RGB similarities 
	pxmj1mj2 = ps4.cosine_similarity(data['pixel_rep']['mj1'], data['pixel_rep']['mj2'])
	pxmj1cat = ps4.cosine_similarity(data['pixel_rep']['mj1'], data['pixel_rep']['cat'])
	pxmj2cat = ps4.cosine_similarity(data['pixel_rep']['cat'], data['pixel_rep']['mj2'])
	#VGG similarities 
	vggmj1mj2 = ps4.cosine_similarity(data['vgg_rep']['mj1'], data['vgg_rep']['mj2'])
	vggmj1cat = ps4.cosine_similarity(data['vgg_rep']['mj1'], data['vgg_rep']['cat'])
	vggmj2cat = ps4.cosine_similarity(data['vgg_rep']['cat'], data['vgg_rep']['mj2'])


print 'pxreps'
print pxmj1mj2
print pxmj1cat
print pxmj2cat

print 'VGGreps'
print vggmj1mj2
print vggmj1cat
print vggmj2cat