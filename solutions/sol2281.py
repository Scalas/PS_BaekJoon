import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)
INF = 10 ** 9


# 2281 데스노트
# n 개의 이름을 한줄에 m개의 빈칸을 가진 노트에 왼쪽부터 오른쪽으로, 위에서 아래로 차례대로 적어나간다.
# 단, 이름사이엔 반드시 한칸의 간격이 있어야하며 한 이름을 두 줄에 나눠 쓸 수는 없다.
# 이 때, 각 줄의 오른쪽 끝에 남는 빈칸의 수의 제곱의 합의 최솟값을 구히는 문제
# 마지막 줄의 빈칸은 아직 사용가능성이 있으므로 세지 않는다.
def sol2281():
    n, m = map(int, input().split())
    names = [int(input()) for _ in range(n)]

    # dfs(cur, left) = dp[cur][left] = cur 번째 이름을 적을 차례이며
    # 현재 줄에 남은 칸수가 left 일때 남은 이름을 모두 적었을때 남는 빈칸수의 제곱의 합의 최솟값
    dp = [[-1] * m for _ in range(n)]

    def dfs(cur, left):
        # 더이상 적을 이름이 없다면 0 반환
        if cur == n:
            return 0

        if dp[cur][left] < 0:
            length = names[cur]
            res = INF
            # 현재 줄에 이어쓰는 경우
            if length < left:
                res = min(res, dfs(cur+1, left-names[cur]-1))

            # 다음줄로 넘어가는 경우
            res = min(res, dfs(cur+1, m-names[cur]) + left ** 2)

            # 메모이제이션
            dp[cur][left] = res

        return dp[cur][left]

    # 첫 줄 첫 칸에는 반드시 0 번째 이름을 적기 때문에 (m - names[0])만큼의 빈칸이 남았을 때
    # 1 번 째 이름을 적는 경우 탐색
    return dfs(1, m-names[0])


if __name__ == '__main__':
    print(sol2281())
