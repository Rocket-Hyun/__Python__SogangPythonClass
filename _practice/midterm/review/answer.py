master = []
# write your own code
# open master2.dat
# 한줄에 하나의 숫자의 수험번호씩 있는 것은 확실하다고 함
with open("master2.dat", "r") as f:
    master = f.readlines()
print("1. Number of records in master = ", len(master))


apply = []
# write your own code
with open("apply2.dat", "r") as f:
    apply = f.readlines()
# open apply2.dat
print("2. Number of records in apply = ", len(apply))


apply2 = []
# write your own code
# 한줄에 데이타가 하나씩인 것은 보장되지만, 데이타 클리닝이 안되어서
# 앞뒤로 블랭크가 있는 경우가 있을 수 있다고 하니 이 작업 필요하다
for k in apply:
    apply2.append(k.strip())
print("3. Number of records in apply2 = ", len(apply2))


data1 = []
# write your own code
# master에는 없지만 apply에는 있는 데이타를 찾아내시오
master2 = []
for k in master:
    master2.append(k.strip())
data1 = set(apply2) - set(master2)
# 원서 제출없이 현장에서 응시한 응사자의 수?
print("4. Number of data = ", len(data1), data1)


data2 = []
# write your own code
# master에는 있지만 apply에는 없는 데이타를 찾아내시오
# 원서는 제출했지만 응시하지 않은 사람의 수?
data2 = set(master2) - set(apply2)
print("5. Number of data2 = ", len(data2), data2)
