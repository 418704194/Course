
text=input()
kmer,win,num= map(int,input().split()) 

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
pat_num = {}

while index+win <= len(text):
    seq = Clump(text[index:(index+win)],kmer,num)
    index = index + 1

    for x in seq :
        if x not in pat_num :
            pat_num[x] = 1
        else :
            pat_num[x] += 1 
print (pat_num.keys())

unique_pat_num = []
for k in pat_num.keys():
    if pat_num[k]==1:
        unique_pat_num.append(k)

print (" ".join(unique_pat_num))