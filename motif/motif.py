#import numpy as np
import math
#read data from file 
file = open("input", "r")

data = file.readlines()
#print(data)
for line in range(0,len(data)): 
    data[line] = data[line].strip()

k,t = [int(i) for i in data[0].split()]
#print(f"{k} {t}")
data.pop(0)
#print(data)

"""Counts the number of ACGT's in a column & creates the profile"""
def count_n_profile(Dna):

    count = list(dict())


    k = len(Dna[0])
    t = len(Dna) 
   # print(k)
    #print(t)

    for i in range(0,k):
        count_col = {'A':1, 'C':1, 'G':1,'T':1}

        for j in range(0,t):

            key = Dna[j][i]
            #print(key)
            count_col[key] += 1


        count_col = profile_col(count_col,t)

        count.append(count_col)
    #print(count)
    return count; 

"""handles each profile column to generate the profile value"""
def profile_col(count,t):
    
    profile_dic = count

    for k in profile_dic.keys(): 
        #print(k)
        profile_dic[k] = profile_dic[k]/(t+4) #PLUS 4 because add 1 to each column 
  
    return profile_dic


"""return the consensus string"""
def consensus(motifs):
    mot_profile = count_n_profile(motifs)
    #print(mot_profile)
    consensus = ""

    for k in mot_profile: 
        neuclotide = max(k, key=k.get) #gets me the A-C-G-T max in the prof col 
        #print(k)
        consensus += neuclotide
    #print(consensus)
    return consensus

def ham_distance(cons,motif): 
    score1 = 0 
    kmer_len = len(cons) 

    for i in range(kmer_len):
        if cons[i] != motif[i]:
            score1 += 1

    return score1

def score(motifs): 
    cons = consensus(motifs)
    #print("The consesus is: " + cons)
    score = 0 

    for motif in motifs: 
        score += ham_distance(cons,motif)


    return score




def most_prob_kmer(Dna,profile,k):
    #print("here")
    length = len(Dna)
    index = 0 
    max_prob = 0 
    most_probable = Dna[0:k]
    #print("most probable bfore loop: " + most_probable)
    while index + k <= length:
        sub = Dna[index:index+k]
        
        #probability = pattern_probability(profile, sub)
        probability = 1

        for i in range(0, len(sub)):
            probability *= profile[i][sub[i]]

        #print(probability)
        if probability > max_prob:
            most_probable = sub
            max_prob = probability
        index += 1
    #print("the most probable " + most_probable)
    return most_probable


# GREEDYMOTIFSEARCH(Dna, k, t)
#     BestMotifs ← motif matrix formed by first k-mers in each string
#                   from Dna
#     for each k-mer Motif in the first string from Dna
#         Motif1 ← Motif
#         for i = 2 to t
#             form Profile from motifs Motif1, …, Motifi - 1
#             Motifi ← Profile-most probable k-mer in the i-th string
#                       in Dna
#         Motifs ← (Motif1, …, Motift)
#         if Score(Motifs) < Score(BestMotifs)
#             BestMotifs ← Motifs
#     return BestMotifs

#greedy motif search in Rosalind pseudo code 
def greedy_motif_search(Dna,k,t):

    bestMotif = list()
    for i in range(t):
        bestMotif.append(Dna[i][0:k])

    index0 = 0 

    while index0 + k <= len(Dna[0]): 
        motifs = list()
        motifs.append(Dna[0][index0: index0 + k])
        #print("motifs before the for loop")
        #print(motifs)
        for i in range(1,t):
      
            profile = count_n_profile(motifs[0:i])
            #print(profile)
            #print("\n"+str(i))
            motifs.append(most_prob_kmer(Dna[i],profile,k))

           # print(motifs)

           # print("Score motif")
            motif_score = score(motifs)

           # print("score best motif")
            bestMotif_score = score(bestMotif)

            #print(f"{motif_score}  {bestMotif_score}")

        if motif_score < bestMotif_score:
                
           # print("inside score compare")
            bestMotif = motifs[:]
           # print(bestMotif)

        index0+=1
    

    return bestMotif



     


answer = greedy_motif_search(data, k, t)
out = open("output","w")
for kmer in answer:
    out.write(kmer+"\n")
out.close()
file.close()
print(answer)