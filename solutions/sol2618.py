import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


# 2618 경찰차
# (1, 1), (n, n)의 위치에 있는 두 대의 경찰차를 사건이 발생한 장소에 출동시킬 때
# 두 경찰차의 이동거리의 합을 최소화하는 출동순서를 구하는 문제
def sol2618():
    n = int(input())
    w = int(input())

    # 사건이 발생한 좌표 리스트
    works = [list(map(int, input().split())) for _ in range(w)]

    # dp[i][j] 는 1번경찰차와 2번경찰차가 각각 마지막으로 i번, j번 사건을
    # 해결한 상태일 때의 이동거리의 최솟값
    dp = [[-1] * (w+1) for _ in range(w+1)]
    answer = []

    # 현재 경찰차의 상태가 x, y 일때 다음에 처리해야할 사건의 번호는 nxt = max(x, y) + 1
    # 가능한 경우의 수는 x가 nxt 로 가거나 y가 nxt 로 가는 것
    # 계산결과를 dp 리스트에 메모이제이션하는 것으로 중복계산 방지
    def dfs(x, y):
        nxt = max(x, y) + 1
        if nxt-1 == w:
            return 0
        if dp[x][y] < 0:
            dp[x][y] = min(dfs(nxt, y) + dist(works, 1, x, nxt), dfs(x, nxt) + dist(works, n, y, nxt))

        return dp[x][y]

    # dp 배열을 구할 때 각 단계에서 보다 적은 이동거리를 얻을 수 있는 선택지를 골랐기에
    # 역추적시에도 마찬가지로 보다 적은 이동거리를 얻을 수 있는 선택지를 구해나가면 된다
    def trace(x, y):
        nxt = max(x, y) + 1
        if nxt-1 == w:
            return
        if dp[nxt][y]+dist(works, 1, x, nxt) < dp[x][nxt]+dist(works, n, y, nxt):
            answer.append(1)
            trace(nxt, y)
        else:
            answer.append(2)
            trace(x, nxt)

    # dp 배열을 구함과 동시에 최소 이동거리를 answer 배열에 삽입
    answer.append(dfs(0, 0))

    # 역추적 함수를 실행하여 answer 배열에 출동순서를 삽입
    trace(0, 0)

    return '\n'.join(map(str, answer))


# 두 사건간의 거리를 구하는 함수
# 번호가 0일 경우 k값에 따라 (1, 1) 또는 (n, n) 반환
def dist(pos, k, i, j):
    a, b = [k, k] if i == 0 else pos[i-1]
    c, d = [k, k] if j == 0 else pos[j-1]
    return abs(a - c) + abs(b - d)
