import sys

input = sys.stdin.read


# 4354 문자열 제곱
# 문자열 a의 n 제곱을 문자열 a를 n번 이어붙이는 연산으로 정의하고(ex)  'abc'^3 == 'abcabcabc')
# 문자열 s가 주어졌을 때,  s 를 a^n 을 만족하는 가장 큰 n을 구하는 문제.
# KMP 알고리즘의 실패함수를 활용하여 해결할 수 있다.
def sol4354():
    # 각 케이스의 정답을 저장할 리스트
    answer = []

    # 케이스의 문자열 s
    for s in input().splitlines():
        # s가 '.'이라면 종료
        if s == '.':
            break

        # lps 테이블 전처리
        m = len(s)
        dp = [0] * m
        i = 0
        for j in range(1, m):
            while i > 0 and s[i] != s[j]:
                i = dp[i - 1]
            if s[i] == s[j]:
                i += 1
                dp[j] = i

        # 공통부분 v
        v = dp[-1] * 2 - m

        # 공통부분의 길이가 0보다 작은 경우
        # lps * 2 < m 이기 때문에 답은 1
        if v < 0:
            answer.append(1)

        # 공통부분의 길이가 0인 경우
        # lps * 2 == m 이기 때문에 답은 2
        elif v == 0:
            answer.append(2)

        # 공통부분의 길이가 1 이상인 경우
        else:
            # lps에서 공통부분을 뺀 길이
            u = dp[-1] - v

            # v가 u의 배수가 아니라면
            # 반복되는 문자열로 나타낼 수 없기 때문에 답은 1
            if v % u:
                answer.append(1)

            # v가 u의 배수라면
            # 양 끝의 u와 중간의 v//u 개의 u를 이어붙인 형태이기 때문에
            # u ^ (v//u + 2) 로 나타낼 수 있음.
            # 답은 v//u + 2
            else:
                answer.append(v // u + 2)

    # 정답 리스트를 출력형식에 맞춰 반환
    return '\n'.join(map(str, answer))
