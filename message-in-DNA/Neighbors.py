#!/usr/bin/python
# Filename: if.py
 
text=input()
dis=int(input())

#cal distance
def Hamming(p,q):
	num=0
	for i in range(0,len(p)):
		if (p[i]!=q[i]):
			num=num+1
	return num


def NumberToPattern(num,Len):
	char=("A","C","G","T")
	pattern=[]
	while Len>0 :
		pattern.append(char[num//(4**(Len-1))])
		num=num%(4**(Len-1))
		Len=Len-1
	
	return ''.join(pattern)

def Neig(text,distance):
	nei=[]
	k=len(text)
	for i in range (0,4**k):
		tmp=NumberToPattern(i,k)
		if Hamming(text,tmp)<=distance :
			nei.append(tmp)
	return nei


RC=Neig(text,dis)
print("\n".join(RC))  
TET=[]
TET.append("0")
TET.append(str(r"\n".join(RC)))
print (TET)