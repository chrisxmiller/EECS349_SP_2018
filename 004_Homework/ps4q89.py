'''
Christopher Miller
EECS349 - Spring 2018
Northwestern University
Homework 4 - Part II - Q8/9 Runner
Cosine similarity function
''' 

import math
import numpy as np
import ps4
import json

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

# idx = images.index(test[1])

# capext = captions[test[idx]]

#print capext
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
		cossim = ps4.cosine_similarity(test_vec,train_vec)
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
		cossim = ps4.cosine_similarity(test_vec,train_vec)
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
