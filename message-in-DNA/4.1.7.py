# first, import the random package
import random
# Input:  A dictionary Probabilities whose keys are k-mers and whose values are the probabilities of these kmers
# Output: A randomly chosen k-mer with respect to the values in Probabilities
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

