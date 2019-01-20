#!/usr/bin/python
#text,k= map(str,input().split()) 
#k=int(k)
text=input()
k=int(input())

def PatternToNumber(pattern):
	num=0;
	Len=len(pattern)
	for i in range(0,Len):
		index=0;
		if (pattern[i]=="A") :
			index=0
		elif (pattern[i]=="C"):
			index=1
		elif (pattern[i]=="G"):
			index=2
		elif (pattern[i]=="T"):
			index=3
		num=num+index*(4**(Len-i-1))
	return num


def ComputingFrequencies(text,k):
	FreArray=[]
	for i in range (0,4**k):
		FreArray.append(0)
	for i in range(0,len(text)-k+1):
		index=PatternToNumber(text[i:i+k])
		FreArray[index]=FreArray[index]+1
	return FreArray
FreArray=ComputingFrequencies(text,k)
print (' '.join(map(str,FreArray)))

