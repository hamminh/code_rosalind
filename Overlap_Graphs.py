from Bio import SeqIO

def overlap_graph(fasta_file, k=3):
    # Read file FASTA
    records = list(SeqIO.parse(fasta_file, "fasta"))
    
    # Save names and strings in a dictionary
    dna_strings = {record.id: str(record.seq) for record in records}
    
    # List of graph edges
    edges = []
    
    # Compare all pairs of strings to check overlap conditions
    for id1, seq1 in dna_strings.items():
        suffix = seq1[-k:]
        for id2, seq2 in dna_strings.items():
            if id1 != id2 and seq2.startswith(suffix):  # Check overlap conditions
                edges.append((id1, id2))
    
    return edges

# Print edge list
def print_edges(edges):
    for edge in edges:
        print(edge[0], edge[1])

fasta_file = "rosalind_grph.txt"
edges = overlap_graph(fasta_file)
print_edges(edges)
