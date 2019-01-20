#!/usr/bin/python
#num,Len= map(int,input().split()) 
num= int(input()) 
Len= int(input()
) 

def NumberToPattern(num,Len):
	char=("A","C","G","T")
	pattern=[]
	while Len>0 :
		pattern.append(char[num//(4**(Len-1))])
		num=num%(4**(Len-1))
		Len=Len-1
	
	return ''.join(pattern)

print (NumberToPattern(num,Len))