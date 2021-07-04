import sys

input = sys.stdin.readline


# 11066 파일 합치기
# 두 파일을 합치는데 드는 비용이 두 파일의 크기의 합일 때
# k개의 파일을 "연속으로" 하나로 합칠 때의 최소 비용을 구하는 문제

# 파일을 두 부분으로 나누는 모든 경우의 수를 검사하여 최소값을 구하는 방식으로 해결 가능
# 동적계획법으로 중복연산을 제거하면 O(N^3)으로 풀 수있다
# 그러나 파이썬으로는 시간초과가 발생하기에 PyPy3으로 제출하거나 다른 언어를 사용해야 한다
def sol11066():
    answer = []
    for t in range(int(input())):
        k = int(input())
        files = list(map(int, input().split()))
        total = [0] * (k + 1)
        for i in range(k):
            total[i + 1] = total[i] + files[i]

        dp = [[0] * (k + 1) for _ in range(k + 1)]
        for g in range(1, k):
            for i in range(1, k - g + 1):
                res = float('inf')
                j = i + g
                for m in range(i, j):
                    res = min(res, dp[i][m] + dp[m + 1][j] + total[j] - total[i - 1])
                dp[i][j] = res
        answer.append(str(dp[1][k]))
    print('\n'.join(answer))


# Kruth 최적화를 활용하여 O(N^2)으로 푸는 방식도 있지만 제대로 이해하지 못했기에 일단 생략한다
# O(N^2)으로 풀어야하는 문제가 별도로 있으니 나중에 따로 풀어볼것
