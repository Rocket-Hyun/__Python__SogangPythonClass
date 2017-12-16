#임포트시
# from textreader.filereader import TextReader

#하드코딩시
# 텍스트 파일을 불러오는 클래스
class TextReader:
    def __init__(self, fileName):
        textFile = open(fileName, "r", encoding="utf8")
        self.text = textFile.read()

#쓸만한 함수
#문자열.replace("&nbsp;", "")
#리스트.sort()
#리스트.append()
#del 리스트[index]
#리스트.remove('값')
#리스트.extend(리스트)
#list(set(리스트)) -> 리스트 중복제거


firstFile = TextReader("dummy1.txt")
print(firstFile.text.split(",")[0:10])
firstList =firstFile.text.split(",")
print(len(firstList))
secondFile = TextReader("dummy2.txt")
print(secondFile.text.split(",")[0:10])
secondList = secondFile.text.split(",")
print(len(secondList))

# 공통 단어를 뽑아내는 함수
CommonWords = []
for word in firstList:
    if word in secondList:
        CommonWords.append(word)

print(list(set(CommonWords)))
