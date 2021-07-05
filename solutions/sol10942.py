from sys import stdin

input = stdin.read


# 10942 팰린드롬?
# 주어진 수열에서 입력받은 구간(시작인덱스, 끝인덱스)이 팰린드롬(앞에서봐도 뒤에서봐도 같은 형태)인지 출력하는 문제
# seq[i:j] 가 팰린드롬이려면 seq[i+1:j-1]이 팰린드롬이고 양 끝 값이 같아야한다
# 이를 이용해서 동적계획법으로 풀 수 있다.
def sol10942():
    I = list(map(int, input().split()))
    n = I[0]
    seq = I[1:n + 1]
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        dp[i][i] = 1
        dp[i][i + 1] += (seq[i] == seq[i + 1])
    dp[n - 1][n - 1] = 1

    for g in range(2, n):
        for i in range(n - g):
            j = i + g
            dp[i][j] = dp[i + 1][j - 1] * (seq[i] == seq[j])

    answer = []
    for i in range(n + 2, len(I), 2):
        s, e = I[i], I[i + 1]
        answer.append(str(dp[s - 1][e - 1]))
    print('\n'.join(answer))


