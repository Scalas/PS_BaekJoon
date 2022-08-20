import sys

input = sys.stdin.readline
sys.setrecursionlimit(50000)


# 13392 방법을 출력하지 않는 숫자 맞추기
# 원통형 숫자나사 n개로 구성된 자물쇠의 각 숫자나사를 모두 특정 숫자로 맞추려고 할 때
# 필요한 숫자나사 회전 수 합의 최솟값을 구하는 문제
# 단, 숫자나사는 왼쪽으로 돌릴때는 아래의 숫자나사들도 모두 같이 회전하지만 오른쪽으로 돌릴때는 돌린 숫자나사만 회전한다.
def sol13392():
    n = int(input())
    before = list(map(int, input().rstrip()))
    after = list(map(int, input().rstrip()))

    # dp[i][j] 는 i번 나사를 맞출 차례이고 지금까지의 누적 좌측 회전수가 j일 때
    # 남은 나사를 모두 맞추기 위해 필요한 최소 회전수
    dp = [[-1] * 10 for _ in range(n)]

    def dfs(cur, left):
        if cur == n:
            return 0

        if dp[cur][left] == -1:
            # 좌측 회전수에 따라 기존 숫자나사의 값 갱신
            bcur = (before[cur] + left) % 10
            acur = after[cur]

            # 기존 나사의 수와 맞춰야할 수의 차
            diff = abs(acur - bcur)

            # 이미 맞춰진 경우
            if bcur == acur:
                dp[cur][left] = dfs(cur + 1, left)

            # 기존 값보다 큰 값으로 만들어야하는 경우
            elif bcur < acur:
                dp[cur][left] = min(dfs(cur + 1, (left + diff) % 10) + diff, dfs(cur + 1, left) + 10 - diff)

            # 기존 값보다 작은 값으로 만들어야하는 경우
            else:
                dp[cur][left] = min(dfs(cur + 1, (left + 10 - diff) % 10) + 10 - diff, dfs(cur + 1, left) + diff)

        return dp[cur][left]

    return dfs(0, 0)
