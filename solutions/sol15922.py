import sys

input = sys.stdin.readline


# 15922 아우으 우아으이야!!
# 수직선상의 선분의 시작과 끝 좌표가 n개 주어졌을 때
# 선분을 모두 그은 뒤 선분의 길이의 합을 구하는 문제
def sol15922():
    n = int(input())
    pos = [list(map(int, input().split())) for _ in range(n)]
    pos.sort()
    answer = 0
    s, e = pos[0][0], pos[0][1]
    for u, v in pos[1:]:
        if u <= e:
            e = max(e, v)
        else:
            answer += (e - s)
            s, e = u, v
    answer += (e - s)

    return answer
