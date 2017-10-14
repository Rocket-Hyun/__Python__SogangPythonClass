textFile = open("howtostartastartup.txt", "r")
text = textFile.read()
wordsArray = text.split()
analyze = {}
for word in wordsArray:
    analyze[word] = analyze.get(word, 0) + 1
sortedAnalyze = sorted(analyze.items(), key=lambda kv:kv[1], reverse=True)
#print(sortedAnalyze[:30])

cnt = 0
for k, v in sortedAnalyze:
    print(k, v)
    if cnt > 100: break
    cnt += 1
