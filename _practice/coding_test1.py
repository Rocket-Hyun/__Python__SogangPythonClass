# https://alpha-school.programmers.co.kr/learn/challenge_codes/95

def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    dic = {}
    for text in strings:
        # 딕셔너리 안에 이미 해당 key 값이 있다면?
        if text[n] in dic:
            #원래 key에 해당하는 value 뒤에 ',값'을 붙여준다.
            dic[text[n]] = dic[text[n]]+","+text
        #없다면 그냥 key/value 패어로 추가
        else:
            dic[text[n]] = text
    #딕셔너리의 키값들만 리스트로 만들기
    keyList = list(dic.keys())
    #알파벳 오름차순으로 정렬
    keyList.sort()
    resultList = []

    #키값들만 있는 리스트를 돌리면서 딕셔너리에 대입하면서 원래 단어를 찾는다.
    for key in keyList:
        #만약에 value 값에 ,가 포함되어 있으면 같은 key값을 공유하던 단어들이므로
        #split을 써서 나눠준 후 각각을 resultList 리스트에 붙여준다.
        if ',' in dic[key]:
            for word in dic[key].split(","):
                resultList.append(word)
        #,가 없다면 한 단어 뿐이므로 그냥 resultList 리스트에 추가해준다.
        else:
            resultList.append(dic[key])
    return resultList



# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( strange_sort(["sun", "bed", "cer", "gogogoo", "google"], 1) )
