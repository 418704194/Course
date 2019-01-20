

def skew(Genome):
    array = {}
    array[0] = 0
    for i in range(0,len(Genome)):
        if Genome[i] == "G":
            array[i+1] = array[i] + 1
        elif Genome[i] == "C":
            array[i+1] = array[i] - 1
        else :
            array[i+1] = array[i]
    return array
Genome = input()
#Genome = "AAAAGGGG"
#Symbol = "A"
count = skew(Genome)
print (" ".join(str(count[i]) for i in count))
