from itertools import product

def generate_lexicographic_strings(alphabet, n):
    # Generate all possible strings of length n from the given alphabet
    all_strings = [''.join(p) for p in product(alphabet, repeat=n)]
    
    # Sort the strings lexicographically
    all_strings.sort()
    
    return all_strings


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  
n = 3  

# Generate and print all lexicographically ordered strings
lexicographic_strings = generate_lexicographic_strings(alphabet, n)
    
for string in lexicographic_strings:
    print(string)

