import re
from Bio import SeqIO

import itertools
nt = 'ACGT'        #Use this order of nt to get correct order later without sorting
permutations = itertools.product(nt, repeat=4)

kmers = []
for i, j in enumerate(list(permutations)):
    kmer = ''
    for item in j:
        kmer += str(item)
    kmers.append(kmer)

record = SeqIO.read('rosalind_kmer.txt', 'fasta')
sequence = record.seq

A = []
for k in kmers:
    occurence = 0
    pattern = re.compile(r'(?=(' + k + '))')
    for l in re.findall(pattern, str(sequence)):
        occurence += 1
    A.append(occurence)
print(*A, sep=' ')