import sys

input = sys.stdin.readline


# 할 일 정하기 1
# 비트마스크 동적계획법의 연습문제
# n개의 사람과 n개의 일이 주어졌을때 누가 어느일을 해야 가장 효율이 좋은지 구하는 전형적인 할당문제
# 데이터의 크기가 더 커지면 헝가리안 알고리즘이라는 더 효율적인 방법을 사용해야하지만
# 이 문제에서는 비트마스크 동적계획법만으로도 해결이 가능하다.
def sol1311():
    # 일과 사람의 수
    n = int(input())

    # c[i][j] 는 i 번째 사람이 j 번째 일을 할 경우 드는 비용
    c = [list(map(int, input().split())) for _ in range(n)]

    # dp[t][visit] 는 t 번째 문제를 풀 차례이며 사람들의 상태(일을 맡았는지 아닌지)가
    # visited일 때 모든 일을 처리하기 위해 앞으로 필요한 비용의 최솟값
    dp = [[-1] * (1 << n) for _ in range(n)]

    # 완전탐색 함수
    def dfs(t, visit):
        # 모든 문제를 해결했다면 앞으로 필요한 비용은 0
        if t == n:
            return 0

        # 아직 계산한 적이 없는 단계일 경우
        if dp[t][visit] == -1:
            # 일을 맡지 않은 사람 하나를 택해 다음단계로 넘어가는 경우 중
            # t번째 일의 처리비용과 남은 일의 처리비용의 합의 최솟값이 dp[t][visit] 가 된다.
            dp[t][visit] = min([dfs(t + 1, visit | (1 << p)) + c[p][t] for p in range(n) if not (visit & 1 << p)])

        # 남은 문제를 해결하기 위한 최소비용 반환
        return dp[t][visit]

    # 첫 번째 문제를 해결해야 하고 아무도 일을 맡지 않은 상황에서부터 탐색하여 최소비용을 반환
    return dfs(0, 0)
