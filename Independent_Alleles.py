from math import comb

def binomial_probability(k, N):
    # Number of children in the k-th generation
    num_children = 2 ** k
    
    # Probability of having genotype Aa Bb (AaBbxAaBb --> AaBb=0.25)
    p = 0.25
    
    # Calculate the cumulative probability of having less than N Aa Bb organisms
    cumulative_prob = 0
    for x in range(N):
        prob = comb(num_children, x) * (p ** x) * ((1 - p) ** (num_children - x))
        cumulative_prob += prob
    
    # Return the complement probability: P(X >= N)
    return 1 - cumulative_prob

# Example usage:
k = 2  # Number of generations
N = 1  # Minimum number of Aa Bb organisms
result = binomial_probability(k, N)
print(f"{result:.3f}")
