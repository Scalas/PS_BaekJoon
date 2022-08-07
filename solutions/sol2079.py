import sys

input = sys.stdin.readline


# 2079 팰린드롬
# 주어진 문자열을 최소 갯수의 팰린드롬 문자열로 분할하는 문제
def sol2079():
    word = input().rstrip()
    n = len(word)
    if n == 1:
        return 1

    # [i, j] 가 팰린드롬인지 여부
    palindrome = [[False] * n for _ in range(n)]

    # j로 끝나는 팰린드롬의 시작인덱스 리스트
    palindrome_start = [[] for _ in range(n)]

    # 문자열의 i번째 문자까지의 최소 팰린드롬 수
    dp = [i + 1 for i in range(n)]

    # 팰린드롬 여부 계산
    for i in range(n):
        palindrome[i][i] = True
        palindrome_start[i].append(i)
        if i < n - 1 and word[i] == word[i + 1]:
            palindrome[i][i + 1] = True
            palindrome_start[i + 1].append(i)
    for g in range(3, n + 1):
        for i in range(n - g + 1):
            j = i + g - 1
            if word[i] == word[j] and palindrome[i + 1][j - 1]:
                palindrome[i][j] = True
                palindrome_start[j].append(i)

    # i에서 끝나는 팰린드롬 구간(1) + 이전까지의 최소 팰린드롬 갯수 중 최솟값을 구함
    for i in range(1, n):
        for pre in palindrome_start[i]:
            if not pre:
                dp[i] = 1
            else:
                dp[i] = min(dp[i], dp[pre - 1] + 1)

    return dp[-1]
