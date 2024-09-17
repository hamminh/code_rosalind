from Bio import SeqIO
from collections import Counter

# Build Profile Matrix
def build_profile_matrix(dna_strings):
    num_strings = len(dna_strings)
    if num_strings == 0:
        return [], ""

    length = len(dna_strings[0])
    profile = {'A': [0] * length, 'C': [0] * length, 'G': [0] * length, 'T': [0] * length}

    for string in dna_strings:
        for i, nucleotide in enumerate(string):
            profile[nucleotide][i] += 1

    return profile

# Build Consensus String
def build_consensus_string(profile):
    length = len(profile['A'])
    consensus = []
    
    for i in range(length):
        column = {nucleotide: profile[nucleotide][i] for nucleotide in 'ACGT'}
        max_count = max(column.values())
        consensus_nucleotides = [nucleotide for nucleotide, count in column.items() if count == max_count]
        consensus.append(consensus_nucleotides[0])  # Pick the first nucleotide in case of a tie

    return "".join(consensus)


# Read file FASTA
fasta_file = "rosalind_cons.txt"
dna_strings = [str(record.seq) for record in SeqIO.parse(fasta_file, "fasta")]
    
profile = build_profile_matrix(dna_strings)
consensus_string = build_consensus_string(profile)

# Output
print(consensus_string)
print("A:", " ".join(map(str, profile['A'])))
print("C:", " ".join(map(str, profile['C'])))
print("G:", " ".join(map(str, profile['G'])))
print("T:", " ".join(map(str, profile['T'])))
