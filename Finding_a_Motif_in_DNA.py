def find_substring_locations(s, t):
    positions = []
    
    # Loop through each position in s to find the positions of t
    for i in range(len(s) - len(t) + 1):
        if s[i:i + len(t)] == t:
            positions.append(i + 1)  # Add the starting position to the result, numbering from 1
    
    return positions

# Input
s = "ACGTACGTGACGGTAGTAGTA"
t = "GTA"

# Output
result = find_substring_locations(s, t)
print(result)
