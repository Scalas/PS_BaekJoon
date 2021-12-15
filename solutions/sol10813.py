import sys

input = sys.stdin.readline


# 10813 공 바꾸기
# 1~N까지의 바구니에 순서대로 들어있는 공을 주어진 명령대로 위치를 변경한 후
# 공의 순서를 구하는 문제
def sol10813():
    n, m = map(int, input().split())
    balls = list(range(n+1))
    for _ in range(m):
        a, b = map(int, input().split())
        balls[a], balls[b] = balls[b], balls[a]

    return ' '.join(map(str, balls[1:]))
