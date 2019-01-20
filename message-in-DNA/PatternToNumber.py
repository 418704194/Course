#!/usr/bin/python

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

pattern=input()
print (PatternToNumber(pattern))