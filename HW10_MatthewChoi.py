def initialLetterCount(wordList):
    dict={}
    for i in range(len(wordList)):
        if wordList[i][0] in dict:
            dict[wordList[i][0]] = dict[wordList[i][0]] +1
        else:
            dict[wordList[i][0]] = 1
    return dict

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))

def initialLetters(wordList):
    dict={}
    for i in wordList:
        if i[0] not in dict:
            dict[i[0]]=[i]
        elif i not in dict[i[0]]:
            dict[i[0]].append(i)
    return dict

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say', 'wit']

print(initialLetters(horton))
