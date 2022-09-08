"""Find min skew in DNA sequence"""

#handles new lines in file lines read
def strip_new_line(line_array):
    sequence = ""
    for line in line_array:
        sequence += str(line)
    return sequence

def str_min_skew(skew_array):
    minimum = min(skew[1:])
    output = ""
    for i in range(1, len(skew)):

        if skew[i] == minimum:
            output += str(i) + " "
    return output

file = open("input", "r")
#read lines (pattern) store in list
lines = file.read().splitlines()
sequence = strip_new_line(lines)
length = len(sequence)
#print(sequence)
skew = [0]
#make the min skew array
for i in range(length):
    if sequence[i] == "C":
        skew.append(skew[-1] - 1)
    elif sequence[i] == "G":
        skew.append(skew[-1] + 1)
    else:
        skew.append(skew[-1])

print(skew)

output = str_min_skew(skew)
print(output)

file.close()

o_file = open("output", "w")
o_file.write(output)
o_file.close()