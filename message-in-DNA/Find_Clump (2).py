#!/usr/bin/python
# Filename: if.py
 
genome=input()
#genome="CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTA"
kmer,win,n= map(int,input().split()) 

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
		if dict[key]==n:
			out.append(key)
	
	return out

#save result
out={}

#windows foreach
for i in range(0,len(genome)-win+1):
    win_count=Count(genome[i:(i+win)],kmer,n)
	#print (win_count)
	for x in win_count :
		if x in out :
			out[x] = out[x]+1
		else :
			out[x] = 1
	i = i + win

print (out)
out2 = []
for i in out.keys():
	if out[i]==1 :
		out2.append(i)

print(" ".join(out2))


