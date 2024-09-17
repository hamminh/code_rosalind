import re
from Bio import SeqIO
from Bio.Seq import Seq

# Read the sequence from the FASTA file
record = SeqIO.read('test.fasta', 'fasta')

# Define the pattern to find
pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')

# Get the forward and reverse complement sequences
frw_seq = record.seq
rev_seq = frw_seq.reverse_complement()

# List to store unique protein sequences
sequences = []

# Find and translate sequences in the forward strand
for m in re.findall(pattern, str(frw_seq)):
    dna_seq = Seq(m)  # No need to specify generic_dna
    prot_seq = dna_seq.translate()
    if prot_seq not in sequences:
        sequences.append(prot_seq)

# Find and translate sequences in the reverse strand
for n in re.findall(pattern, str(rev_seq)):
    rev_dna_seq = Seq(n)  # No need to specify generic_dna
    rev_prot_seq = rev_dna_seq.translate()
    if rev_prot_seq not in sequences:
        sequences.append(rev_prot_seq)

# Print all unique protein sequences
for i, s in enumerate(sequences):
    print(s)
