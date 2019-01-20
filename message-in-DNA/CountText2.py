
text=input()
kmer=int(input())

patter = {}
for i in range(0,len(text)-kmer+1) :
	pat = text[i:(i+kmer)]
	if pat in patter :
		patter[pat] = patter[pat] + 1
	else : 
		patter[pat] = 1

Mnum = -1
Mseq = []
for key in patter:
	if patter[key] > Mnum : 
		Mnum = patter[key]
		Mseq = [key]
	elif patter[key] == Mnum:
		Mseq.append(key)

print (" ".join(k for k in Mseq))