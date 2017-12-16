master = []
# write your own code
# open master2.dat
# 한줄에 하나의 숫자의 수험번호씩 있는 것은 확실하다고 함

# master2.dat 텍스트 파일을 읽어들임
textFile1 = open("master2.dat", "r", encoding="utf8")
texts1 = textFile1.read()
# 한줄에 하나씩 있다고 했으므로 \n을 기준으로 문자열을 나눠서 각각 리스트에 저장
for number in texts1.split("\n"):
    master.append(number)
print("1. Number of records in master = ", len(master))

apply = []
# write your own code
# open apply2.dat

# apply2.dat 텍스트 파일을 읽어들임
textFile2 = open("apply2.dat", "r", encoding="utf8")
texts2 = textFile2.read()
# 일단 \n을 기준으로 문자열을 나눠서 각각 리스트에 저장
for number in texts2.split("\n"):
    apply.append(number)
print("2. Number of records in apply = ", len(apply))


apply2 = []
# write your own code
# 한줄에 데이타가 하나씩인 것은 보장되지만, 데이타 클리닝이 안되어서
# 앞뒤로 블랭크가 있는 경우가 있을 수 있다고 하니 이 작업 필요하다

# apply 리스트를 for 문으로 돌면서
for number in apply:
    # 그 문자열 안에 블랭크가 있는지 확인해서
    if " " in number:
        # 블랭크가 있다면 블랭크를 없앤 후 number 변수에 다시 저정하고
        number = number.replace(" ","")
    # 하나하나씩 apply2 리스트에 넣는다.
    apply2.append(number)
print("3. Number of records in apply2 = ", len(apply2))


data1 = []
# write your own code
# master에는 없지만 apply에는 있는 데이타를 찾아내시오
# 원서 제출없이 현장에서 응시한 응사자의 수?

# 일단 appply2에 있는 데이터를 찾는거니까 apply2 리스트를 하나씩 돌면서
for applyNum in apply2:
    # 해당 값이 master 리스트에 있는지 확인하고
    if applyNum not in master:
        # master리스트에 해당 값이 없으면 data1 이라는 리스트에 넣는다.
        data1.append(applyNum)
print("4. Number of data = ", len(data1), data1)


data2 = []
# write your own code
# master에는 있지만 apply에는 없는 데이타를 찾아내시오
# 원서는 제출했지만 응시하지 않은 사람의 수?

# 일단 master에 있는 데이터를 찾는거니까 master 리스트를 하나씩 돌면서
for masterNum in master:
    # 해당 값이 apply2 리스트에 있는지 확인하고
    if masterNum not in apply2:
        # apply2 리스트에 해당 값이 없으면 data2 라는 리스트에 넣는다.
        data2.append(masterNum)
print("5. Number of data2 = ", len(data2), data2)
