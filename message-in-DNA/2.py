# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    revComp = '' # output variable
    comp = complement(Pattern)
    for i in range(len(Pattern)):
        revComp = revComp + comp[len(Pattern)-i-1]
    return revComp


# Copy your reverse function from the previous step here.


# HINT:   Filling in the following function is optional, but it may come in handy when solving ReverseComplement
# Input:  A character Nucleotide
# Output: The complement of Nucleotide
def complement(Nucleotide):
    comp = '' # output variable
    for i in range(len(Nucleotide)):
        if Nucleotide[i]=='A':
            comp = comp + 'T'
        elif Nucleotide[i]==  'T':
            comp = comp + 'A'
        elif Nucleotide[i]==  'G':
            comp = comp + 'C'
        elif Nucleotide[i]==  'C':
            comp = comp + 'G'
    return comp



### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
print(ReverseComplement(sys.stdin.read().strip()))