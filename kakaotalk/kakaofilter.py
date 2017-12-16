class Kakaofilter:
    def __init__(self, name, fileName):
        self.name = name
        self.fileName = fileName

    def textToList(self):
        textFile = open(self.fileName,"r",encoding="utf8")
        text = textFile.read()
        text = text.split("\n")
        newList = []
        index=0
        for i in text:
            if len(i)!=0 and index!=0:
                newList.append(i)
            index+=1
        return newList

    def fixText(self, textList):
        filteredList = []
        i=0
        for oneItem in textList:
            if oneItem[0] == "[":
                filteredList.append(oneItem)
                i+=1
            elif "---------------" in oneItem:
                pass
            else:
                filteredList[i-1]=filteredList[i-1]+oneItem
        return filteredList


    def userText(self, list):
        usersList=[]
        for item in list:
            if "["+self.name in item:
                usersList.append(item.split("] ")[2])
        return usersList

    def doAll(self):
        textList = self.textToList()
        fixedText = self.fixText(textList)
        return self.userText(fixedText)
