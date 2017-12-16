import sys
import codecs

class KakaoAnalyzer:
    def __init__(self, fileName):
        self.fileName = fileName

    
    def talkSpliter(self):
        textFile = open(self.fileName, "r", encoding="utf8")
        text = textFile.read()
        text = text.split("\n")
        newList = []
        for i in text:
            if len(i)!=0:
                newList.append(i)
        return newList

    def fixText(self, textList):
        filteredList = []
        i=0
        for oneItem in textList:
            if "2017년 " in oneItem[0:7]:
                filteredList.append(oneItem)
                i+=1
            else:
                filteredList[i-1]=filteredList[i-1]+oneItem
        return filteredList

    def getUserText(self, user, filteredList):
        userTextList = []
        for item in filteredList:
            splitedText = item.split(":",2)
            if user in ':'.join(splitedText[:2]):
                #userTextList.append(''.join(splitedText[2:]))
                userTextList.append(item)
        return userTextList


    def doAll(self, user):
        textList = self.talkSpliter()
        filteredList = self.fixText(textList)
        userTextList = self.getUserText(user, filteredList)
        return userTextList


#fileName = sys.argv[1]
#userName = sys.argv[2]

junghyunTalk = KakaoAnalyzer("KakaoTalkChats2.txt")
for text in junghyunTalk.doAll("회원님"):
    print(text)
    print("\n")

f = codecs.open("회원님.txt", "w", "utf-8")
for i in junghyunTalk.doAll("회원님"):
    data = i+"\n"
    f.write(data)
#junghyunTalk.doAll("회원님")
