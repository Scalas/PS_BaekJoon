import sys

input = sys.stdin.read


# 2718 타일 채우기
# 4 * n 크기의 타일을 2 * 1, 1 * 2 크기의 도미노로 채우는 경우의 수를 구하는 문제
def sol2718():
    _, *case = map(int, input().split())

    # 테스트케이스 최댓값
    n = max(case)

    # dp[i] 는 n이 i 일 때의 경우의 수
    dp = [1, 1]
    for i in range(2, n+1):
        # 1칸을 덮는 경우는 1개, 2칸을 덮는 경우는 4개
        dp.append(dp[-1] + dp[-2] * 4)

        # 3칸 이상부터는 짝수라면 3가지 경우의 수, 홀수라면 2가지 경우의 수가 존재
        for j in range(3, i+1):
            dp[i] += dp[i-j] * (3 - j % 2)
    return '\n'.join(map(str, [dp[i] for i in case]))
