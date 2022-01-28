import sys

input = sys.stdin.readline


# 4781 사탕 가게
# n 개의 사탕의 칼로리와 가격이 주어졌을 때
# m 만큼의 돈으로 살 수 있는 사탕의 칼로리의 합의 최댓값을 구하는 문제
def sol4781():
    answers = []
    while True:
        # 사탕의 종류와 가진 돈의 양
        n, m = map(conv, input().split())

        # 입력의 마지막
        if not n:
            break

        # 사탕의 칼로리와 가격
        # 같은 가격이라면 칼로리가 높은 사탕만 저장
        candies = {}
        for _ in range(n):
            c, p = map(conv, input().split())
            candies[p] = max(candies.get(p, 0), c)

        # 사탕을 한종류씩 사용하여 같은 가격으로 더 높은 칼로리를 갱신
        dp = [0] * (m+1)
        for p, c in candies.items():
            for price in range(p, m+1):
                dp[price] = max(dp[price], dp[price-p] + c)

        # 가진 돈을 사용해서 얻을 수 있는 최대 칼로리를 answers 에 저장
        answers.append(dp[-1])

    return '\n'.join(map(str, answers))


# 정수문자열은 정수로, 실수문자열은 100을 곱하여 소수점아래를 버린 정수로 반환
def conv(num):
    return int(num.replace('.', ''))
