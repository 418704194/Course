# first, import the random package
import random

# Input:  Integers k, t, and N, followed by a collection of strings Dna
# Output: GibbsSampler(Dna, k, t, N)
def GibbsSampler(Dna, k, t, N):
    BestMotifs = [] # output variable
    # your code here
    Motif = RandomMotifs(Dna, k, t)
    BestMotifs = Motif.copy()
    for j in range(N):
        i = random.randint(0, t-1)
        Motif2 = [Motif[z] for z in range(t) if z != i ]
        Profile = ProfileWithPseudocounts(Motif2)
        Motif[i] = ProfileMostProbablePattern(Dna[i], k, Profile)
        if Score(Motif) < Score(BestMotifs):
            BestMotifs = Motif
        else:
            return BestMotifs 

    return BestMotifs

# place all subroutines needed for GibbsSampler below this line
def Count(Motifs):
    count = {} # initializing the count dictionary
    # your code here
    mlen = len(Motifs[0])
    for alp in "ACGT":
        count[alp] = [0] * mlen
    for i in range(len(Motifs)):
        for j in range(mlen):
            count[Motifs[i][j]][j] += 1
    return count

def RandomMotifs(Dna, k, t):
    # place your code here. 
    motifs = []
    n = len(Dna[0])-k
    for i in range(t):
        seed = random.randint(0,n)
        motifs.append(Dna[i][seed:(seed+k)])
    return(motifs)

def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    con = ""
    for i in range(k):
        num = 0
        for j in "AGCT":
            if count[j][i]>num:
                num = count[j][i]
                seq = j
        con = con + seq
    return con

def Score(Motifs):
    # Insert code here
    sum = 0
    con = Consensus(Motifs)
    for i in range(len(Motifs)):
        for j in range(len(Motifs[0])):
            if con[j] != Motifs[i][j]:
                sum += 1
    return sum

def ProfileWithPseudocounts(Motifs):
    k = len(Motifs[0])
    profile = {} # output variable
    count = CountWithPseudocounts(Motifs)
    for i in count.keys():
        profile[i] = [float(count[i][j])/(count["A"][j] + count["G"][j] + count["C"][j] + count["T"][j]) for j in range(k)]
    return profile

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

def Motifs(Profile, Dna):
    # insert your code here
    t = len(Dna)
    kmer = len(Profile["A"])
    motifs = []
    for i in range(0, t):
        motifs.append(ProfileMostProbablePattern(Dna[i], kmer, Profile))
    return(motifs)

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

def Pr(Text, Profile):
    # insert your code here
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p

k = 8
t = 5 
n = 100
dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]

print(GibbsSampler(dna, k, t, n))
