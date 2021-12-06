import sys

input = sys.stdin.readline


# 2511 카드 놀이
# A와 B의 카드를 비교하여 숫자가 큰쪽이 승점 3을 가져가고 비긴다면 양쪽모두 1점을 가져간다
# 10번의 라운드의 결과 점수가 더 높은쪽이 승자가되며 점수가 같다면 마지막으로 이긴사람이 승자가된다.
# 만약 10번 모두 무승부라면 무승부가 된다.
# A와 B가 10라운드동안 제출한 카드가 주어졌을 때 두 사람의 승점과 게임의 최종결과를 구하는 문제
def sol2511():
    ar = list(map(int, input().split()))
    br = list(map(int, input().split()))
    a, b = 0, 0
    last_winner = 'D'
    for i in range(10):
        diff = ar[i] - br[i]
        if diff > 0:
            a += 3
            last_winner = 'A'
        elif diff < 0:
            b += 3
            last_winner = 'B'
        else:
            a += 1
            b += 1
    res = ('A' if a > b else 'B' if a < b else last_winner)
    return '\n'.join(['%d %d' % (a, b), res])
