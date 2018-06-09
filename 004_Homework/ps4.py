'''
Christopher Miller
EECS349 - Spring 2018
Northwestern University
Homework 4 - Part II - Code
Cosine similarity function
''' 

import math
import numpy as np
import json

#Q5 --- COSINE SIMILARITY 

def cosine_similarity(vec1, vec2):
	#Compute dot product of both vectors
	dotprod = np.dot(vec1,vec2)
	#Compute the norm of each vector
	v1norm = np.linalg.norm(vec1)
	v2norm = np.linalg.norm(vec2)
	#compute the cosine similarity and return
	return dotprod / (v1norm*v2norm)

#Q6 --- VGGNET RESULTS
#Test the function with othogonal arrays
# vec1 = np.array([1,0,0])
# vec2 = np.array([0,1,0])
# output = cosine_similarity(vec1, vec2)
# print output

#import the *.json file and compute the cosine similarity for both VGG and RGB representations
with open('cnn_dataset.json') as cnn_dataset:
	data = json.load(cnn_dataset)
	#RGB similarities 
	pxmj1mj2 = cosine_similarity(data['pixel_rep']['mj1'], data['pixel_rep']['mj2'])
	pxmj1cat = cosine_similarity(data['pixel_rep']['mj1'], data['pixel_rep']['cat'])
	pxmj2cat = cosine_similarity(data['pixel_rep']['cat'], data['pixel_rep']['mj2'])
	#VGG similarities 
	vggmj1mj2 = cosine_similarity(data['vgg_rep']['mj1'], data['vgg_rep']['mj2'])
	vggmj1cat = cosine_similarity(data['vgg_rep']['mj1'], data['vgg_rep']['cat'])
	vggmj2cat = cosine_similarity(data['vgg_rep']['cat'], data['vgg_rep']['mj2'])


print 'pxreps'
print pxmj1mj2
print pxmj1cat
print pxmj2cat

print 'VGGreps'
print vggmj1mj2
print vggmj1cat
print vggmj2cat

#Q8 --- CAPTIONS

#Read in JSON 
with open('dataset.json') as dataset:
	data = json.load(dataset)
	#Test
	test = data['test']
	#Train
	train = data['train']
	#images
	images = data['images']
	#Captions
	captions = data['captions']

#Read in VGG
vggmat = np.load('vgg_rep.npy')

#VGG
vgg_cs = []
vgg_results = []

for im in test:
	idx = images.index(im)
	test_vec = vggmat[idx]	
	#pull vector in matrix for image
	for imt in train:
		#pull vector in matrix for training set
		idx_train = images.index(imt)
		train_vec = vggmat[idx_train]
		#Calculate cosine similarity for this image
		cossim = cosine_similarity(test_vec,train_vec)
		#Store the CSsim
		vgg_cs.append(cossim)
	#find max CSsim 
	max_cssim = max(vgg_cs)
	#index of max cos sim, also index in training set of most similar image
	idx_max = vgg_cs.index(max_cssim)
	#Extract image name
 	most_sim_im = train[idx_max]
  	#Extract the caption
 	sim_cap = captions[most_sim_im]
  	#append the caption to an array where in
	vgg_results.append(sim_cap)
  	#Clear the arrays 
	vgg_cs = []
#Write a dictionary
vgg_dict = dict(zip(test,vgg_results))
#Save file 
f = open("vggres.txt","w")
for out in vgg_dict:
	f.write(str(out))
	f.write(":")
	f.write(vgg_dict[out])
	f.write("\n")
f.close()


#Pixel
#Repeat process as above, but referencing the new database
#Read in pixel
pixmat = np.load('pixel_rep.npy')

#Pixel
pix_cs = []
pix_results = []

for im in test:
	idx = images.index(im)
	test_vec = pixmat[idx]	
	#pull vector in matrix for image
	for imt in train:
		#pull vector in matrix for training set
		idx_train = images.index(imt)
		train_vec = pixmat[idx_train]
		#Calculate cosine similarity for this image
		cossim = cosine_similarity(test_vec,train_vec)
		#Store the CSsim
		pix_cs.append(cossim)
	#find max CSsim 
	max_cssim = max(pix_cs)
	#index of max cos sim, also index in training set of most similar image
	idx_max = pix_cs.index(max_cssim)
	#Extract image name
 	most_sim_im = train[idx_max]
  	#Extract the caption
 	sim_cap = captions[most_sim_im]
  	#append the caption to an array where in
	pix_results.append(sim_cap)
  	#Clear the arrays 
	pix_cs = []

pix_dict = dict(zip(test,pix_results))
p = open("pixres.txt","w")
for out in pix_dict:
	p.write(str(out))
	p.write(":")
	p.write(pix_dict[out])
	p.write("\n")
p.close()
