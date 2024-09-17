from Bio import SeqIO
record = SeqIO.read('rosalind_kmp.txt', 'fasta')
sequence = list(record.seq)

F_array = [0] * len(sequence)
k = 0
for i in range(2, len(sequence) + 1):
    while k > 0 and sequence[k] != sequence[i - 1]:
        k = F_array[k - 1]
    if sequence[k] == sequence[i - 1]:
        k += 1
    F_array[i - 1] = k


print(' '.join(map(str, F_array)))
