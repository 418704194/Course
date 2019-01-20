#!/usr/bin/python
# Filename: if.py
 
patter="CTTGATCAT"
text=input()

#print(len(text))
#print (len(patter))
def Count(text,pat):
	num=[]
	for i in range(0,len(text)-len(pat)+1):
		#print (i,i+len(pat),text[i:(i+len(pat))])
		if text[i:(i+len(pat))]==pat:
			num.append(i)
		
	return num

num=Count(text,patter)

print (" ".join(str(k) for k in num))

