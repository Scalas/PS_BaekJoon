import sys

input = sys.stdin.read


# 15483 최소 편집
# 문자열 A와 B가 주어졌을 때
# 1. 문자열 A의 임의의 위치에 문자 하나 삽입
# 2. 문자열 A의 임의의 문자 하나 삭제
# 3. 문자열 A의 임의의 문자 하나 변경
# 위 세가지 연산만을 사용하여 A를 B로 만들 때
# 필요한 연산 횟수의 최솟값을 구하는 문제
def sol15483():
    str1, str2 = input().split()

    # dp[i][j] 는 문자열 A의 i번째 까지를 문자열 B의 j번째 까지
    dp = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]

    # A나 B중 한쪽이 빈 문자열일 때
    for i in range(len(str1)):
        dp[i][-1] = i+1
    for j in range(len(str2)):
        dp[-1][j] = j+1

    for i in range(len(str1)):
        for j in range(len(str2)):
            # 마지막 문자가 서로 같은 경우
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1]

            # 마지막 문자가 서로 다른 경우
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    return dp[-2][-2]
