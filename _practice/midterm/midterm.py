#임포트시
from textreader.filereader import TextReader

#하드코딩시
# class TextReader:
#     def __init__(self, fileName):
#         textFile = open(fileName, "r", encoding="utf8")
#         self.text = textFile.read()

#쓸만한 함수
#문자열.replace("&nbsp;", "")
#리스트.sort()
#리스트.append()
#del 리스트[index]
#리스트.remove('값')
#리스트.extend(리스트)


firstFile = TextReader("howtostartastartup.txt")
print(firstFile.text[0:50])
secondFile = TextReader("KakaoTalkChats.txt")
print(secondFile.text[0:50])