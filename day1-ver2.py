import operator

textFile = open("howtostartastartup.txt", "r")
text = textFile.read()
wordsArray = text.split()
analyze = {}
for word in wordsArray:
    analyze[word] = analyze.get(word, 0) + 1
    # dictionary에 get(a,b)은 a key값이 있으면 그 value를 리턴하고 없으면 b를 리턴하는 메서드
sortedAnalyze = sorted(analyze.items(), key=lambda kv:kv[1], reverse=True)
# sorted() list에서는 자동 순서 배열
# 그 안에 dictionary를 넣으면 key값으로 자동 순서 배치 (키 값만 남기고 list로 변경)
# dictionary items()는 키/밸류 페어로 배열 만들어줌  
print(sortedAnalyze[:30])
