
def PatternCount2(Len, Text):
    count = {}
    for i in range(len(Text)-Len+1):
        pattern = Text[i:(i+Len)]
        if pattern in count:
            count[pattern] = count[pattern] + 1
        else:
            count[pattern] = 1
    return count 

def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    Genome = Genome + Genome[0:n//2]
    count = PatternCount2(len(symbol),Genome[0:n//2])
    if symbol in count:
        array[0] = count[symbol]
    else:
        array[0] = 0
    for i in range(1,n):
        pattern = Genome[(i-1):(i-1+len(symbol))]
        count[pattern] = count[pattern] -1 
        pattern = Genome[(i+(n//2)-len(symbol)):(i+(n//2))]
        if pattern in count:
            count[pattern] = count[pattern] + 1
        else:
            count[pattern] = 1

        if symbol in count:
            array[i] = count[symbol]
        else:
            array[i] = 0
    return array
Genome = input()
Symbol = input()
#Genome = "AAAAGGGG"
#Symbol = "A"
print (SymbolArray(Genome,Symbol))
