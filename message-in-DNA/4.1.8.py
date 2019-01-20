# first, import the random package
import random
# then, copy Pr, Normalize, and WeightedDie below this line
def Normalize(Probabilities):
    # your code here
    freq = sum([Probabilities[i] for i in Probabilities.keys()])
    return ({i: Probabilities[i]/freq for i in Probabilities.keys()})

def WeightedDie(Probabilities):
    kmer = '' # output variable
    # your code here
    p = random.uniform(0, 1)
    tmp = 0
    for i in Probabilities:
        tmp = tmp + Probabilities[i]
        if p < tmp :
            kmer = i
            break
    return kmer

def Pr(Text, Profile):
    # insert your code here
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]

    return p

# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {} 
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)
