from collections import deque


# 9019 DSLR
# 숫자 a에 네개의 연산을 사용하여 b를 만들기 위한 최단 루트를 찾는 문제
# bfs로 풀 수 있지만 파이썬으로는 통과하지못했다.
# 원래 파이썬으로는 쉽지않은 문제인듯 하지만 통과한사람이 있는걸로 봐서는 최적화가 부족한듯
# 나중에 다시 풀어볼것
def sol9019(case):
    res = []
    oprt = ['D', 'S', 'L', 'R']
    for a, b in case:
        dp = [''] * 10000
        proc = [-1] * 10000
        q = deque([a])
        dp[a] = 'E'
        while q:
            p = q.popleft()
            for i in range(4):
                nxt = conv(i, p)
                if not dp[nxt]:
                    dp[nxt] = oprt[i]
                    proc[nxt] = p
                    if nxt == b:
                        q = None
                        break
                    q.append(nxt)


        path = []
        while dp[b] != 'E':
            path.append(dp[b])
            b = proc[b]
        res.append(''.join(path[::-1]))
    return '\n'.join(res)


def conv(o, n):
    if o == 0:
        return (n * 2) % 10000

    if o == 1:
        return (n - 1) if n > 0 else 9999

    d1 = n // 1000
    n %= 1000
    d2 = n // 100
    n %= 100
    d3 = n // 10
    n %= 10
    d4 = n
    if o == 2:
        return d2 * 1000 + d3 * 100 + d4 * 10 + d1
    if o == 3:
        return d4 * 1000 + d1 * 100 + d2 * 10 + d3
