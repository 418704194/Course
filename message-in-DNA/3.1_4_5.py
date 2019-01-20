# Insert your Pr(Text, Profile) function here from Motifs.py.
def Pr(Text, Profile):
    # insert your code here
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p

# Input:  String Text, an integer k, and profile matrix Profile
# Output: ProfileMostProbablePattern(Text, k, Profile)
def ProfileMostProbablePattern(Text, k, Profile):
    # insert your code here. Make sure to use Pr(Text, Profile) as a subroutine!
    pr = []
    for i in range(len(Text)-k+1):
        pr.append ( Pr(Text[i:(i+k)],Profile))
    pr_max = max(pr)
    print (pr)
    seq = ""
    for i in range(len(pr)):
        if pr[i]==pr_max:
            seq = Text[i:(i+k)]
            break
    return seq

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
Text = lines[0]
k = int(lines[1])
A = [float(c) for c in lines[2].split()]
C = [float(c) for c in lines[3].split()]
G = [float(c) for c in lines[4].split()]
T = [float(c) for c in lines[5].split()]
Profile = {'A':A, 'C':C, 'G':G, 'T':T}
print(ProfileMostProbablePattern(Text,k,Profile))