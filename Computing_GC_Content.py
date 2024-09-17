from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

def find_highest_gc_content(fasta_file):
    max_gc_content = -1
    max_gc_id = ""

    # Read file FASTA and caculate GC-content
    for record in SeqIO.parse(fasta_file, "fasta"):
        gc_content = gc_fraction(record.seq) * 100  # Caculate GC-content
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_gc_id = record.id
    
    return max_gc_id, max_gc_content


fasta_file = "rosalind_gc.txt"
id_with_max_gc, gc_content = find_highest_gc_content(fasta_file)
print(f"{id_with_max_gc}\n{gc_content:.3f}")
