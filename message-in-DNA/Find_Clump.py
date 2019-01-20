#!/usr/bin/python
# Filename: if.py
 
genome=input()
#genome="CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTA"
#kmer,win,n= map(int,input().split()) 
kmer=9
win=500
n=3
#print(len(text))
#print (len(patter))
def Count(text,kmer,n):
	out=[]
	dict = {}
	for i in range(0,len(text)-kmer+1):
		#print (i,i+len(pat),text[i:(i+len(pat))])
		if text[i:(i+kmer)] in dict:
			dict[text[i:(i+kmer)]]+=1
		else:
			dict[text[i:(i+kmer)]]=1
	
	for key in dict:
		if dict[key]>=n:
			out.append(key)
	
	return out

#save result
out=[]

#windows foreach
for i in range(0,len(genome)-win+1):
	win_count=Count(genome[i:(i+win)],kmer,n)
	if len(win_count)>0:
		out.append(win_count)


out2 = {}
for i in range(0,len(out)):
	tmp=out[i][0]
	out2[tmp]=1

print(" ".join(str(i) for i in out2.keys()))  


