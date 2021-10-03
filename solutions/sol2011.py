import sys

input = sys.stdin.readline


# 2011 암호코드
# 알파벳 A~Z 를 1~26의 숫자로 치환하는 암호체계를 사용할 때
# 주어진 암호코드의 가능한 모든 해석의 갯수를 구하는 문제
def sol2011():
    # 나머지 연산을 위한 mod
    mod = 1000000

    # 암호코드
    s = [0, *map(int, list(input().rstrip()))]

    # 암호코드의 길이
    lens = len(s)

    # 첫 문자가 0이라면 잘못된 암호코드
    if not s[1]:
        return 0

    # dp[i] 는 s[1:i] 의 해석의 갯수
    dp = [0] * lens
    dp[0] = dp[1] = 1

    # 현재자리까지의 해석의 갯수는
    # 이전자리+현재자리를 두자리수의 암호코드로 해석하는 경우 + 현재자리를 한자리수의 암호코드로 해석하는 경우
    for i in range(2, lens):
        dp[i] = ((dp[i - 2] if s[i - 1] == 1 or (s[i - 1] == 2 and s[i] < 7) else 0) + (dp[i - 1] if s[i] else 0)) % mod

    # 마지막 자리까지의 해석의 갯수를 반환
    return dp[-1]
