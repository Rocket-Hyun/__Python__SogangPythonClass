textFile = open("text.txt","r",encoding="utf8")
text = textFile.read()
text = text.replace("\n\n","\n")
text = text.replace("\n\n\n","\n")
#print("과연",text)
#print(text[111]=="\n")
#print(len(text[111]))
#print(text[113])
textList = text.split("\n")
#textList = textList[3:]

newList = []

for i in textList[:20]:
    print(i)

#print(textList[4:20])
i=0
for oneText in textList:
    #print(i)
    #print(len(oneText))
    #if i<10:
        #print("과연",oneText)
        #print(i)
    #if len(oneText)>0:
    #print(i)
    #print("에러전",oneText)
    #print(len(oneText))
    #print(oneText[0])
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

