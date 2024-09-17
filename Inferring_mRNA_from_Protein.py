def count_rna_strings(protein_string):
    MOD = 1_000_000
    
    # Codon table for each amino acid (excluding the stop codon)
    codon_count = {
        'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2, 'I': 3,
        'K': 2, 'L': 6, 'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6, 'S': 6,
        'T': 4, 'V': 4, 'W': 1, 'Y': 2
    }
    
    # Number of possible RNA strings
    num_rna_strings = 1
    
    # Calculate total number of RNA strings
    for amino_acid in protein_string:
        if amino_acid in codon_count:
            num_rna_strings *= codon_count[amino_acid]
            num_rna_strings %= MOD
        else:
            raise ValueError(f"Unknown amino acid: {amino_acid}")
    
    # Include the stop codon
    num_rna_strings *= 3  # 3 possible stop codons
    num_rna_strings %= MOD
    
    return num_rna_strings



protein_string = "MA" 
print(count_rna_strings(protein_string))
