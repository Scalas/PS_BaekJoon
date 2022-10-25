import sys

input = sys.stdin.readline


# 3933 라그랑주의 네 제곱수 정리
# 어떤 숫자 n을 네 개 이하의 제곱수의 합으로 만드는 경우의 수를 구하는 문제
# 단, 구성 제곱수가 같고 순서만 다른 경우는 하나의 경우로 생각한다.
def sol3933():
    numbers = []
    while True:
        num = int(input())
        if not num:
            break
        numbers.append(num)

    m = max(numbers)

    # dp[i][j] 는  숫자 i 를 j개의 제곱수로 나타내는 경우의 수
    # 제곱수 1부터 시작해서 m 보다 작은 제곱수까지를 순차적으로 더해나가며 만들 수 있는 모든 경우의 수를 카운팅
    dp = [[0] * 5 for _ in range(m + 1)]
    dp[0][0] = 1
    for i in range(1, int(m ** .5) + 1):
        sq = i ** 2
        for j in range(m):
            for k in range(4):
                if not dp[j][k]:
                    continue
                nxt = j + sq
                if nxt > m:
                    continue
                dp[nxt][k + 1] += dp[j][k]

    return '\n'.join(map(str, [sum(dp[num]) for num in numbers]))
