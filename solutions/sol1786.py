import sys

input = sys.stdin.readline


# 1786 찾기
# 문자열 T 속에서 문자열 P가 등장하는 횟수와 그 위치를 구하는 문제
# KMP 알고리즘을 알아보는 문제이다.
def sol1786():
    # 전체 문자열 T
    T = input().replace('\n', '')

    # 찾을 문자열 P
    P = input().replace('\n', '')

    # 문자열 T, P의 길이 n, m
    n, m = len(T), len(P)

    # LPS 테이블
    dp = [0] * (m + 1)

    # P의 첫 위치이자 suffix의 길이
    i = 0

    # dp[j] 는 P[:j+1]의 LPS값
    for j in range(1, m):
        # 만약 P[i]와 P[j] 가 다르고 0보다 크다면
        # P[i]==P[j]가 될 때까지 i를 이전에 suffix가 이어졌던 부분까지 이동
        while i > 0 and P[i] != P[j]:
            i = dp[i - 1]

        # P[i]와 P[j]가 같다면 suffix의 길이를 1 증가
        # dp[j] 에 suffix의 길이를 저장
        if P[i] == P[j]:
            i += 1
            dp[j] = i

    # 문자열 P가 발견된 위치를 모두 저장할 리스트
    answer = []

    # 문자열 T, P의 탐색 위치
    i, j = 0, 0

    # i가 문자열 T의 길이에 도달하기 전 까지 반복
    while i < n:
        # T[i]와 P[j] 가 같다면 두 인덱스 모두 1씩 증가
        if T[i] == P[j]:
            i += 1
            j += 1

            # 인덱스가 증가한 결과 j가 m에 도달했다면
            # P와 일치하는 문자열을 발견한 것이기 때문에 answer에 append
            # j는 LPS 테이블을 참조하여 다음 탐색 위치(dp[j-1])로 이동
            # 다음 탐색에서는 이미 일치할 것을 알고있는 부분을 생략하고 탐색
            if j == m:
                answer.append(i - m + 1)
                j = dp[j - 1]

        # T[i] 와 P[j] 가 다르다면
        else:
            # 만약 P[0] 부터 일치하지 않았다면 T[i]와의 비교는 무의미하기 때문에 i += 1
            if j == 0:
                i += 1

            # j는 LPS 테이블을 참조하여 다음 탐색 위치로 이동
            j = dp[j - 1]

    # 문자열 P가 등장한 횟수와 위치를 출력형식에 맞춰 반환
    return '\n'.join(map(str, [len(answer), ' '.join(map(str, answer))]))
