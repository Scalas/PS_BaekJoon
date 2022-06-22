import sys

input = sys.stdin.readline
INF = float('inf')


# 3860 할로윈 묘지
# w * h 격자공간의 묘지에서 (0, 0)에서 (w-1, h-1)로 이동하는데 걸리는 최소시간을 구하는 문제
# 단, 묘비가 있는 위치로는 이동 불가능하며 구멍이 있는 곳에 빠질 경우 일정 시간이 지난 후 다른 위치로 이동
# 걸어서 이동시에는 1초가 걸리며 구멍을 통해 이동시 음수시간이 나올 수 있다.
# 무한히 과거로 가는게 가능할 경우 never를, 출구로 갈 수 없다면 Impossible을, 그 외에는 최소시간을 반환한다.
def sol3860():

    def shortest_path(w, h):
        n = w * h
        g = [{} for _ in range(n)]
        # 묘비
        gs = set()
        for _ in range(int(input())):
            u, v = map(int, input().split())
            gs.add((v, u))

        # 귀신구멍
        hole = set()
        for _ in range(int(input())):
            u1, v1, u2, v2, d = map(int, input().split())
            hole.add((v1, u1))
            idx1, idx2 = w * v1 + u1, w * v2 + u2
            g[idx1][idx2] = d

        # 그래프 구성
        idx = 0
        for i in range(h):
            for j in range(w):
                if i == h - 1 and j == w - 1:
                    break
                if (i, j) in gs:
                    idx += 1
                    continue
                if (i, j) in hole:
                    idx += 1
                    continue
                if i > 0 and (i - 1, j) not in gs:
                    g[idx][idx - w] = 1
                if i < h - 1 and (i + 1, j) not in gs:
                    g[idx][idx + w] = 1
                if j > 0 and (i, j - 1) not in gs:
                    g[idx][idx - 1] = 1
                if j < w - 1 and (i, j + 1) not in gs:
                    g[idx][idx + 1] = 1
                idx += 1

        # 최단거리를 구함
        dp = [INF] * n
        dp[0] = 0
        for _ in range(n - 1):
            # 모든 간선 체크
            changed = False
            for cur in range(n):
                for nxt, dst in g[cur].items():
                    if dp[cur] + dst < dp[nxt]:
                        dp[nxt] = dp[cur] + dst
                        changed = True

            # 변경사항이 없을 경우
            if not changed:
                break

        # 계속해서 과거로 돌아가는 경우
        # 모든 간선 체크
        changed = False
        for cur in range(n):
            for nxt, dst in g[cur].items():
                if dp[cur] + dst < dp[nxt]:
                    dp[nxt] = dp[cur] + dst
                    return 'Never'

        # 빠져나올 수 없는 경우
        if dp[-1] == INF:
            return 'Impossible'

        # 그 외의 경우 묘지를 빠져나가는 최단시간 출력
        return dp[-1]

    answer = []

    while True:
        w, h = map(int, input().split())
        if w == h == 0:
            break
        answer.append(shortest_path(w, h))

    return '\n'.join(map(str, answer))
