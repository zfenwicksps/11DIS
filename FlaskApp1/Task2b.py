
isomorph1= []
isomorph2= []
word1 = "doko"
word2 = "book"
print(len(word1)-1)
if len(word1) == len(word2):
	for indexa, chara in enumerate(word1):
		if word1.count(chara) > 1:
			for indexb, charb in enumerate(word1):
				if indexa <= indexb:
					if indexb == len(word1)-1 and chara == charb:
						print(indexb)
						isomorph1.append('')
				else:
					if chara == charb:
						isomorph1.append(f"+{indexa-indexb}")

					else:
						isomorph1.append('0')
		else:
			isomorph1.append('0')

	if isomorph1 == isomorph2:
		print("The words are isomorphic pairs")

	else:
		print("The words are not isomorphic pairs")
else:
	print("The words are different lengths")
print(isomorph1)
