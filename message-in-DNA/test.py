def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    # insert your code here
    profile = Count(Motifs)
    for i in profile.keys():
        for j in range(len(profile[i])):
            profile[i][j] = profile[i][j]/t
    return profile
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
DNA = ["AAGCCAAA", "AATCCTGG", "GCTACTTG", "ATGTTTTG"]
Motif = ["CCA", "CCT", "CTT","TTG"]
print(Motifs(Profile(Motif), DNA))

