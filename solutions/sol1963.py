import sys

input = sys.stdin.readline


# 1963 소수 경로
# 네 자리 소수로 이루어진 비밀번호는 매 단계마다 한 자리 씩만 변경할 수 있으며 항상 네 자리 소수인 상태를 유지해야한다.
# 두 네 자리 소수 src, dst 가 주어졌을 때, src를 dst로 바꾸기 위해 거쳐야할 단계 수의 최솟값을 구하는 문제
def sol1963():
    # 10000 미만의 수의 소수 여부 판별
    is_prime = [True] * 10000
    is_prime[0] = is_prime[1] = False
    for i in range(2, 10000):
        if is_prime[i]:
            is_prime[i * 2:10000:i] = [False] * (9999 // i - 1)

    # 각 네 자리 소수마다 한 자리만 변경하여 얻을 수 있는 네 자리 소수를 구함
    g = [[] for _ in range(10000)]
    for prime in range(1001, 10000):
        if not is_prime[prime]:
            continue

        digits = []
        tmp = prime
        while tmp:
            digits.append(tmp % 10)
            tmp //= 10
        while len(digits) < 4:
            digits.append(0)

        # 1000의 자리 변경
        prime_3 = prime - digits[3] * 1000
        for i in range(1, 10):
            nprime = prime_3 + 1000 * i
            if prime == nprime:
                continue
            if nprime < 1000:
                continue
            if is_prime[nprime]:
                g[prime].append(nprime)

        # 100의 자리 변경
        prime_2 = prime - digits[2] * 100
        for i in range(10):
            nprime = prime_2 + 100 * i
            if prime == nprime:
                continue
            if nprime < 1000:
                continue
            if is_prime[nprime]:
                g[prime].append(nprime)

        # 10의 자리 변경
        prime_1 = prime - digits[1] * 10
        for i in range(10):
            nprime = prime_1 + 10 * i
            if prime == nprime:
                continue
            if nprime < 1000:
                continue
            if is_prime[nprime]:
                g[prime].append(nprime)

        # 1의 자리 변경
        prime_0 = prime - digits[0] * 1
        for i in range(10):
            nprime = prime_0 + i
            if prime == nprime:
                continue
            if nprime < 1000:
                continue
            if is_prime[nprime]:
                g[prime].append(nprime)

    # src를 dst로 바꾸기 위해 필요한 최소 단계 수
    def bfs(src, dst):
        if src == dst:
            return 0

        q = [src]
        visited = [False] * 10000
        visited[src] = True
        count = 0
        while q:
            count += 1
            nq = []
            for cur in q:
                for nxt in g[cur]:
                    if nxt == dst:
                        return count

                    if not visited[nxt]:
                        visited[nxt] = True
                        nq.append(nxt)
            q = nq
        return -1

    answers = []
    for _ in range(int(input())):
        src, dst = map(int, input().split())
        result = bfs(src, dst)
        answers.append(str(result) if result != -1 else 'Impossible')

    return '\n'.join(answers)
