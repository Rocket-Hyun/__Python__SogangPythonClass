import plotly 
plotly.tools.set_credentials_file(username='Rocket-Hyun', api_key='n0UPp1dsatHr5oS5R5is')

import plotly.plotly as py
import plotly.graph_objs as go

stream_id = 'cyinop9ohv'
stream_1 = dict(token=stream_id, maxpoints=60)

trace1 = go.Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream_1
)

data = go.Data([trace1])

layout = go.Layout(title='Time Series')
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='python-streaming')

s = py.Stream(stream_id)
s.open()

import datetime
import time
import random
from kalkSpliter import KakaoAnalyzer


time.sleep(2)

myTalk = KakaoAnalyzer("KakaoTalkChats.txt")
for text in myTalk.doAll("회원님"):
    date = text.split(",",2)[0]
    #오후일땐 시간에 12시간 +
    if "오후" in date:
        dateTimeList = date.split(" 오후 ")
        dateTimeList[0] = dateTimeList[0].replace("년 ","-").replace("월 ","-").replace("일","")
        timeList = dateTimeList[1].split(":")
        timeList[0] = str(int(timeList[0]) + 12)
        dateTimeList[1] = ':'.join(timeList)
        usableTime = ' '.join(dateTimeList)

    #오전일땐 그대로
    else:
        dateTimeList = date.split(" 오전 ")
        dateTimeList[0] = dateTimeList[0].replace("년 ","-").replace("월 ","-").replace("일","")
        usableTime = ' '.join(dateTimeList)
        
    x = datetime.datetime.strptime(usableTime, "%Y-%m-%d %H:%M").strftime('%Y-%m-%d %H:%M:%S.%f')
    y = len(text.split(": ",2)[1])
    s.write(dict(x=x, y=y))
    time.sleep(1)  

s.close()
