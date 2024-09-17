import itertools
n = 3
alphabet = 'WZHNDMKXFOQ'
perm = []

for i in range(1, n + 1):
    perm.append(list(map(''.join, (itertools.product(alphabet, repeat=i)))))
permutations = list(itertools.chain(*perm))
srt_perm = sorted(permutations,
                  key=lambda word: [alphabet.index(c) for c in word])


for j in srt_perm:
    print(j)
