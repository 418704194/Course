# Copy your Consensus(Motifs) function here.
def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    con = ""
    for i in range(k):
        num = 0
        alp = ""
        for j in "AGCT":
            if count[j][i]>num:
                num = count[j][i]
                seq = j
        con = con + seq
    return con

# Copy your Count(Motifs) function here.
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
# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    # Insert code here
    sum = 0
    con = Consensus(Motifs)
    for i in range(len(Motifs)):
        for j in range(len(Motifs[0])):
            if con[j] != Motifs[i][j]:
                sum += 1
    return sum        

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
print(Score(sys.stdin.read().splitlines()))