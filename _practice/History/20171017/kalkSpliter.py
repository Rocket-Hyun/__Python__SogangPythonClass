import sys

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
