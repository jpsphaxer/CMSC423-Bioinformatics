

from random import randint
import math
import numpy as np

def euclidean_distance(a,b):
    distance = math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2))
    return distance

dataPoints = [[1.3,1.1],[1.3,0.2],[0.6,2.8],[3,3.2],[1.2,0.7],[1.4,1.6],[1.2,1.0],[1.2,1.1],[0.6,1.5],[1.8,2.6],[1.2,1.3],[1.2,1.0],[0.0,1.9]]
#print (dataPoints)

k = 2

centroids = []

def trivial_centers(k,m,data): 
    return [data[i] for i in range(k)]


centroids = trivial_centers(k, 2, dataPoints)
# for i in range(1,k+1):
#     #print (i)
#     uniqueNumber = False
#     while(uniqueNumber==False):
#         a = randint(0, len(dataPoints)-1)
#         print (a)
#         if (dataPoints[a] not in centroids):
#             uniqueNumber = True
#     centroids.append(dataPoints[a])

print(centroids)

while(True):
    clusters = []
    for i in range(k):
        clusters.append([])
    #print(clusters)
    #clusters = [[[6,1],[]],[[1,5],[]]]

    for point in dataPoints:
        #print(point)
        closestCluster = [0,euclidean_distance(point,centroids[0])]
        #print(closestCluster)
        for i in range(1,k):
            #print(i)
            dist = euclidean_distance(point,centroids[i])
            #print(dist)
            if (dist<closestCluster[1]):
                closestCluster=[i,dist]
        clusters[closestCluster[0]].append(point)

    print(clusters)

    newCentroids = []
    for i in range(k):
        print(clusters[i])
        help = np.mean(clusters[i],axis=0)
        print(help)
        newCentroids.append(np.mean(clusters[i],axis=0).tolist())

    print(newCentroids)

    centroidShifted = False

    for i in range(k):
        if (centroids[i] != newCentroids[i]):
            centroidShifted = True
    centroids = newCentroids

    print(centroidShifted)

    if (centroidShifted==False):
        break

