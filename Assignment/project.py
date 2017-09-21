import urllib.request

url = "http://paulgraham.com/hp.html"
f = urllib.request.urlopen(url)
data = f.read().decode('utf-8')

begin = data.find("May 2003")
end = data.find("unexpectedly sharp curves.")

print (begin)
print (end)

end += len ("unexpectedly sharp curves.")
print (end)
print (data[begin:begin+100])
print (data[end-100:end])
print ("length=", end-begin)

speech = data[begin:end]
speech = speech.replace("&nbsp;", "")
speech = speech.replace("<br>", "")
speech = speech.replace(".", " ")
speech = speech.replace(",", " ")

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
