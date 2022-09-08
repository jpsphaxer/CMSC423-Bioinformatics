'''
Inverse Burrows-Wheeler Transform
BWT -> Original String
'''

def input_parse():
    """opens input.txt and removes new lines""" 
    file = open("input", "r")
    text = ""
    lines = file.read().splitlines()

    for line in lines: 
        text += str(line)
    file.close() 

    return text


def convert_bwt(text): 
    """create list with touples containing letter,index"""
    touple_arr = list()

    for i in range(len(text)):
        
        touple = (text[i],i)
        touple_arr.append(touple)

    return touple_arr

def string_retrieve(sorted_bwt): 
    """retrieve the original string from sorted touple array"""
    string = ""


    #separating touple letters into letter touple 
    ## separating indexes in to index touple 
    ### zip is a handy function REMEMBER 
    letter, index = zip(*sorted_bwt)
    #getting the index in the first "line" ($, 1st index) 
    #this helps start the loop so I can jump and get the characters
    #of the original string 
    val = index[0]

    #infinite loop which makes sure that go through the whole array 
    i = 0 

    while i < len(sorted_bwt): 

        # checking if we finally reached the $ we append it to the string and break out 
        # of infinite loop 
        if letter[val] == '$': 
            string += '$'
            break
        
        string += letter[val] #retrieve and append letter at given index to string
        tou = sorted_bwt[val] # we access the touple in the sorted_bwt
        val = tou[1]    # set val to the index we need to jump to next 

    #print(string)
    return string  



        
text = input_parse()
bwt = convert_bwt(text) 
sorted_bwt = sorted(bwt)
string = string_retrieve(sorted_bwt)

out = open("output", "w")
out.write(string)
out.close()