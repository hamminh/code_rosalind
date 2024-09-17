reverse_comp=""
dna = input('dna:')
def reverse_complement(dna):
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a':'t', 'c':'g', 'g':'c' , 't':'a'}
        reverse = dna[::-1]
        reverse_complement = ''.join([complement[base] for base in reverse])
        return reverse_complement
reverse_comp = reverse_complement(dna)
print('    raeverse_complement :', reverse_comp)