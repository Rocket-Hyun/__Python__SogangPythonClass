textFile = open("text.txt","r",encoding="utf8")
text = textFile.read()
text = text.replace("\n\n","\n")
text = text.replace("\n\n\n","\n")
textList = text.split("\n")

newList = []

for i in textList[:20]:
    print(i)

#print(textList[4:20])
i=0
for oneText in textList:
    if len(oneText) == 0:
        del textList[i]
        i-=1
    else:
        if oneText[0] != "[":
            textList[i-1]=textList[i-1]+textList[i]
            del textList[i]
            i-=1
    i+=1
#print(textList[0:20])

for i in textList[0:20]:
    print(i)
