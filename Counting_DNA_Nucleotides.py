a = 0
t = 0
c = 0
g = 0
dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

for n in dna:
    if n == 'A' :
        a += 1
    elif n == 'T':
        t += 1
    elif n == 'C':
        c += 1
    elif n == 'G':
        g += 1
    
print(str(a) + ' ' + str(c) + ' ' + str(g) + ' ' + str(t))