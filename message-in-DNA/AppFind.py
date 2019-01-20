#!/usr/bin/python
# Filename: if.py
 
text=input()
k,dis=map(int,input().split()) 

#text="ACGTTGCATGTCGCATGATGCATGAGAGCT"
#k=4
#dis=1

#cal distance
def Hamming(p,q):
	num=0
	for i in range(0,len(p)):
		if (p[i]!=q[i]):
			num=num+1
	return num

#naming
def NumberToPattern(num,Len):
	char=("A","C","G","T")
	pattern=[]
	while Len>0 :
		pattern.append(char[num//(4**(Len-1))])
		num=num%(4**(Len-1))
		Len=Len-1
	
	return ''.join(pattern)
#find max index
def MaxIndex(num):
	max=num[0]
	for i in range(1,len(num)):
		if (max<num[i]):
			max=num[i]
	
	loci=[]
	for i in range(0,len(num)):
		if (max==num[i]):
			loci.append(i)

	return loci

#foreach
def Count(text,k,distance):
	#cal frequence
	FreArray=[]
	NameArray=[]
	for i in range (0,4**k):
		FreArray.append(0)
		NameArray.append(NumberToPattern(i,k))

	for i in range(0,len(text)-k+1):
		for j in range (0,4**k):
			if Hamming(text[i:(i+k)],NameArray[j])<=distance:
				FreArray[j]=FreArray[j]+1
	loci=MaxIndex(FreArray)
	pattern=[]
	for i in range(0,len(loci)):
		pattern.append(NameArray[loci[i]])
	return pattern


print (" ".join(Count(text,k,dis)))



