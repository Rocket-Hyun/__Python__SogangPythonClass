import urllib.request

url = "http://news.joins.com/article/21844194"
f = urllib.request.urlopen(url)
data = f.read().decode('utf-8')

# find => 첫번째 부분의 index가 나옴
begin = data.find("존경하는 국민 여러분")
end = data.find("감사합니다.")

print (begin)
print (end)

# 마지막은 감사합니다 이전 index니까 감사합니다.의 인덱스를 더해줌

end += len ("감사합니다.")
print (end)
print (data[begin:begin+100])
print (data[end-100:end])
print ("length=", end-begin)

speech = data[begin:end]
speech = speech.replace("&nbsp;", "")
speech = speech.replace("<br/>", "")

speech = speech.split()

analyze = {}
for word in speech:
    analyze[word] = analyze.get(word, 0) + 1

flist = sorted(analyze.items(), key=lambda kv: kv[1], reverse=True)
print("number of words is ", len(flist))

cnt = 0
for k, v in flist:
    print(k, v)
    if cnt > 100: break
    cnt += 1
