from Bio import SeqIO

# Function to check if a given substring exists in all DNA strings
def is_common_substring(substring, dna_strings):
    return all(substring in dna for dna in dna_strings)

# Function to find the longest common substring
def find_longest_common_substring(dna_strings):
    # Start with the shortest string, since the longest common substring must be a substring of it and use binary search on the length of the substring
    shortest_string = min(dna_strings, key=len)
    length = len(shortest_string)
    longest_common_substr = ""

    # Check all possible substrings of the shortest string
    for i in range(length):
        for j in range(i + len(longest_common_substr) + 1, length + 1):
            candidate = shortest_string[i:j]
            if is_common_substring(candidate, dna_strings):
                longest_common_substr = candidate

    return longest_common_substr

# Function to handle FASTA input and return the result
def longest_common_substring_from_fasta(fasta_file):
    dna_strings = [str(record.seq) for record in SeqIO.parse(fasta_file, "fasta")]
    return find_longest_common_substring(dna_strings)


fasta_file = "rosalind_lcsm.txt"
result = longest_common_substring_from_fasta(fasta_file)
print(result)
