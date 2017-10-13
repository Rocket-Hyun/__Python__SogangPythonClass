def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    dic = {}
    for text in strings:
        dic[text[n]] = text
    keyList = list(dic.keys())
    keyList.sort()
    resultList = []
    for key in keyList:
        resultList.append(dic[key])
    return resultList



# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( strange_sort(["sun", "bed", "car"], 1) )
