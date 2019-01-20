# Insert your Count(Motifs) function here from the last Code Challenge.
def Count(Motifs):
    count = {} # initializing the count dictionary
    # your code here
    mlen = len(Motifs[0])
    for alp in "AGCT":
        count[alp] = [0] * mlen
    for i in range(len(Motifs)):
        for j in range(mlen):
            count[Motifs[i][j]][j] += 1
    return count

# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
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


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
print(Profile(sys.stdin.read().splitlines()))