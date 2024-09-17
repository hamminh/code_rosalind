from Bio import SeqIO
reads = []
with open('rosalind_pdst.txt', 'r') as f:
    for record in SeqIO.parse(f, 'fasta'):
        reads.append(str(record.seq))

read_len = len(reads[0])

for curr_read in reads:
    distance = []
    for comp_read in reads:
        hamming = 0
        for nt1, nt2 in zip(curr_read, comp_read):
            if nt1 != nt2:
                hamming += 1
        distance.append(str.format('{0:.5f}', hamming / read_len))
    print(*distance, sep=' ') 