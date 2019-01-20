#!/usr/bin/python
# Filename: Skew.py
 
pattern=input()
#pattern="ATTCTGGA"
text=input()
#text="CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
dis=int(input())
#dis=3

def Hamming(p,q):
	num=0
	for i in range(0,len(p)):
		if (p[i]!=q[i]):
			num=num+1
	return num

def AppMatch(text,pattern,distance):
	loci=[]
	len_pat=len(pattern)
	for i in range(0,len(text)-len(pattern)+1):
		if (Hamming(pattern,text[i:i+len_pat])<=distance):
			loci.append(i)

	return loci

loci=AppMatch(text,pattern,dis)
print (" ".join(str(i) for i in loci))
