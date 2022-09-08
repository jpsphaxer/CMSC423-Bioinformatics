#https://www.youtube.com/watch?v=mGVWYT-WBn0
# this video helped me in developing the code below
def readInput(): 
    fileObj = open("input","r")
    line1 = fileObj.readline().strip()
    line1 = '-' + line1
    line2 = fileObj.readline().strip()
    line2 = '-' + line2
    fileObj.close()
    return line1, line2

def readBloFile(fileName):
    '''reads the  BLOSUMFILE or INPUT'''
    stuff = [] 
    fileObj = open(fileName, "r") #opens the file in read mode
    for line in fileObj.readlines(): 
        lin = line.split()
        stuff.append(lin)

    fileObj.close()
    return stuff

def make_lookup(blo): 
    """makes a look up table row - column """
    x = 0
    table = {}
    blo[0].insert(0, '-')
    
    for i in range(1,len(blo[1])):       
        for j in range(1,len(blo)): 
            touple = (blo[i][x],blo[x][j])
            #print(f'keys: {touple} value: {blo[i][j]} ')
            table[touple] = int(blo[i][j])

    return table

def make_score_back_tables(str1,str2):
    #Note not adding the - to the beginning was messing up my table

    score = [[0 for s2 in range(len(str2))] for s1 in range(len(str1))]
    back =  [["" for s2 in range(len(str2))] for s1 in range(len(str1))]
   
    ##initialize 1 row and 1 column with scores and directions
    # for i in range(len(str1)): 
    #    # print(str1[i])
    #     score[i][0] = -SIGMA * i 
    #     back[i][0] = "up"

    #     for j in range(len(str2)):
    #         score[0][j] = -SIGMA * j
    #         back[0][j] = "left"
    
    #matrix_printer(score)
    #matrix_printer(back)
    
    return score,back


def process_tables(str1,str2,table): 
    
    score,back = make_score_back_tables(str1, str2)

    best_score = 0
    # this will run through put the score values based on the blosum table
    # and also create the backtrack matrix 
    for i in range(1, len(str1)): 
        for j in range (1, len(str2)): 
            #check if the key is in the parsed BLOSUM table
            if (str1[i],str2[j]) in table: 
                #use this key to get the scoring from the table
                key = (str1[i],str2[j])
                #if i ==1 and j == 1: 
                    #print(key)
                #3 test cases used for scoring and also the back track
                diag = score[i-1][j-1] + table[key]
                up = score[i -1][j] - SIGMA
                left = score[i][j-1] - SIGMA

                score[i][j] = max(diag,left,up,0)

                score_val = score[i][j]
                #best score is always the last value (bottom right)
                
                if score_val == diag:
                    back[i][j] = "diagonal"
                elif score_val == up:
                    back[i][j] = "up"
                elif score_val == left:
                    back[i][j] = "left"
    #matrix_printer(score)
    #matrix_printer(back)
    #print(best_score)
    #best_score = score[len(str1)-1][len(str2)-1]   
    print(score)
    best,max_loc_row,max_loc_col = retrieve_score_info(score, len(str1), len(str2))



    return best, back, max_loc_row,max_loc_col

def retrieve_score_info(score_table, str1_len,str2_len):
    '''Going through scores table to find index or row and col where the best score is 
    so we can traverse through the backtracking table 
    '''
        
    best_score = -1
    max_loc_row = 0
    max_loc_col = 0

    for i in range(str1_len):
        for j in range(str2_len): 

            if score_table[i][j] > best_score:
                best_score = score_table[i][j]
                max_loc_row,max_loc_col = i, j
    return best_score,max_loc_row,max_loc_col

def alignment(str1,str2,back,row,col): 
    '''traversing thorugh the backwards table
        to get the alignment of the strings
    '''
    new_str1 = ""
    new_str2 = ""

    i = row
    j = col

    while back[i][j] != "" : 
        dir = back[i][j]

        if dir == "diagonal":
            new_str1 = str1[i] + new_str1
            new_str2 = str2[j] + new_str2
            #travel up diagonal
            i -= 1
            j -= 1

        elif dir == "up": 
            new_str1 = str1[i] + new_str1
            new_str2 = '-' + new_str2
            #travel up 
            i -= 1
        elif dir == "left": 
            new_str1 = '-' + new_str1
            new_str2 = str2[j] + new_str2
            #travel left
            j -= 1

    #print(new_str1)
    #print(new_str2) 

    return new_str1,new_str2     

def matrix_printer(matrix):
    '''printing for debuggin'''
    for row in matrix: 
        print(row) 



SIGMA = 5
str1, str2 = readInput()
blo = readBloFile("PAM250.txt")
table = make_lookup(blo)
#print(table)
score,back,row,col = process_tables(str1, str2, table)
alig1,alig2 = alignment(str1, str2, back,row,col)

output = open("output", "w")
output.write(str(score)+'\n')
output.write(alig1+'\n')
output.write(alig2+'\n')
output.close()

# print(str(score))
# print(alig1)
# print(alig2)

#print(table)
