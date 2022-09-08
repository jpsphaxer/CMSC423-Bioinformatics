def file_manager():
    d_matrix = []
    file = open("input", "r")
    lines = file.read().splitlines()

    n = int(lines[0])
    lines.pop(0)
    # print(lines)
    # print(n)

    for line in lines:
        values = [float(d) for d in line.split(' ')]
        # print(values)
        d_matrix.append(values)

    #file.close()

    # print(d_matrix)
    return n, d_matrix

#  HierarchicalClustering(D, n)
#  Clusters ← n single-element clusters labeled 1, ... , n
#  construct a graph T with n isolated nodes labeled by single elements 1, ... , n
#  while there is more than one cluster
#   find the two closest clusters Ci and Cj
#   merge Ci and Cj into a new cluster Cnew with |Ci| + |Cj| elements
#   add a new node labeled by cluster Cnew to T
#   connect node Cnew to Ci and Cj by directed edges
#   remove the rows and columns of D corresponding to Ci and Cj
#   remove Ci and Cj from Clusters
#   add a row/column to D for Cnew by computing D(Cnew, C) for each C in Clusters
#   add Cnew to Clusters
#     assign root in T as a node with no incoming edges
#     return T


def HierarchicalClustering(distance_matrix,n):
    # first line making clusters
    clusters = [[i] for i in range((n))]

    new_clusters_list = []

    while len(clusters) != 1:  # while more than 1 cluster

        # Find the two closest clusters
        min_dist = float('inf') # palce holder just like prev proj

        #iterating through the dist array only top half fashion
        for i in range(len(clusters) - 1):
            for j in range(i + 1, len(clusters)):

                #calculations of distances using table rather than avg method
                dist = 0
                for idx1 in clusters[i]:
                    for idx2 in clusters[j]:
                        dist += distance_matrix[idx1][idx2]
                dist /= (len(clusters[i]) * len(clusters[j]))

                #Figuring out the closest distance
                if dist < min_dist:
                    min_dist = dist
                    index1_clus = i
                    index2_clus = j

        # Merge the two closeet clusters
        new_cluster = clusters[index1_clus] + clusters[index2_clus]
        # Removal of nodes Ci and Cj like pseudocode 
        clusters = [clu for clu in clusters if clu not in [
            clusters[index1_clus], clusters[index2_clus]]]
        #adding Cnew to clusters
        clusters.append(new_cluster)
        #returning our actual new list of clusters. 
        new_clusters_list.append(new_cluster)
    return new_clusters_list


n, d_matrix = file_manager()
clus = HierarchicalClustering(d_matrix,n)

#adds 1 to match the output on rosalind
def plusone(item):
    return item+1


# processing the clusters to the right vals with func above
answer = []
for line in clus: 
    output = list(map(plusone,line))
    answer.append(output)

#create string array of the answers to be written to file
ans = []
for line in answer: 
    ans.append(' '.join(str(e) for e in line)+'\n')

#write to file 
out = open("output", "w")
for line in ans: 
    out.write(line)
#out.close()


#print(answer)
#print(ans)
