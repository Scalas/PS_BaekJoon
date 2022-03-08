import sys

input = sys.stdin.readline
INF = 10 ** 9


# 1865 웜홀
# 노드의 갯수 n과 그 사이의 양방향 간선 m개,
# 단방향 음수간선 w개가 주어질 때
# 그래프에서 음수 사이클이 발생하는지 확인하는 문제
def sol1865():
    answer = []
    for _ in range(int(input())):
        n, m, w = map(int, input().split())

        # 두 노드간의 거리
        dist = [[10000] * n for _ in range(n)]

        # 간선 리스트
        edge = []

        # 도로(양방향)
        for _ in range(m):
            s, e, t = map(int, input().split())
            s, e = s-1, e-1
            # 새로운 간선이라면 edge에 추가
            if dist[s][e] == 10000:
                edge.append((s, e))
                edge.append((e, s))

            # 가중치 최솟값으로 갱신
            if t < dist[s][e]:
                dist[s][e] = dist[e][s] = t

        # 웜홀(단방향 음수간선)
        for _ in range(w):
            s, e, t = map(int, input().split())
            s, e = s-1, e-1
            if dist[s][e] == 10000:
                edge.append((s, e))
            dist[s][e] = min(dist[s][e], -t)

        # 벨만-포드 알고리즘을 사용하여 사이클 검출
        def search(start):
            dp[start] = 0
            for i in range(n):
                for s, e in edge:
                    t = dist[s][e]
                    if dp[s] + t < dp[e]:
                        if i == n-1:
                            return True
                        dp[e] = dp[s] + t
            return False

        # 최단거리 초기값
        # 음수간선으로 인한 사이클의 발생을 검출하는 것은
        # 연결그래프 내에선 어느 노드를 시작점으로 하든 검출 가능하므로
        # 한 점에 대해 최단거리를 구했을 때 dp값이 INF가 아닌 노드에 대해서는
        # 벨만-포드 알고리즘을 수행할 필요가 없음
        dp = [INF] * n

        res = 'NO'

        # 모든 노드에 대해
        for start in range(n):
            # 이미 검사가 끝난 노드일 경우 continue
            if dp[start] != INF:
                continue

            # 노드 start를 시작점으로 하여 벨만-포드 알고리즘 수행
            # 사이클 검출시 시간이 줄어들며 출발위치로 돌아갈 수 있음을 표시하고 break
            if search(start):
                res = 'YES'
                break

        answer.append(res)

    return '\n'.join(answer)
