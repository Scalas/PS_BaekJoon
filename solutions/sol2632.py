import sys
from collections import defaultdict

input = sys.stdin.readline


# 2632 피자판매
# n조각으로 나눠진 피자 A와 m조각으로 나눠진 피자 B의 각 조각의 크기가 시계방향으로 주어졌을 때
# 각 피자에서 피자조각을 떼서 그 합이 손님이 주문한 크기와 같게 만들 수 있는 모든 경우의 수를 구하는 문제
# 단, 하나의 피자에서 두 조각 이상의 피자를 떼려할 경우 피자조각은 연속한 조각이어야한다.
def sol2632():
    # 손님이 주문한 피자의 크기
    k = int(input())

    # A 피자와 B 피자의 크기
    n, m = map(int, input().split())

    # 피자 A조각과 B조각의 조각의 크기 리스트를 2번 반복한 후 누적합을 구한다
    # 순환상태이기 때문에 모든 구간을 구하기 위함
    asize = [int(input()) for _ in range(n)] * 2
    for i in range(1, 2*n):
        asize[i] += asize[i-1]
    asize.append(0)

    bsize = [int(input()) for _ in range(m)] * 2
    for i in range(1, 2*m):
        bsize[i] += bsize[i-1]
    bsize.append(0)

    # piza, pizb는 A와 B 피자에서 각각 연속된 피자조각을 떼어 만들 수 있는 피자의 크기와 그 경우의 수
    piza = defaultdict(int)
    pizb = defaultdict(int)

    # 아무 조각도 떼지 않았을 경우와 모든 조각을 떼었을 경우는 1가지뿐
    piza[0] = 1
    pizb[0] = 1
    piza[asize[n-1]] = 1
    pizb[bsize[m-1]] = 1

    # 시작점 0~n-1 에서 뗴어낼 조각 수를 늘려가며 연속된 피자조각의 크기를 구하고
    # 그 크기를 만들 수 있는 경우의 수를 증가시킴
    # 단, 모든 피자조각을 떼는 경우는 제외한다
    for i in range(n):
        for g in range(n-1):
            piza[asize[i+g]-asize[i-1]] += 1
    for i in range(m):
        for g in range(m-1):
            pizb[bsize[i+g]-bsize[i-1]] += 1

    # A에서 0조각, B에서 k조각을 떼는 경우부터 시작
    # A에서 1, B에서 k-1 ... 와 같은 방식으로 모든 경우를 탐색
    answer = 0
    for pa in range(k+1):
        answer += piza[pa] * pizb[k-pa]

    return answer
