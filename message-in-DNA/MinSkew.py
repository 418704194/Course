#!/usr/bin/python
# Filename: Skew.py
 
text="CATTCCAGTACTTCATGATGGCGTGAAGA"
#text=input()
def Skew(text):
	num=[]
	num.append(0)
	for i in range(0,len(text)):
		if (text[i]=="C"):
			num.append(num[i]-1)
		elif (text[i]=="G"):
			num.append(num[i]+1)
		else :
			num.append(num[i])
	
	return num

def MinIndex(num):
	min=num[0]
	for i in range(1,len(num)):
		if (min>num[i]):
			min=num[i]
	
	loci=[]
	for i in range(0,len(num)):
		if (min==num[i]):
			loci.append(i)

	return loci

num=Skew(text)
loci = MinIndex(num)
print (" ".join(str(i) for i in loci))
