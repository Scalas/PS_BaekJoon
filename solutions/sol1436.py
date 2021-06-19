import sys

input = sys.stdin.readline


# 1436 영화감독 숌
# 666이 들어가는 수 중 오름차순으로 n번째 수를 찾는 문제

# 첫 번째 시도
# 단순히 666이 들어가는지 체크하는 함수를 정의하여
# 666부터 숫자를 하나씩 증가시켜나가며 n번째 666이 포함된 수를 찾는 방법
# n이 작기때문에 시간내에 풀리긴 하지만 시간이 상당히 많이 소모된다
def sol1436():
    n = int(input())
    cnt = 1
    num = 667
    answer = 666
    while cnt < n:
        num += 1
        if (str(num).find('666') != -1):
            answer = num
            cnt += 1

    print(answer)


# 두 번째 시도
# 666에 앞뒤로 숫자를 붙여나가며 새로운 숫자를 만들어내는 풀이
# 반복문 한번에 생겨나는 숫자가 매우 빠르게 증가하기때문에
# n이 10만대를 벗어나면 효율이 떨어지기 시작한다
def sol1436_2():
    ends = {'666'}
    while len(ends) < 10000:
        added = set()
        for num in ends:
            for i in range(10):
                added.add(num + str(i))
                added.add(str(i) + num)
        ends |= added
    ends = list(set(map(int, ends)))
    ends.sort()
    print(ends[int(input()) - 1])
