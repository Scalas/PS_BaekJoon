import sys

input = sys.stdin.readline


# 15966 군계일학
# n개의 수로 이루어진 수열에서 원래의 순서를 유지시킨채로 인접한 수 간의 차이가 1인 부분 수열을 뽑을 때
# 그 부분 수열의 최대 길이를 구하는 문제
def sol15966():
    n = int(input())
    seq = list(map(int, input().split()))

    # 숫자 num으로 끝나는 군계일학 수열의 최대길이는 num - 1로 끝나는 군계일학 수열의 최대길이 + 1 로 갱신가능
    dp = [0] * (max(seq) + 1)
    answer = 1
    for num in seq:
        dp[num] = max(dp[num], dp[num - 1] + 1)
        answer = max(answer, dp[num])

    return answer
