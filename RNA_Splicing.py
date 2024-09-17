from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import six_frame_translations

# Reads a FASTA file and returns a dictionary of sequences.
def read_fasta(file_path):
    sequences = {}
    for record in SeqIO.parse(file_path, "fasta"):
        sequences[record.id] = str(record.seq)
    return sequences

# Removes introns from the DNA sequence to obtain exons.
def remove_introns(dna_sequence, introns):
    exon_sequence = dna_sequence
    for intron in introns:
        exon_sequence = exon_sequence.replace(intron, "")
    return exon_sequence

# Transcribes the DNA sequence to RNA.
def transcribe_to_rna(dna_sequence):
    return dna_sequence.replace('T', 'U')

# Translates the RNA sequence to a protein sequence.
def translate_rna_to_protein(rna_sequence):
    return str(Seq(rna_sequence).translate())


sequences = []                             
handle = open('rosalind_splc.txt', 'r')     
for record in SeqIO.parse(handle, 'fasta'):
    sequences.append(str(record.seq))      
handle.close()                             
dna_fasta_file = sequences[0]                           
intron_fasta_file = sequences[1]      

# Read DNA sequence and introns from FASTA files
dna_sequences = read_fasta(dna_fasta_file)
intron_sequences = read_fasta(intron_fasta_file)

# Assume the DNA sequence is under the key 'dna'
dna_sequence = list(dna_sequences.values())[0]
    
# Extract introns
introns = list(intron_sequences.values())
    
# Remove introns to get exons
exons = remove_introns(dna_sequence, introns)
    
# Transcribe to RNA
rna_sequence = transcribe_to_rna(exons)
    
# Translate to protein
protein_sequence = translate_rna_to_protein(rna_sequence)
    
# Output the protein sequence
print(protein_sequence)



