import sys
from bisect import bisect_left

input = sys.stdin.readline


# 18353 병사 배치하기
# 병사들의 전투력이 번호순으로 주어졌을 때
# 일부 병사를 열외시키는 것으로 전투력을 내림차순으로 만들기 위해
# 열외시켜야할 병사 수의 최솟값을 구하는 문제
def sol18353():
    n = int(input())
    power = list(map(int, input().split()))
    # 병사의 번호를 전투력순으로 내림차순
    soldier = sorted(range(n), key=lambda x:-power[x])

    # 이미 전투력순으로 내림차순된 상태이기에 번호가 오름차순인지만 신경쓰면 된다.(최장증가수열)
    # 단, 오름차순인 번호여도 두 병사의 전투력이 같은 경우는 제외해야한다.
    lis = []
    for num in soldier:
        if not lis or num > lis[-1]:
            if lis and power[num] == power[lis[-1]]:
                continue
            lis.append(num)
        else:
            lis[bisect_left(lis, num)] = num
    return n - len(lis)
