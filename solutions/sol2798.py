import sys

input = sys.stdin.read


# 2798 블랙잭
# 합이 m을 넘지않는 세 카드의 합중 최댓값을 구하는 문제
# 카드를 세개 뽑는 모든 경우의수를 탐색하여 해결 가능
def sol2798():
    n, m, *cards = map(int, input().split())
    answer = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                s = cards[i] + cards[j] + cards[k]
                if answer < s <= m:
                    answer = s
    print(answer)
