from libkmeans import *

data=read_data("abalone.data")
kmeans(calculate_centroids(3,data),data)