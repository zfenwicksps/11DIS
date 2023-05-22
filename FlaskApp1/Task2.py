
isomorph1 = []
isomorph2 = []
word1 = "doko"
word2 = "book"
if len(word1) == len(word2):
    for index, char in enumerate(word1):
        if word1.count(char) > 1:
            n = 0
            n = index + 1

            while n < len(word1):
                print(word1[index])
                print(word1[n])
                if word1[index] == word1[n]:
                    isomorph1.append(f"+{n-index}")
                    n += 1
                #elif :
                #   isomorph1.append('0')
                else:
                    n += 1

        else:
            isomorph1.append('0')
else:
    print("Words are different lengths")
print(isomorph1)
