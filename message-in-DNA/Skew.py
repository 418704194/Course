#!/usr/bin/python
# Filename: Skew.py
 
#text="GAGCCACCGCGATA"
text=input()
def skew(text):
	num=[]
	num.append(0)
	for i in range(0,len(text)):
		if (text[i]=="C"):
			num.append(num[i]-1)
		elif (text[i]=="G"):
			num.append(num[i]+1)
		else :
			num.append(num[i])
	
	return " ".join(str(k) for k in num)

print (skew(text))
