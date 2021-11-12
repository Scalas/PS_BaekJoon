import sys

input = sys.stdin.readline


# 2502 떡 먹는 호랑이
# 첫날에 준 떡의 갯수가 a, 둘째날에 준 떡의 갯수가 b일 때
# 셋째날부터는 전날과 전전날에 준 떡의 갯수를 합친만큼의 떡을 줘야한다
# D 일째에 준 떡의 갯수가 K임이 주어졌을 때 a, b를 구하는 문제
def sol2502():
    d, k = map(int, input().split())
    # u, v => 전전날의 a의 갯수와 b의 갯수
    # w, x => 전날의 a의 갯수와 b의 갯수
    u, v, w, x = 0, 1, 1, 1

    # D 일쨰의 a의 갯수와 b의 갯수를 구한다
    for _ in range(d-3):
        u, v, w, x = w, x, u+w, v+x

    # a*w + b*x == k 인 a와 b를 구하여 반환
    a = 0
    while True:
        a += 1
        bx = k-a*w
        if not bx % x:
            b = bx // x
            return '%d\n%d' % (a, b)
