import sys

input = sys.stdin.read


# 2688 줄어들지 않아
# 각 자릿수가 이전 자릿수보다 크거나 같은 n자리 수의 갯수를 구하는 문제
def sol2688():
    n, *cases = map(int, input().split())
    mc = max(cases)

    # dp[i][j] j 로 끝나는 i자리 줄어들지 않는 수의 갯수
    dp = [[0] * 10 for _ in range(mc+1)]

    # 한자리 줄어들지 않는 수는 0~9까지 각각 1개씩
    dp[1] = [1] * 10

    # k로 끝나는 줄어들지 않는 i+1자리 수의 갯수는 k보다 작은 수로 끝나는
    # i자리 수의 갯수를 모두 더한 것과 같다
    for i in range(1, mc):
        for j in range(10):
            for k in range(j+1):
                dp[i+1][k] += dp[i][j]
    return '\n'.join(map(str, [sum(dp[i]) for i in cases]))
