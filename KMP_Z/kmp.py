

#handles new lines in file lines read
def strip_new_line(line_array):
    sequence = ""
    for line in line_array:
        sequence += str(line)
    return sequence


file = open("input", "r")

discard = file.readline()

seq_arr = file.read().splitlines()
sequence = strip_new_line(seq_arr)

sp = [0] * len(sequence)



for i in range (0, len(sequence)-1):
    
    curr = sp[i]

    while curr > 0 and sequence[i+1] != sequence[curr]:
        curr = sp[curr -1]
    
    if sequence[i+1] == sequence[curr]:
        #curr += 1
        sp[i+1] = curr + 1
    else:

        sp[i+1] = 0 

#print(sp)


#out.join(str(sp))
out = " ".join(str(i) for i in sp)

print(out)


output = open("output", "w")
output.write(out)
output.close()
file.close()


