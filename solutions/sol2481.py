import sys

input = sys.stdin.readline


# 2481 해밍 경로
# n개의 이진코드가 주어지고 이진코드간의 해밍 거리가 1인 경우에만 코드간의 이동이 가능할 때
# 1번 코드로부터 주어진 m 개의 해밍 코드로 가는 경로를 구하는 문제
# 경로가 없다면 -1을 반환
def sol2481():
    n, k = map(int, input().split())
    
    # 해밍 코드간의 연결관계를 구함
    g = [[] for _ in range(n)]
    h = {}
    for i in range(n):
        code = int(input(), 2)
        h[code] = i
    for code, idx in h.items():
        # 최대 k자리까지 1비트 차이나는 해밍코드를 탐색
        # 해당 해밍코드가 노드중에 존재한다면 양방향 연결
        bit = 1
        for i in range(k):
            if code & bit:
                bit <<= 1
                continue
            ni = h.get(code + bit, -1)
            if ni != -1:
                g[idx].append(ni)
                g[ni].append(idx)
            bit <<= 1

    # bfs로 각 노드로 최단경로로 이동했을 때 이전 노드 번호를 저장
    pre = [-2] * n
    q = [0]
    pre[0] = -1
    while q:
        nq = []
        for cur in q:
            for nxt in g[cur]:
                if pre[nxt] == -2:
                    pre[nxt] = cur
                    nq.append(nxt)
        q = nq

    # 이전 노드정보를 역추적하여 경로를 구함
    answer = []
    for _ in range(int(input())):
        dst = int(input()) - 1
        path = []
        while dst >= 0:
            path.append(dst + 1)
            dst = pre[dst]
        if path and path[-1] == 1:
            answer.append(' '.join(map(str, path[::-1])))
        else:
            answer.append('-1')

    return '\n'.join(answer)
