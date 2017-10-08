import operator

textFile = open("howtostartastartup.txt", "r")
text = textFile.read()
wordsArray = text.split()
analyze = {}
for word in wordsArray:
    analyze[word] = analyze.get(word, 0) + 1
sortedAnalyze = sorted(analyze.items(), key=operator.itemgetter(1), reverse=True)    
print(sortedAnalyze[:20])
