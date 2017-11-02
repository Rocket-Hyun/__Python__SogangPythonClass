import datetime
from datetime import timedelta, date
# import matplotlib.pyplot as plt
# import numpy as np
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
            if len(i) != 0:
                newList.append(i)
        return newList

    def fixText(self, textList):
        filteredList = []
        i = 0
        for oneItem in textList:
            if "2017년 " in oneItem[0:7]:
                filteredList.append(oneItem)
                i += 1
            else:
                filteredList[i - 1] = filteredList[i - 1] + oneItem
        return filteredList

    def getUserText(self, user, filteredList):
        userTextList = []
        for item in filteredList:
            splitedText = item.split(":", 2)
            if user in ':'.join(splitedText[:2]):
                # userTextList.append(''.join(splitedText[2:]))
                userTextList.append(item)
        return userTextList

    def doAll(self, user):
        textList = self.talkSpliter()
        filteredList = self.fixText(textList)
        userTextList = self.getUserText(user, filteredList)
        return userTextList


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


wordFrequency = {}
myTalk = KakaoAnalyzer("KakaoTalkChats.txt")
talkList = myTalk.doAll("회원님")

startdate = talkList[0].split(",", 2)[0].replace("년 ", "-").replace("월 ", "-").replace("일", "").split(" ")[0].split("-")
lastdate = talkList[len(talkList)-1].split(",", 2)[0].replace("년 ", "-").replace("월 ", "-").replace("일", "").split(" ")[0].split("-")
start_date = date(int(startdate[0]), int(startdate[1]), int(startdate[2]))
end_date = date(int(lastdate[0]), int(lastdate[1]), int(lastdate[2])+1)
for single_date in daterange(start_date, end_date):
    wordFrequency[str(single_date)] = 0

for text in talkList:
    talkdate = text.split(",", 2)[0]
    # 오후일땐 시간에 12시간 +
    if "오후" in talkdate:
        dateTimeList = talkdate.split(" 오후 ")
        dateTimeList[0] = dateTimeList[0].replace("년 ", "-").replace("월 ", "-").replace("일", "")
        usableTime = dateTimeList[0]

    # 오전일땐 그대로
    else:
        dateTimeList = talkdate.split(" 오전 ")
        dateTimeList[0] = dateTimeList[0].replace("년 ", "-").replace("월 ", "-").replace("일", "")
        usableTime = dateTimeList[0]

    usableTime = datetime.datetime.strptime(usableTime, "%Y-%m-%d").strftime('%Y-%m-%d')
    wordFrequency[usableTime] = wordFrequency.get(usableTime, 0) + len(text.split(": ", 2)[1])

print(wordFrequency)

dateList = []
wordcountList = []
for key,value in wordFrequency:
    dateList.append(key)
    wordcountList.append(value)

print(dateList)
print(wordcountList)

# plt.plot(dateList, wordcountList)
# plt.ylabel('some numbers')
# plt.show()