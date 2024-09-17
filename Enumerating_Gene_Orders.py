from itertools import permutations
import math

# Function generate permutations
def generate_permutations(n):
    # Generate all permutations of length n
    perm_list = list(permutations(range(1, n+1)))
    
    # Calculate the total number of permutations
    total_permutations = len(perm_list)
    
    return total_permutations, perm_list

def main(n):
    total_permutations, perm_list = generate_permutations(n)
    
    # Print the total number of permutations
    print(total_permutations)
    
    # Print each permutation
    for perm in perm_list:
        print(' '.join(map(str, perm)))


n = 5 
main(n)
