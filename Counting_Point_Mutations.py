from Bio import SeqIO

def hamming_distance(s, t):
    # Ensure the strings have the same length
    if len(s) != len(t):
        raise ValueError("Strings must be of the same length")
    
    # Count the number of positions where the characters differ
    distance = sum(1 for a, b in zip(s, t) if a != b)
    return distance

def get_sequences(fasta_file):
    # Read sequences from the FASTA file
    sequences = [str(record.seq) for record in SeqIO.parse(fasta_file, "fasta")]
    
    # Ensure there are exactly 2 sequences
    if len(sequences) != 2:
        raise ValueError("The FASTA file must contain exactly 2 sequences")
    
    return sequences[0], sequences[1]


fasta_file = "rosalind_hamm.txt"

s, t = get_sequences(fasta_file)
distance = hamming_distance(s, t)

# In kết quả
print(distance)
