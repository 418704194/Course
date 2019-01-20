#!/usr/bin/python
# Filename: if.py
 
text=input()
k,dis=map(int,input().split()) 

#text="GGCGCTGGGCTCCGGCGCGGCTCCGGCGCGGCTCCGCGTCTCGGCGCCGGCGCCGTGGGCGCCGCGTCTGTCGCTGGCTCCGGGCGCCGGGCTCTCTGTCGGCTGTCCGGGCTGCGTGTCTCGCTGTGCGCGGCGGCGCGGCGCGCCGGCGCGGCTCTGGGCTCGGCGCGGCTCCGGGCTGTGTCGCTCTCTCGGCGGCGGCTCTGGCTCTCGCTCGGCTCTGTGGC"
#k=7
#dis=3

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
#index
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
#revcom
def Reverse(text):
	text2=""
	for i in range(0,len(text)):
		text2=text2+text[len(text)-i-1]
	return text2

def Complement(text):
	text2=""
	for i in range(0,len(text)):
		if text[i]=="A":
			text2=text2+"T"
		elif text[i]=="T":
			text2=text2+"A"
		if text[i]=="G":
			text2=text2+"C"
		elif text[i]=="C":
			text2=text2+"G"
	return text2
def Revcom(text):
	return Reverse(Complement(text))

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
	FreArray2=[]
	for i in range (0,4**k):
		FreArray2.append(FreArray[i]+FreArray[PatternToNumber(Revcom(NumberToPattern(i,k)))] )

	loci=MaxIndex(FreArray2)
	pattern=[]
	for i in range(0,len(loci)):
		#if ( not Revcom(NameArray[loci[i]]) in pattern ):
		pattern.append(NameArray[loci[i]])
	return pattern

print (" ".join(Count(text,k,dis)))
#print (Count(text,k,dis))


