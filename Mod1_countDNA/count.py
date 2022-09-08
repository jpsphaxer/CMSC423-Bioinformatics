"""DNA Neuclotide Counter"""

a = 0
c = 0
g = 0
t = 0 

file = open("input", "r")
lines = file.readlines()

for line in lines:
    a += line.count("A")
    c += line.count("C")
    g += line.count("G")
    t += line.count("T")


output = f"{a} {c} {g} {t}"
#print(f"{a} {c} {g} {t}")
#print(output)

file_out = open("output", "w")
file_out.write(output)