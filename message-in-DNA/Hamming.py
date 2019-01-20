#!/usr/bin/python
# Filename: Skew.py
 
#p=input()
#q=input()
p="CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG"
q="ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"
def Hamming(p,q):
	num=0
	for i in range(0,len(p)):
		if (p[i]!=q[i]):
			num=num+1
	return num

print (Hamming(p,q))
