import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline


# 10942 팰린드롬?
# 주어진 수열에서 입력받은 구간(시작인덱스, 끝인덱스)이 팰린드롬(앞에서봐도 뒤에서봐도 같은 형태)인지 출력하는 문제
# seq[i:j] 가 팰린드롬이려면 seq[i+1:j-1]이 팰린드롬이고 양 끝 값이 같아야한다
# 이 점화식을 토대로 동적계획법을 적용하여 문제를 해결할 수 있다.
def sol10942():
    # 수열의 크기
    n = int(input())

    # 수열
    seq = list(map(int, input().split()))

    # 각 질의에 대한 정답
    answer = []

    # dp[s][e] 는 s부터 e까지의 수열이 팰린드롬인지 여부를 저장 (팰린드롬이라면 1, 아니라면 0)
    dp = [[-1] * n for _ in range(n)]

    # 길이 1의 수열은 항상 팰린드롬
    # 길이 2의 수열은 양 끝 값이 같다면 팰린드롬, 다르다면 팰린드롬이 아니다.
    for i in range(n):
        dp[i][i] = 1
        if i < n - 1:
            dp[i][i + 1] = 1 if seq[i] == seq[i + 1] else 0

    # 팰린드롬 여부를 반환하는 함수
    def isPalindrome(s, e):
        # 아직 계산하지 않은 값이라면 점화식에 따라 계산
        # 양 끝 값이 서로 같고 양 끝 값을 제외한 부분이 팰린드롬이라면 자신도 팰린드롬이다.
        if dp[s][e] < 0:
            dp[s][e] = 1 if seq[s] == seq[e] and isPalindrome(s + 1, e - 1) else 0
        return dp[s][e]

    # 각 질의에 대해 isPalindrome 함수를 호출하여 정답을 answer 리스트에 저장
    for m in range(int(input())):
        s, e = map(int, input().split())
        answer.append(isPalindrome(s - 1, e - 1))

    # 출력 조건에 맞춰 정답 리스트 반환
    return '\n'.join(map(str, answer))
