
text=input()
kmer,win,num= map(int,input().split()) 

print(text)
def Clump(text,kmer,num):
    patter = {}
    for i in range(0,len(text)-kmer+1) :
        pat = text[i:(i+kmer)]
        if pat in patter :
            patter[pat] = patter[pat] + 1
        else : 
            patter[pat] = 1

    Mseq = []
    for key in patter:
        if patter[key] == num:
            Mseq.append(key)
    return(Mseq)

index = 0
seq = []

while index < len(text):
    seq = seq + Clump(text[index:(index+win-1)],kmer,num)
    index = index + kmer

print (seq)
useq = []
for x in seq:
    if x not in useq :
        useq.append(x)

print (" ".join(useq))