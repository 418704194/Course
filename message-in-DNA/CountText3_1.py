patter="CTTGATCAT"
text=input()


def Count(text,pat):
	num=[]
	for i in range(0,len(text)-len(pat)+1):
		if text[i:(i+len(pat))]==pat:
			num.append(i)
		
	return num


num = Count(text,patter)
print ( " ".join( str(k) for k in num))

