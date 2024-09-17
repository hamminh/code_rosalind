data = []                                
with open('rosalind_lgis.txt', 'r') as f:   
    for line in f:                       
        for nr in line.split():          
            data.append(int(nr))         


#This first bit reads the file which contains the the length of the permutation and then the permutation, separated by spaces. The numbers are appended to a list as integers.
perm = data[1:]
# Function to find the longest increasing subsequence
def increasing(seq):
    # P will store the predecessors for each element in the sequence
    P = [None] * len(seq)
    # M will store the indices of the smallest end element of all increasing subsequences of different lengths
    M = [None] * len(seq)
    
    # Length of the longest increasing subsequence found so far
    L = 1
    M[0] = 0
    for i in range(1, len(seq)):
        lo = 0
        hi = L
        # If the current element is greater than the last element of the longest subsequence found so far
        if seq[M[hi - 1]] < seq[i]:
            j = hi
        else:
            # Binary search to find the position where seq[i] should be inserted
            while hi - lo > 1:
                mid = (hi + lo) // 2
                if seq[M[mid - 1]] < seq[i]:
                    lo = mid
                else:
                    hi = mid

            j = lo
        
        # Update the predecessor and index for the longest increasing subsequence
        P[i] = M[j - 1]
        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j + 1)

    result = []
    pos = M[L - 1]
    for k in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return (result[::-1])


# Function to find the longest decreasing subsequence
def decreasing(seq):
    # P will store the predecessors for each element in the sequence
    P = [None] * len(seq)
    # M will store the indices of the smallest end element of all decreasing subsequences of different lengths
    M = [None] * len(seq)

    # Length of the longest decreasing subsequence found so far
    L = 1
    M[0] = 0
    for i in range(1, len(seq)):
        lo = 0
        hi = L
        
        # If the current element is smaller than the last element of the longest subsequence found so far
        if seq[M[hi - 1]] > seq[i]:
            j = hi
        else:
            # Binary search to find the position where seq[i] should be inserted
            while hi - lo > 1:
                mid = (hi + lo) // 2
                if seq[M[mid - 1]] > seq[i]:
                    lo = mid
                else:
                    hi = mid

            j = lo
        # Update the predecessor and index for the longest decreasing subsequence
        P[i] = M[j - 1]
        if j == L or seq[i] > seq[M[j]]:
            M[j] = i
            L = max(L, j + 1)

    # Reconstruct the longest decreasing subsequence
    result = []
    pos = M[L - 1]
    for k in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return (result[::-1])

incr = increasing(perm)
decr = decreasing(perm)

print(*incr)
print(*decr)