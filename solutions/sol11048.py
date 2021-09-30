import sys

input = sys.stdin.readline


# 11048 이동하기
# N x M 크기의 미로의 각 방(1 x 1)마다 사탕이 일정 갯수 들어있고
# (1, 1) 방에서 시작하여 오른쪽, 아래, 우하단대각으로만 이동할 수 있으며
# 지나간 방의 사탕을 모두 가져갈 수 있다고 할 때, (N, M) 방까지 이동하며
# 가져갈 수 있는 사탕의 최대 갯수를 구하는 문제
def sol11048():
    # 미로의 크기
    n, m = map(int, input().split())

    # 미로의 각 방에 들어있는 사탕의 갯수
    laby = [list(map(int, input().split())) for _ in range(n)]

    # (i, j)로 이동하기 위해서는 (i-1, j-1), (i-1, j), (i, j-1) 셋중 한 방에서 이동해와야 한다.
    # 즉, dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + laby[i][j] 가 성립한다.
    # 하지만 조금 생각해보면 우하단 대각으로의 이동은 (N, M) 까지의 경로를 단축할 수는 있어도
    # 사탕을 많이 가져가는데는 전혀 도움이 되지 않는다.
    # 그러므로 최종적으로 점화식은 dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + laby[i][j] 가 된다.
    # 여기서는 dp 배열을 별도로 생성하지 않고 laby 배열내에서 점화식을 적용한다

    # 첫 행과 열은 비교를 위한 이전 행이나 열 중 한쪽이 없기때문에 단순히 누적합으로 처리한다.
    for i in range(n - 1):
        laby[i + 1][0] += laby[i][0]
    for i in range(m - 1):
        laby[0][i + 1] += laby[0][i]

    # 나머지 위치에 대해서는 위에서 구한 점화식을 적용한다.
    for i in range(1, n):
        for j in range(1, m):
            laby[i][j] += max(laby[i - 1][j], laby[i][j - 1])

    # laby 배열의 마지막 행, 마지막 열의 값이 얻을 수 있는 사탕의 최대 갯수가 된다.
    return laby[-1][-1]
