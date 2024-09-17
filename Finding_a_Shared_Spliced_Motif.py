from Bio import SeqIO

# Compute the longest common subsequence of strings s and t
def longest_common_subsequence(s, t):
    m, n = len(s), len(t)
    # Create a DP table initialized to 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Recover the LCS from the DP table
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            lcs.append(s[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    # The LCS is built backwards, so reverse it
    lcs.reverse()
    
    return ''.join(lcs)

sequences = []                             
handle = open('rosalind_lcsq.txt', 'r')     
for record in SeqIO.parse(handle, 'fasta'):
    sequences.append(str(record.seq))      
handle.close()                             
s = sequences[0]                           
t = sequences[1] 


lcs = longest_common_subsequence(s, t)
print(lcs)
