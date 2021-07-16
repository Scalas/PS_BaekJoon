import sys


# 12852 1로 만들기 2
# n을 1로 만드는데 필요한 최소 연산 횟수와 과정을 구하는 문제
# 연산의 종류
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.


# 첫 번째 시도
# bottom up 동적계획법으로 각 n에서의 1이 되기위한 최소 연산횟수와 이전단계의 숫자를 구하여 해결
def sol12852(n):
    if n == 1:
        return f'0\n1'
    if n <= 3:
        return f'1\n{n} 1'

    dp = [0] * (n + 1)
    proc = [0] * (n + 1)
    dp[2] = dp[3] = 1
    proc[1] = 0
    proc[2] = 1
    proc[3] = 1
    for i in range(4, n + 1):
        p = i - 1
        if i % 2 == 0 and dp[i // 2] < dp[p]:
            p = i // 2
        if i % 3 == 0 and dp[i // 3] < dp[p]:
            p = i // 3
        dp[i] = dp[p] + 1
        proc[i] = p

    res = [str(dp[n])]
    path = [n]
    while n != 1:
        n = proc[n]
        path.append(n)
    res.append(' '.join(map(str, path)))
    return '\n'.join(res)


# 두 번째 시도
# Top down 동적계획법으로 해결
# -1을 하는 경우는 나머지를 더해주는것으로 처리
# n 까지의 모든 자연수에 대해 최소횟수를 구하는 Bottom up 에 비해 연산 횟수가 줄어들어 훨씬 빠르다.
def sol12852_2(n):
    dp = {1: 0, 2: 1, 3: 1}

    def proc(num):
        if num not in dp:
            dp[num] = min(proc(num // 2) + 1 + num % 2, proc(num // 3) + 1 + num % 3)
        return dp[num]

    answer = str(proc(n))
    path = [n]
    while n > 1:
        if dp[n] == dp[n // 2] + 1 + n % 2:
            if n % 2:
                n -= 1
                path.append(n)
            n //= 2
        else:
            while n % 3:
                n -= 1
                path.append(n)
            n //= 3
        path.append(n)
    return '\n'.join([answer, ' '.join(map(str, path))])
