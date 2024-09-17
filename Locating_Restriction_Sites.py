from Bio import SeqIO
from Bio.Seq import Seq

def reverse_complement(dna_seq):
    # Returns the reverse complement of a DNA sequence
    return str(Seq(dna_seq).reverse_complement())

def find_reverse_palindromes(dna_string):
    # Finds all reverse palindromes of length between 4 and 12 in the DNA string
    min_length = 4
    max_length = 12
    palindromes = []

    for length in range(min_length, max_length + 1):
        for start in range(len(dna_string) - length + 1):
            substring = dna_string[start:start + length]
            if substring == reverse_complement(substring):
                palindromes.append((start + 1, length))  # 1-based index

    return palindromes


fasta_file = "rosalind_revp.txt"
# Reads the FASTA file and finds reverse palindromes in the DNA sequence
for record in SeqIO.parse(fasta_file, "fasta"):
    dna_string = str(record.seq)
    palindromes = find_reverse_palindromes(dna_string)
        
    # Print the results
    for position, length in palindromes:
        print(f"{position} {length}")




