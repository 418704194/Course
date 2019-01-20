text = input()

def rev(text):
	text2 = ""
	for i in range(0,len(text)):
		text2 = text2 + text[len(text)-i-1]
	return text2

def com(text):
	text2 = ""
	for i in range(0,len(text)):
		if (text[i]=="A"):
			text2 = text2 + "T"
		elif (text[i]=="T"):
			text2 = text2 + "A"
		elif (text[i]=="G"):
			text2 = text2 + "C"
		elif (text[i]=="C"):
			text2 = text2 + "G"
	return text2
		
print (rev(com(text)))
