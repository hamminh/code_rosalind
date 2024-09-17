# Define the monoisotopic masses for each amino acid "https://proteomicsresource.washington.edu/protocols06/masses.php"
monoisotopic_mass = {
    'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
    'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406,
    'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
    'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
    'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333
}

# Calculate total weight
def calculate_total_weight(protein_string):
    total_weight = 0.0
    for amino_acid in protein_string:
        if amino_acid in monoisotopic_mass:
            total_weight += monoisotopic_mass[amino_acid]
    return total_weight


protein_string = "SKADYEK"
total_weight = calculate_total_weight(protein_string)
print(f"{total_weight:.3f}")


