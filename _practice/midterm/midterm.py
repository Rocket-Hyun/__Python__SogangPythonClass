#임포트시
from textreader.filereader import TextReader

#하드코딩시
# class TextReader:
#     def __init__(self, fileName):
#         textFile = open(fileName, "r", encoding="utf8")
#         self.text = textFile.read()


#쓸만한 함수
#문자열.replace("&nbsp;", "")
#배열.sort()
#배열.append()
#del 배열[index]


firstFile = TextReader("howtostartastartup.txt")
print(firstFile.text[0:50])
secondFile = TextReader("KakaoTalkChats.txt")
print(secondFile.text[0:50])