N = 96317
x = 0.406113
s = 'TCCCCCTC'
AT = 0
GC = 0

for nt in s:
    if nt == 'A' or nt == 'T':
        AT += 1
    elif nt == 'G' or nt == 'C':
        GC += 1

s_prob = (((1 - x) / 2)**AT) * (((x) / 2)**GC)
prob = 1 - (1 - s_prob)**N
print('%0.3f' % prob)