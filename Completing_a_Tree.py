data = []                                          
with open('rosalind_tree.txt', 'r') as f:             
    for line in f:                                 
        split_data = [int(x) for x in line.split()]
        data.append(split_data)                    

n = data[0][0]                                     
edges = data[1:]                                   
print(n - 1 - len(edges)) 