# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
def Motifs(Profile, Dna):
    # insert your code here
    t = len(Dna)
    kmer = len(Profile["A"])
    motifs = []
    for i in range(0, t):
        motifs.append(ProfileMostProbablePattern(Dna[i], kmer, Profile))
    return(motifs)
    

# Insert your ProfileMostProbablePattern(Text, k, Profile) and Pr(Pattern, Profile) functions here.
def ProfileMostProbablePattern(Text, k, Profile):
    # insert your code here. Make sure to use Pr(Text, Profile) as a subroutine!
    pr = []
    for i in range(len(Text)-k+1):
        pr.append ( Pr(Text[i:(i+k)],Profile))
    pr_max = max(pr)
    seq = ""
    for i in range(len(pr)):
        if pr[i]==pr_max:
            seq = Text[i:(i+k)]
            break
    return seq


def Pr(Pattern, Profile):
    p = 1
    for i in range(len(Pattern)):
        p = p * Profile[Pattern[i]][i]
    return p
    

import sys
con = sys.stdin.read().splitlines()
motifs = [ [ float(j) for j in i.split(" ")] for i in con[:4] ]
motifs = {"A" : motifs[0], "C":motifs[1], "G":motifs[2], "T":motifs[3]}
dna = con[4:]
print(Motifs(motifs, dna))
