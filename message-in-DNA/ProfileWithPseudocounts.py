# Input:  A set of kmers Motifs
# Output: ProfileWithPseudocounts(Motifs)
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {} # output variable
    count = CountWithPseudocounts(Motifs)
    for i in count.keys():
        profile[i] = [float(count[i][j])/(count["A"][j] + count["G"][j] + count["C"][j] + count["T"][j]) for j in range(k)]
    return profile

# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
# HINT:   You need to use CountWithPseudocounts as a subroutine of ProfileWithPseudocounts
def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {} # output variable
    for alp in "AGCT":
        count[alp] = [1] * k
    for i in range(len(Motifs)):
        for j in range(k):
            #print (Motifs[i][j])
            count[Motifs[i][j]][j] += 1
    return count

import sys
motifs = sys.stdin.read().splitlines()
print(ProfileWithPseudocounts(motifs))