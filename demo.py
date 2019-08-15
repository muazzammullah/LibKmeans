from libkmeans import *

data=read_data("whateverdatafile.data")
k=3
kmeans(calculate_centroids(k,data),data)
