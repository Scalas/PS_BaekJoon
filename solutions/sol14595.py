import sys

input = sys.stdin.readline


# 14594-14595 동방 프로젝트
# n개의 방과 1이상 n이하의 자연수 두개로이루어진 m개의 쿼리가 주어지고
# 쿼리 (i, j)의 의미가 i번방과 j번방 사이의 벽을 허무는 것이며
# 사이의 벽이 허물어진 방은 하나의 방이 된다고 할 때
# 모든 쿼리를 처리하고 남아있는 방의 갯수를 구하는 문제
def sol14595():
    n = int(input())
    m = int(input())
    wall = [0] * (n + 1)
    for _ in range(m):
        x, y = map(int, input().split())
        wall[x - 1] += 1
        wall[y - 1] += -1

    answer = 1
    for i in range(n - 1):
        wall[i] += wall[i - 1]
        if not wall[i]:
            answer += 1

    return answer
