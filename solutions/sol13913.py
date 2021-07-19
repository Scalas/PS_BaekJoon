# 13913 숨바꼭질 4
# n에서 -1, +1, *2 세개의 연산을 최소한의 횟수만큼 사용하여 k를 만드는 과정과 연산횟수를 구하는 문제


# bfs를 사용하여 특정 위치까지의 최단거리를 구하되 경로추적을 위해 이전단계의 숫자를 따로 저장해둔다
def sol13913(n, k):
    # 동생이 수빈이와 같은위치에 있거나 그보다 앞에 있는 경우 - 순간이동 사용불가
    if n >= k:
        return '\n'.join([str(n - k), ' '.join(map(str, range(n, k - 1, -1)))])

    dp = [False] * 100001
    path = [-1] * 100001
    q = [n]
    dp[n] = True
    t = 0
    lo, hi = max(2 * n - k, 0), min(k * 2 - n - 1, 100000)
    while q:
        nq = []
        for p in q:
            if p == k:
                nq = []
                break
            for nxt in [p - 1, p + 1, p * 2]:
                if lo <= nxt <= hi and not dp[nxt]:
                    dp[nxt] = True
                    path[nxt] = p
                    nq.append(nxt)
        q = nq
        t += 1

    res = []
    while k != -1:
        res.append(str(k))
        k = path[k]

    return '\n'.join([str(t - 1), ' '.join(res[::-1])])
