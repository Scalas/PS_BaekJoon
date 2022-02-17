import sys

input = sys.stdin.read


# 1344 축구
# 두 팀이 매 5분마다 골을 넣을 수 있는 확률이 백분율로 주어졌을 때
# 총 90분의 경기가 끝난 후 두 팀중 한팀이라도 득점수가 소수일 확률을 구하는 문제
# 단, 각 팀은 5분마다 많아도 1골밖에 넣지 못한다.
def sol1344():
    u, v = map(lambda x: int(x)/100, input().split())
    p = [[(1-u) * (1-v), u * (1-v)],
         [(1-u) * v, u * v]]

    # dp[i][j] 는 A팀이 i점, B팀이 j점일 확률
    # 처음엔 두 팀 모두 0점일 확률이 1(100%)
    dp = [[0] * 19 for _ in range(19)]
    dp[0][0] = 1

    # 5분씩 18번의 경기
    for _ in range(18):
        ndp = [[0] * 19 for _ in range(19)]
        for i in range(19):
            for j in range(19):
                prob = 0

                # 두 팀 모두 골을 넣지 못한경우
                prob += dp[i][j] * p[0][0]

                # A팀은 골을 넣은 경우
                if i > 0:
                    prob += dp[i-1][j] * p[1][0]

                # B팀은 골을 넣은 경우
                if j > 0:
                    prob += dp[i][j-1] * p[0][1]

                # 두 팀 모두 골을 넣은 경우
                if i > 0 and j > 0:
                    prob += dp[i-1][j-1] * p[1][1]

                ndp[i][j] = prob
        dp = ndp

    # 경기가 끝난 후 두 팀의 득점케이스중 최소 한쪽의 점수가 소수인 경우를 모두 합산
    primes = {2, 3, 5, 7, 11, 13, 17}
    answer = 0
    for i in range(19):
        for j in range(19):
            if i in primes or j in primes:
                answer += dp[i][j]
    return answer
