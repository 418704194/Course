#!/usr/bin/python
# Filename: if.py
 
#text=input()
text="CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
#kmer=int(input())
kmer=3
#print(len(text))
#print (len(patter))
def Count(text,pat):
	n=0;
	for i in range(0,len(text)-len(pat)+1):
		#print (i,i+len(pat),text[i:(i+len(pat))])
		if text[i:(i+len(pat))]==pat:
			n=n+1
		
	return n

num=[]
max=0
for i in range(0,len(text)-kmer+1):
	num.append(Count(text,text[i:(i+kmer)]))
	if max<num[i]:
		max=num[i]

out={}
for i in range(0,len(num)):
	if max==num[i]:
		out[text[i:(i+kmer)]]=1

print(" ".join(str(i) for i in out.keys()))  