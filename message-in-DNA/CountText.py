patter=input()
text=input()


def Count(text,pat):
	num=[]
	for i in range(0,len(text)-len(pat)+1):
		if text[i:(i+len(pat))]==pat:
			num.append(i)
		
	return num

num=len(Count(text,patter))

print num


