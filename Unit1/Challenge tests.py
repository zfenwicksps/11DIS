'''
capitals = []
def capital_indexes(word):
    for char in word:
        if char.isupper() == True:
            capitals.append(word.find(char))
capital_indexes("HI")
print(capitals)

def mid(word):
    length = len(word)
    if length%2 != 0:
        mchar = length//2
        print(word[mchar])
mid("abc")
'''
