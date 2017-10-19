import codecs
import sys
from kakaofilter import Kakaofilter

name = sys.argv[1]
fileName = sys.argv[2]
talks = Kakaofilter(name, fileName)
FinalList = talks.doAll()

f = codecs.open(name+".txt", 'w', "utf-8")
for i in FinalList:
    data= i+"\n"
    f.write(data)
f.close()
