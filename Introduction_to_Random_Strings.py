import math

def compute_log_probabilities(dna_string, gc_contents):
    result = []
    
    # Iterate through each GC-content
    for gc_content in gc_contents:
        log_prob = 0
        
        # Calculate probabilities for each nucleotide in the string
        for nucleotide in dna_string:
            if nucleotide in 'GC':
                prob = gc_content / 2
            elif nucleotide in 'AT':
                prob = (1 - gc_content) / 2
            else:
                raise ValueError("Invalid nucleotide in DNA string.")
            
            # Add the log10 of the probability to the result
            log_prob += math.log10(prob)
        
        result.append(log_prob)
    
    return result


dna_string = "AGCTCTTTTAGACCATGAGCTCGTCCAGAGGAACGCATCCCAACACGGAAGACATCATACGAGCGTGTTATATACAGGGCGATGGAATAA"
gc_contents = [0.084, 0.162, 0.219, 0.285, 0.341, 0.417, 0.440, 0.548, 0.572, 0.627, 0.724, 0.764, 0.829, 0.877]

log_probabilities = compute_log_probabilities(dna_string, gc_contents)

for prob in log_probabilities:
    print(f"{prob:.3f}")
