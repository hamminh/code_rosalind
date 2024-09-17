def dominant_phenotype_probability(k, m, n):
    total = k + m + n  # Total number of organisms
    
    # Probabilities of selecting specific pairs
    P_aa_aa = (n / total) * ((n - 1) / (total - 1))  # both recessive
    P_Aa_aa = (m / total) * (n / (total - 1)) + (n / total) * (m / (total - 1))  # one heterozygous and one recessive
    P_Aa_Aa = (m / total) * ((m - 1) / (total - 1))  # both heterozygous
    
    # Probability of producing recessive offspring
    P_recessive = P_aa_aa + P_Aa_aa * 0.5 + P_Aa_Aa * 0.25
    
    # The probability of producing dominant phenotype is the complement of recessive probability
    P_dominant = 1 - P_recessive
    
    return P_dominant

# Example usage:
k = 28  # homozygous dominant (AA)
m = 25  # heterozygous (Aa)
n = 28  # homozygous recessive (aa)

result = dominant_phenotype_probability(k, m, n)
print(f"{result:.5f}")
