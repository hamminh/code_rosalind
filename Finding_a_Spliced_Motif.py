from Bio import SeqIO                      


sequences = []                             
handle = open('test.fasta', 'r')     
for record in SeqIO.parse(handle, 'fasta'):
    sequences.append(str(record.seq))      
handle.close()                             
s = sequences[0]                           
t = sequences[1]                           



pos = 0                                    
positions = []                             
for i in range(len(t)):                    
    for j in range(pos, len(s)):           
        pos += 1                           
        if len(positions) < len(t):        
            if t[i] == s[j]:               
                positions.append(pos)      
                break                      
print(*positions, sep=' ')
