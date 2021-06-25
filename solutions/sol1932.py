import sys

input = sys.stdin.readline


# 1932 정수 삼각형
# 정수값으로 이루어진 삼각형의 꼭대기에서 아랫층의 숫자하나를 택하여 더하면서 내려올 때
# 맨 아랫층에 도달했을 때의 합의 최댓값을 구하는 문제
# 각 경로의 합의 최댓값을 동적계획법으로 구해나가면 해결가능
def sol1932():
    n = int(input())
    tri = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, n):
        for j in range(i + 1):
            a = -1
            if j > 0:
                a = max(a, tri[i - 1][j - 1])
            if j < i:
                a = max(a, tri[i - 1][j])
            tri[i][j] += a
    print(max(tri[-1]))
