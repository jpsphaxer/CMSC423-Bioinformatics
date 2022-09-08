""" Implement GreedyMotifSearch with Pseudocounts """

def read_data_from(filename):
    with open(filename) as f:
        data = f.readlines()

    for i in range(0, len(data)):
        data[i] = data[i].strip()

    return data

profileRow = {'A': 0, 'C':1, 'G':2, 'T':3}
def make_profile(kmers):
    """ return list of dictionaries where each dictionary is column of the profile """

    if len(kmers) == 0:
        #print "None!!!"
        return None

    k = len(kmers[0])
    t = len(kmers)
    profile = list(dict())
    for i in range(k):
        profile_column = {'A':1, 'C':1, 'G':1, 'T':1}
        for j in range(t):
            #print(profile_column)
            profile_column[kmers[j][i]] += 1

        for key in profile_column.keys():
            profile_column[key] = 1.0 * profile_column[key] / t

        profile.append(profile_column)

    return profile

def pattern_probability(profile, pattern):
    probability = 1
    for i in range(0, len(pattern)):
        probability *= profile[i][pattern[i]]

    return probability

def profile_most_probable_kmer(dna, profile, k):
    start = 0
    length = len(dna)
    max_probability = 0
    most_probable = dna[0:k]
    while start + k <= length:
        substr = dna[start:start+k]
        probability = pattern_probability(profile, substr)
        if probability > max_probability:
            most_probable = substr
            max_probability = probability

        start += 1
    print("most probable " + most_probable)
    return most_probable

def hamming_dist(str_one, str_two):
    """ returns number of hamming_dist between two strings """

    len_one = len(str_one)
    len_two = len(str_two)
    if len_one != len_two:
        raise ValueError("Strings have different lengths.")

    mismatches = 0
    for i in range(len_one):
        if str_one[i] != str_two[i]:
            mismatches += 1

    return mismatches

def make_consensus(motifes):
    profile = make_profile(motifes)
    consensus_list = list()
    for item in profile:
        consensus_list.append(max(item, key=item.get))

    return ''.join(consensus_list)

def score(motifes):
    consensus = make_consensus(motifes)
    print(consensus)
    score = 0
    for motif in motifes:
        score += hamming_dist(consensus, motif)

    return score

def greedy_motif_search(Dna, k, t):
    if len(Dna) == 0:
        #print "None!!!"
        return None

    best_motif = list()
    for i in range(t):
        best_motif.append(Dna[i][0:k])

    start = 0
    length = len(Dna[0])
    while start + k <= length:
        motifes = list()
        motifes.append(Dna[0][start:start+k])
        for i in range(1, t):
            profile = make_profile(motifes[0:i])
            #print(profile)
            motifes.append(profile_most_probable_kmer(Dna[i], profile, k))
            print(i)
            print(motifes)
            print(f"{score(motifes)}  {score(best_motif)}")
        if score(motifes) < score(best_motif):
            
            best_motif = motifes[:]

        start += 1

    #for element in best_motif:
        #print (element)
    print(best_motif)
    return best_motif


Dna = read_data_from("in")
greedy_motif_search(Dna, 3, 5)