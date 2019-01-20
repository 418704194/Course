
def skew(Genome):
    array = []
    array.append(0)
    for i in range(0,len(Genome)):
        if Genome[i] == "G":
            array.append( array[i] + 1 )
        elif Genome[i] == "C":
            array.append( array[i] - 1 )
        else :
            array.append( array[i] )
    return array
def MinimumSkew(Genome):
    positions = [] # output variable
    # your code here
    array = skew(Genome)
    maxv = min(array)
    for i in range(0,len(array)):
        if array[i] == maxv:
            positions.append(i)
    return positions

Genome = input()
#Genome = "AAAAGGGG"
#Symbol = "A"
pos = MinimumSkew(Genome)
print (" ".join(str(i) for i in pos))
