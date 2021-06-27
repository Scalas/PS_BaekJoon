import sys

input = sys.stdin.read


# 9251 LCS
# 두 문자열의 공통 부분수열 길이의 최댓값을 구하는 문제
# 두 문자열의 각 위치까지의 최장 공통부분수열을 동적계획법으로 구해나가면 해결 가능하다
# str1은 i번째 문자까지, str2는 j번쨰 문자까지 비교한다고 할 때
# 경우의 수는 두 가지
# 1. str1[i] == str2[j] 인 경우 : i-1 번째 문자까지의 str1과 j-1번째 문자까지의 str2의 LCS길이보다 1 커진다
# 2. str1[i] != str2[j] 인 경우 : LCS의 길이가 늘어나진 않았기에 기존값을 가져와야함
#    이 경우 가져올 값은 str1[i]를 고려하지 않았을 때의 LCS 와 str2[j]를 고려하지 않았을 떄의 LCS 중 큰 값이다
def sol9251():
    str1, str2 = input().split()
    l = len(str1)
    dp = [0] * (l + 1)

    for c in str2:
        tmp = [0] * (l + 1)
        for i in range(1, l + 1):
            if c == str1[i - 1]:
                tmp[i] = dp[i - 1] + 1
            else:
                tmp[i] = max(dp[i], tmp[i - 1])
        dp = tmp

    print(max(dp))
