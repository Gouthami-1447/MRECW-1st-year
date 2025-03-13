from itertools import permutations

# Read the input
s, k = input().split()
k = int(k)

# Generate all permutations of length k from the string s, sorted lexicographically
perm = permutations(sorted(s), k)

# Print each permutation
for p in perm:
    print(''.join(p))