# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
def CountWithPseudocounts(Motifs):
    k = len(Motifs[0])
    # insert your code here
    count = {}
    for alp in "AGCT":
        count[alp] = [1] * k
    for i in range(len(Motifs)):
        for j in range(k):
            print (Motifs[i][j])
            count[Motifs[i][j]][j] += 1
    return (count)

import sys
motifs = sys.stdin.read().splitlines()
print(CountWithPseudocounts(motifs))