import sys

input = sys.stdin.read


# 15990 1, 2, 3 더하기 5
# 각 테스트케이스의 1 이상 100000 이하의 정수 n에 대해
# n을 1, 2, 3의 합으로 나타내는 경우의 수를 구하는 문제
# 단, 같은 숫자를 두번 연속으로 더할 순 없다.
def sol15990():
    _, *tc = map(int, input().split())
    mod = 1000000009
    dp = [
        (1, 0, 0),
        (0, 1, 0),
        (1, 1, 1)
    ]
    for _ in range(3, max(tc)):
        dp.append((
            (dp[-1][1] + dp[-1][2]) % mod,
            (dp[-2][0] + dp[-2][2]) % mod,
            (dp[-3][0] + dp[-3][1]) % mod
        ))

    return '\n'.join(map(str, [sum(dp[n-1]) % mod for n in tc]))
