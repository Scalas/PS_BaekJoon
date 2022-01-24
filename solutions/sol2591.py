import sys

input = sys.stdin.readline


# 2591 숫자카드
# 1에서 34까지의 카드를 사용하여 만든 길이 40이하의 숫자를
# 1에서 34까지의 카드의 배열로 나타낼 수 있는 경우의 수를 구하는 문제
def sol2591():
    num = [0, *map(int, list(input().rstrip()))]
    dp = [0] * len(num)
    dp[0] = dp[1] = 1
    for i in range(2, len(num)):
        # 40이상의 1의자리가 0인 두자리수는 나타낼 수없음
        if not num[i] and num[i-1] >= 4:
            break

        # 이전 자리까지의 숫자를 나타내는 경우에 한자리수(1~9)를 붙이는 경우
        if num[i] > 0:
            dp[i] = dp[i-1]

        # 두 자리 전까지의 숫자를 나타내는 경우에 두자리수(10 ~ 34)를 붙이는 경우
        if 0 < num[i-1] <= 2 or (num[i-1]==3 and num[i] <= 4):
            dp[i] += dp[i-2]

    return dp[-1]
