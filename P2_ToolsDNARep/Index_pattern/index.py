
"""Output index where DNA pattern is found in a sequence"""

#handles new lines in file lines read
def strip_new_line(line_array):
    sequence = ""
    for line in line_array:
        sequence += str(line)
    return sequence

file = open("input", "r")
pattern = file.readline().strip()
pat_len = len(pattern)

#read lines after 1st line (pattern) store in list
lines = file.read().splitlines()
sequence = strip_new_line(lines)



#print(pattern)
#print(sequence)

index = ""
loop_len = len(sequence) - pat_len + 1

for i in range(loop_len):
    if sequence[i:i+pat_len] == pattern:
        index += str(i) + " "

print(index)
file.close()

#writing to output file

output = open("output","w")
output.write(index)
output.close()