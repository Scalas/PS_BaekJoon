import sys
from collections import deque

input = sys.stdin.readline
INF = float('inf')


# 10217 KCM Travel - 다시 풀어봐야할 문제
# 비용한계가 정해진 최단경로 문제
# 다익스트라를 활용하여 풀수는 있지만 최적화를 잘 하지 않으면 큐가 넘쳐 메모리초과나 시간초과 발생
# 큐에 넣는 조건
# 1. 비용이 한계비용 m을 넘은 경로는 큐에 넣지않는다
# 2. 같은 비용, 같은 도착점의 더 짧은 경로가 있다면 현재 경로는 큐에 넣지않는다

# 최적화 요소
# 1. visit와 같은 동적계획법을 사용하기 위한 배열을 선언할 경우 인덱스로 최대한 작은 값을 사용
# 2. 한번의 pop 마다 갱신해둘 수 있는건 최대한 갱신
#    이 코드의 경우 e까지 nc의 돈으로 이동한 최단시간은 nc 이상의 돈으로 이동한 경우에도 적용 가능하다
#    즉, nc보다 많은 돈을 쓰고도 nc만큼을 쓴 것보다 오래 걸린 경우를 걸러낼 수 있다.
def sol10217():
    answer = []
    for t in range(int(input())):
        n, m, k = map(int, input().split())
        g = [[] for _ in range(n + 1)]
        for _ in range(k):
            u, v, c, d = map(int, input().split())
            g[u].append((v, c, d))

        visit = [[INF] * (m+1) for _ in range(n + 1)]
        q = deque([(0, 0, 1)])
        visit[1][0] = 0
        while q:
            d, c, v = q.popleft()
            if visit[v][c] < d:
                continue
            for e, cost, dist in g[v]:
                nd, nc = d + dist, c + cost
                if nc <= m and nd < visit[e][nc]:
                    for i in range(nc, m+1):
                        if nd < visit[e][i]:
                            visit[e][i] = nd
                        else:
                            break
                    q.append((nd, nc, e))
        res = visit[n][m]
        answer.append('Poor KCM' if res == INF else str(res))
    print('\n'.join(answer))
