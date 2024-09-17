from Bio import SeqIO

# Read the FASTA file and store sequences
reads = []
handle = open('rosalind_long.txt', 'r')
for record in SeqIO.parse(handle, 'fasta'):
    reads.append(str(record.seq))
handle.close()

# Find overlaps between reads
overlaps = []
overlapping = []
for i in range(len(reads)):
    curr_read = reads[i]
    for j in range(len(curr_read) // 2, len(curr_read)):
        curr_suffix = curr_read[-(j + 1):]
        for k in range(len(reads)):
            curr_comp = reads[k]
            for l in range(len(curr_comp) // 2, len(curr_comp)):
                curr_prefix = curr_comp[:l]
                if curr_suffix == curr_prefix:
                    overlaps.append(k)
                    overlapping.append([len(curr_suffix), i, k])

# Find the first read and build the superstring
s = set(overlaps)
first_read = ''
count = len(overlapping)
for m in range(len(overlapping)):
    suf_index = overlapping[m][1]
    if suf_index not in s:           #find first read and initialise new str
        first_read = suf_index
        new_str = reads[overlapping[m][1]] + reads[overlapping[m][2]][
            overlapping[m][0]:]
        count -= 1
        pref_index = overlapping[m][2]
        while count > 0:                       #when the first read is found, add 
            for n in range(len(overlapping)):  #the remaining in the correct order
                if pref_index == overlapping[n][1]:
                    new_str += reads[overlapping[n][2]][overlapping[n][0]:]
                    pref_index = overlapping[n][2]
                    count -= 1

print(new_str)

