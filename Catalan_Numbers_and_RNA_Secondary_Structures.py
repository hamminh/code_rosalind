from Bio import SeqIO
from Bio.Seq import Seq

MOD = 1000000

# Check if two nucleotides can form a valid base pair
def can_pair(a, b):
    return (a == 'A' and b == 'U') or (a == 'U' and b == 'A') or (a == 'C' and b == 'G') or (a == 'G' and b == 'C')

# Function to count noncrossing perfect matchings
def count_noncrossing_matchings(rna_sequence):
    n = len(rna_sequence)
    dp = [[0] * n for _ in range(n)]
    
    # Base case: Single nucleotide (no valid matchings)
    for i in range(n):
        dp[i][i] = 1  # Empty or single nucleotide has 1 way (no pairs)

    # Fill DP table for substrings of increasing length
    for length in range(2, n + 1):  # length of substring
        for i in range(n - length + 1):
            j = i + length - 1
            total = 0
            # Try to pair the first nucleotide with any nucleotide at position k
            for k in range(i + 1, j + 1, 2):  # Ensure k is even relative to i
                if can_pair(rna_sequence[i], rna_sequence[k]):
                    left_matchings = dp[i + 1][k - 1] if i + 1 <= k - 1 else 1
                    right_matchings = dp[k + 1][j] if k + 1 <= j else 1
                    total += left_matchings * right_matchings
                    total %= MOD  # Apply modulo at each step
            dp[i][j] = total

    return dp[0][n - 1]  # The result for the full string


# Read RNA sequence from a FASTA file
def read_rna_sequence(file_path):
    record = SeqIO.read(file_path, "fasta")
    rna_sequence = str(record.seq) 
    return rna_sequence


file = "rosalind_cat.txt"
rna_string = read_rna_sequence(file)
result = count_noncrossing_matchings(rna_string)
print(result) 
