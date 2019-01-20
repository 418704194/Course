

def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    Genome = Genome + Genome[0:n//2]
    count = PatternCount(symbol,Genome[0:n//2])
    array[0] = count
    for i in range(1,n):
        if Genome[(i-1):(i-1+len(symbol))] == symbol:
            count = count - 1
        if Genome[(i+(n//2)-len(symbol)):(i+(n//2))] == symbol:
            count = count + 1
        array[i] = count
    return array
Genome = input()
Symbol = input()
#Genome = "AAAAGGGG"
#Symbol = "A"
print (SymbolArray(Genome,Symbol))
