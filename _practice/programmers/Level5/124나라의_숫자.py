def change124(num):
    numbers = ['1','2','4']
    numberList = []
    while num>=3:
        numberList.append(numbers[(num%3)-1])
        if num%3 ==0:
        	num=(num-1)//3
        else:
        	num=num//3
    if num != 0:
        numberList.append(numbers[num-1])
    numberList.reverse()
    answer = "".join(numberList)

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(change124(12381213123123712893))
