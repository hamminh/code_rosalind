def transition_transversion_ratio(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("DNA strings must be of the same length.")
    
    transitions = 0
    transversions = 0
    
    transition_pairs = {('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')}
    
    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            if (char1, char2) in transition_pairs:
                transitions += 1
            else:
                transversions += 1
    
    # Handle the case where there are no transversions
    if transversions == 0:
        if transitions > 0:
            return float('inf')  # Infinite ratio when no transversions and some transitions
        else:
            return 0.0  # No changes at all
    
    return transitions / transversions



from Bio import SeqIO   

sequences = []                             
handle = open('rosalind_tran.txt', 'r')     
for record in SeqIO.parse(handle, 'fasta'):
    sequences.append(str(record.seq))      
handle.close()                             
s1 = sequences[0]                           
s2 = sequences[1]  


# Example usage

print(transition_transversion_ratio(s1, s2))  # Output will be the ratio R(s1, s2)
