import sys

input = sys.stdin.readline


# 1707 이분 그래프
# 그래프를 인접한 점이 다른 색이 되도록 칠할 수 있는지 구하는 문제
# 사용 가능한 색이 n개가 된 버전인 n분 그래프도 생각해볼것
def sol1707():
    answer = []
    for t in range(int(input())):
        v, e = map(int, input().split())
        g = [[] for _ in range(v)]
        for _ in range(e):
            v1, v2 = map(int, input().split())
            g[v1 - 1].append(v2 - 1)
            g[v2 - 1].append(v1 - 1)

        answer.append('YES' if div(g, v) else 'NO')
    print('\n'.join(answer))


def div(g, v):
    color = [0] * v
    for i in range(v):
        if not color[i]:
            q = [i]
            color[i] = 1
            while q:
                nq = []
                for vertex in q:
                    for nav in g[vertex]:
                        if not color[nav]:
                            color[nav] = -color[vertex]
                            nq.append(nav)
                        elif color[nav] == color[vertex]:
                            return False
                q = nq
    return True
