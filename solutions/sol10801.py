import sys

input = sys.stdin.readline


# 10801 카드게임
# 각 라운드에 더 높은 숫자를 낸 쪽이 게임에 이긴다고 할때
# 10라운드중 더 많은 라운드를 승리한 쪽을 구하는 문제
def sol10801():
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))
    ac, bc = 0, 0
    for i in range(10):
        if alist[i] < blist[i]:
            bc += 1
        elif alist [i] > blist[i]:
            ac += 1
    return 'A' if ac > bc else 'B' if ac < bc else 'D'
