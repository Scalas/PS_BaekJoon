import sys

input = sys.stdin.readline


# 1592 영식이와 친구들
# 규칙에따라 공을 던지고 받으며 한사람이 m번 공을 받을 때 게임은 끝이난다
# 게임이 끝났을 때 공을 던진 횟수를 구하는 문제
def sol1592():
    n, m, l = map(int, input().split())
    cnt = [0] * n
    idx = 0
    while True:
        cnt[idx] += 1
        if cnt[idx] == m:
            break

        if cnt[idx] % 2:
            idx = (idx + l) % n
        else:
            idx = (idx - l) % n
    return sum(cnt) - 1
