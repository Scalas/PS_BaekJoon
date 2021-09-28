import sys

input = sys.stdin.readline


# 11052 카드 구매하기
# n개의 카드를 구매하려 하고 1개, 2개, ... , n 개 짜리 카드팩의 가격이 각각 주어졌을 때
# n개의 카드를 가장 비싸게 사는 경우의 총 지출을 구하는 문제
def sol11052():
    # 사야할 카드의 갯수
    n = int(input())

    # 카드팩의 가격
    packs = [0, *map(int, input().split())]

    # 사야할 카드의 갯수별 최대비용
    for i in range(2, n+1):
        # n개의 카드를 사기위한 최대비용은 max(packs[0] + packs[n], packs[1] + packs[n-1], ... , packs[n-1] + packs[1])
        # 즉, packs[n] = max([packs[k] + packs[n-k] for k in range(n)]) 가 된다.
        # 하지만 k가 n의 절반을 넘어서면서부터는 중복값이 나오기 때문에
        # 실질적으로는 packs[n] = max([packs[k] + packs[n-k] for k in range(n // 2 + 1)]) 가 된다.
        packs[i] = max([packs[k] + packs[i - k] for k in range(i//2+1)])

    # 카드 n개를 살 때의 최대비용 반환
    return packs[n]

