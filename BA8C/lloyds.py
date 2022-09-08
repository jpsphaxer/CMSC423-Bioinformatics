
import math ##for distance formula 

'''This function parses the input file'''
def file_parser():
    m = 0 
    k = 0 
    points = []
    file = open("input", "r")

    for line in file: 
        if k == 0 : 
            values = line.strip().split() 
            k = int(values[0])
            m = int(values[1])
        else: 
            points.append(([float(v) for v in line.strip().split()]))
    file.close()
    return k,m,points


'''

Lloyd_K_means(Data, k)
  Centers[k] =  k randomly selected points from Data
  while Centers change
     # Centers to clusters
     for each point p in Data
       assign p to its nearest center
     # clusters to centers
     for i in 1..k
        Centers[i] = center of mass of points assigned to it
   
   return Centers


'''

def kmean(k,m,data): 
    centers = get_centers(k, m, data)
   # print(centers)
    center_change = True


    while  center_change == True: 
        clusters = []

        for i in range(k):         
            clusters.append([]) ### appending different clusters based on k 
        
        for point in data:

            ##using this cluster to cal the distance for later process
            close_cluster = [0,euclidean_distance(point, centers[0])] 

            for i in range(1,k):

                dist = euclidean_distance(point, centers[i])
                ### calculating distances using the close_cluster dist and dist 
                ### we can figure out into what cluster I can place the point (line 64)
                if dist < close_cluster[1]: 
                    close_cluster = [i,dist]   ##i is the indice for the cluster
            ### assigning p to its nearest point        
            clusters[close_cluster[0]].append(point)

        ## this is the clusters to centers part of the alg
        new_centers = []
        for i in range(k):
            ##using get mean formula I am getting the new centers
            new_centers.append(get_mean(clusters[i]))

        center_change = False
        ## Sanity check for clusters to see if they have changed or not
        for i in range(k): 
            if(centers[i] != new_centers[i]):
                center_change = True
        centers = new_centers


        if(center_change == False): break 
    return centers
  


def get_mean(clusters): 

    #print(clusters)
    column_average = [sum(sub_list) / len(sub_list) for sub_list in zip(*clusters)]
    #print(column_average)

    return column_average


def euclidean_distance(a,b):
    distance = math.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2))
    return distance

def get_centers(k,m,data): 
    return [data[i] for i in range(k)]


def distance(p1,p2,m):
    return sum((p1[i]-p2[i])**2 for i in range (m))

k,m,points = file_parser()
centers = kmean(k, m, points)
print(centers)


strA = []
for p in centers: 
    str = ''
    for val in p : 
        formatted = '{:.3f}'.format(val)
        str += formatted + " "
        #print(str)
    str = str[:len(str)-1]
    strA.append(str)
print(strA)



file = open("output", "w")
file.write('\n'.join(strA))
file.close()

# with open("output", "w") as outfile:
#     outfile.write("\n".join(strA))