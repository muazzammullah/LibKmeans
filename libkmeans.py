import os
import sys
import math
from copy import deepcopy
import matplotlib.pyplot as plt
import random

def distance(cpoint,point1):
	return math.sqrt(((cpoint[0]-point1[0])**2)+((cpoint[1]-point1[1])**2))
def average(valueclass,points):
	sumx=0
	sumy=0
	npoints=0
	for datapoint in points:
		if(datapoint[2]==valueclass):
			npoints+=1
			sumx+=datapoint[0]
			sumy+=datapoint[1]
	return [sumx/(npoints),sumy/(npoints)]


def kmeans(centroids,data):
	#append None to every point in data so it can be assigned a color later
	for datapoint in data:
		datapoint.append(None)
	#start plotting all points in yellow.Initial data representation
	for centroid in centroids:
		centroid_x=centroid[0]
		centroid_y=centroid[1]
		centroid_color_plot=centroid[2]+"*"
		centroid_color_name=centroid[2]
		plt.plot(centroid_x,centroid_y,centroid_color_plot)
	centroid_cluster_points_x=[datapoint[0] for datapoint in data if datapoint[2]==None]
	centroid_cluster_points_y=[datapoint[1] for datapoint in data if datapoint[2]==None]
	#plotting points
	plt.plot(centroid_cluster_points_x,centroid_cluster_points_y,"yo")
	#assign title to plot
	plt.title(1)
	#save figure as image in png format
	plt.savefig('iter_1.png')
	#initialize counter to increase and show on top of plot
	counter=1
	#loop until convergence
	while(True):
		#increment counter for current plot
		counter+=1
		#initialize figure for plot
		fig=plt.figure()
		#deep copy centroid array
		centroid_copy=deepcopy(centroids)
		#assign colors based on euclidean distance
		for i in range(0,len(data)):
			datapoint_to_centroid=[]
			for x in range(0,len(centroids)):
				datapoint_to_centroid.append(distance(centroids[x],data[i]))
			centroid_index=datapoint_to_centroid.index(min(datapoint_to_centroid))
			data[i][2]=centroids[centroid_index][2]
		#reposition centroids on plot
		for j in range(0,len(centroids)):
			centroid_color=centroids[j][2]
			points_average=average(centroid_color,data)
			centroids[j][0]=points_average[0]
			centroids[j][1]=points_average[1]
		#plot all points in all clusters
		for centroid in centroids:
			centroid_x=centroid[0]
			centroid_y=centroid[1]
			centroid_color_plot=centroid[2]+"*"
			centroid_color_name=centroid[2]
			plt.plot(centroid_x,centroid_y,centroid_color_plot)
			centroid_cluster_points_x=[datapoint[0] for datapoint in data if datapoint[2]==centroid_color_name]
			centroid_cluster_points_y=[datapoint[1] for datapoint in data if datapoint[2]==centroid_color_name]
			plt.plot(centroid_cluster_points_x,centroid_cluster_points_y,centroid_color_name+"o",markeredgecolor='black')
		#assign title to figure with iteration number
		plt.title(""+str(counter))
		#save figure
		fig.savefig('iter_'+str(counter)+'.png')
		#k-means convergence case,break out of loop
		if(centroids==centroid_copy):
			break
	return data
	
#read data from file
def read_data(filename):
	data=[]
	data_file=open(filename,"r")
	for line in data_file:
		length=float(line.split(",")[0])
		width=float(line.split(",")[1].replace("\n",""))
		item=[length,width]
		data.append(item)
	#return data as array
	return data
	
#run(centroids,data)////////////////////////////////////////////////////////////////

def calculate_centroids(k,data):
	#centroids empty list
	centroids=[]
	#color lists
	colors=["b","g","r","c","m","k","y"]
	for i in range(0,k):
		#initialize empty centroid
		centroid=[]
		#set centroid pos as random data point
		random_color_index=random.randint(0,len(colors)-1)
		#select random color for centroid 
		random_data_point=random.randint(0,len(data)-1)
		#append x value
		centroid.append(data[random_data_point][0])
		#append y value
		centroid.append(data[random_data_point][1])
		#append color value
		centroid.append(colors[random_color_index])
		#delete color from color arr to make sure visualisation has no repeat colors
		del colors[random_color_index]
		#append current filled centroid to centroids array
		centroids.append(centroid)
	return centroids
