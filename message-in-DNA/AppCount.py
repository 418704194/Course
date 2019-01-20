#!/usr/bin/python
# Filename: if.py
 
#text=input()
#patter=input()
#dis=input()

text="TACGCATTACAAAGCACA"
pattern="AA"
dis=1
#print(len(text))
#print (len(patter))
def Hamming(p,q):
	num=0
	for i in range(0,len(p)):
		if (p[i]!=q[i]):
			num=num+1
	return num

def Count(text,pat,distance):
	n=0;
	for i in range(0,len(text)-len(pat)+1):
		#print (i,i+len(pat),text[i:(i+len(pat))])
		if Hamming(text[i:(i+len(pat))],pat)<=distance:
			n=n+1
		
	return n
num=Count(text,pattern,dis)

print (num)



