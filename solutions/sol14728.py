import sys

input = sys.stdin.readline


# 14728 벼락치기
# n개의 단원의 공부에 걸리는 시간과 해당 단원에서 나오는 문제의 배점,
# 공부할 수 있는 총 시간이 주어졌을 때 얻을 수 있는 최대점수를 구하는 문제
def sol14728():
    n, t = map(int, input().split())
    score = {0: 0}
    for _ in range(n):
        u, v = map(int, input().split())
        update = {}
        for time in score:
            weight = score[time]
            nt, nw = time+u, weight+v
            if nt <= t and score.get(nt, 0) < nw:
                update[nt] = nw
        score.update(update)
    return max(score.values())
