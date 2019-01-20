def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    for i in range(0,len(Text)-len(Pattern)+1):
        if HammingDistance(Pattern,Text[i:(i+len(Pattern))])<= d:
            positions.append(i)
    return positions

def HammingDistance(str1,str2):
    diff = 0
    for i in range(0,len(str1)):
        if str1[i]!=str2[i]:
            diff = diff + 1
    return(diff)
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    for i in range(0,len(Text)-len(Pattern)+1):
        if HammingDistance(Pattern,Text[i:(i+len(Pattern))])<= d:
            count = count + 1
    return count

str1 = input()
str2 = input()
print(HammingDistance (str1,str2))