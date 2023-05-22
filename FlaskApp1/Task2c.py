isomorph1 = []
isomorph2 = []
word1 = input("Input a first word: ")
word2 = input("Input a second word: ")
if len(word1) == len(word2):
	for indexa, chara in enumerate(word1):
		if word1.count(chara) > 1:
			for indexb, charb in enumerate(word1):
				if indexa < indexb:
					if chara == charb:
						isomorph1.append(f"+{indexb-indexa}")
						break
					elif charb == word1[len(word1)-1]:
						isomorph1.append('0')
				else:
					if indexb == len(word1)-1 and chara == charb:
						isomorph1.append('0')
		else:
			isomorph1.append('0')
	for indexa, chara in enumerate(word2):
		if word2.count(chara) > 1:
			for indexb, charb in enumerate(word2):
				if indexa < indexb:
					if chara == charb:
						isomorph2.append(f"+{indexb-indexa}")
						break
					elif charb == word2[len(word2)-1]:
						isomorph2.append('0')
				else:
					if indexb == len(word2)-1 and chara == charb:
						isomorph2.append('0')
		else:
			isomorph2.append('0')
	if isomorph1 == isomorph2:
		final = ' '.join(isomorph1)
		print("The words are isomorphic pairs")
		print(f"With the pattern {final}")
	else:
		print("The words are not isomorphic pairs")
else:
	print("The words are different lengths")
