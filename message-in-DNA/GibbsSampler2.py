# import the random package
import random
# Copy your GibbsSampler function (along with all required subroutines) below this line
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

# Copy the ten strings occurring in the hyperlinked DosR dataset below.
Dna = ["GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC",
"CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG",
"ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC",
"GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC",
"GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG",
"CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA",
"GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA",
"GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG",
"GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG",
"TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"]

# set t equal to the number of strings in Dna, k equal to 15, and N equal to 100
t = len(Dna)
k = 15
N = 100
# Call GibbsSampler(Dna, k, t, N) 20 times and store the best output in a variable called BestMotifs
BestMotifs = GibbsSampler(Dna, k, t, N)
for i in range(100):
    tmpmotif = GibbsSampler(Dna, k, t, N)
    if Score(BestMotifs) > Score(tmpmotif):
        BestMotifs = tmpmotif.copy()
# Print the BestMotifs variable
print(BestMotifs)
# Print Score(BestMotifs)
print(Score(BestMotifs))