def HammingDistance(str1,str2):
	diff = 0
	for i in range(0,len(str1)):
		if str1[i]!=str2[i]:
			diff = diff + 1
	return(diff)

str1 = input()
str2 = input()
print(HammingDistance (str1,str2))