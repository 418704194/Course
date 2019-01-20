#!/usr/bin/python
# Filename: if.py
 
text=input()
patter=input()
#print(len(text))
#print (len(patter))
def Count(text,pat):
	n=0;
	for i in range(0,len(text)-len(pat)+1):
		#print (i,i+len(pat),text[i:(i+len(pat))])
		if text[i:(i+len(pat))]==pat:
			n=n+1
		
	return n
num=Count(text,patter)

print (num)



