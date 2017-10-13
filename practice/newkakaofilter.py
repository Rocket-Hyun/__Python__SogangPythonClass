def textToList():
    textFile = open("sglikelion.txt","r",encoding="utf8")
    text = textFile.read()
    text = text.split("\n")
    newList = []
    index=0
    for i in text:
        if len(i)!=0 and index!=0:
            newList.append(i)
        index+=1
    return newList

def fixText(textList):
    filteredList = []
    i=0
    for oneItem in textList:
        if oneItem[0] == "[":
            filteredList.append(oneItem)
            i+=1
        elif "---------------" in oneItem:
            pass
        else:
            # print(i)
            filteredList[i-1]=filteredList[i-1]+oneItem
    return filteredList


def userText(name, list):
    usersList=[]
    for item in list:
        if "["+name in item:
            usersList.append(item.split("] ")[2])
    return usersList

textList = textToList()
fixedText = fixText(textList)
print(userText("임동진",fixedText))
# for i in fixText(textList):
#     print(i)
#print(fixText(textList)[:10])
