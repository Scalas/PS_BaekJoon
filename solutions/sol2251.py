import sys

input = sys.stdin.readline


# 2251 물통
# A, B, C 물통의 최대용량이 주어지고 C에 물이 가득찬 상태로 시작하여
# 한 물통에서 다른 물통으로 물을 부을 떈 반드시 한쪽이 꽉차거나 한쪽이 빌 때 까지 부어야한다고 할 때
# A가 비어있는 경우에 가능한 C에 있는 물의 양의 모든 경우의 수를 구하는 문제
def sol2251():
    u, v, w = map(int, input().split())
    visited = [[[False] * (w + 1) for _ in range(v + 1)] for _ in range(u + 1)]

    # 0, 0, w 상태로 시작하여 매번 가능한 모든 물 붓기를 시도
    # 첫 번째 통의 물 양이 0인 경우에만 answer를 갱신
    q = [(0, 0, w)]
    visited[0][0][w] = True
    answer = []

    while q:
        nq = []
        for cu, cv, cw in q:
            if cu == 0:
                answer.append(cw)
            if cu:
                move = min(cu, v - cv)
                nu, nv, nw = cu - move, cv + move, cw
                if not visited[nu][nv][nw]:
                    visited[nu][nv][nw] = True
                    nq.append((nu, nv, nw))

                move = min(cu, w - cw)
                nu, nv, nw = cu - move, cv, cw + move
                if not visited[nu][nv][nw]:
                    visited[nu][nv][nw] = True
                    nq.append((nu, nv, nw))
            if cv:
                move = min(cv, u - cu)
                nu, nv, nw = cu + move, cv - move, cw
                if not visited[nu][nv][nw]:
                    visited[nu][nv][nw] = True
                    nq.append((nu, nv, nw))

                move = min(cv, w - cw)
                nu, nv, nw = cu, cv - move, cw + move
                if not visited[nu][nv][nw]:
                    visited[nu][nv][nw] = True
                    nq.append((nu, nv, nw))
            if cw:
                move = min(cw, u - cu)
                nu, nv, nw = cu + move, cv, cw - move
                if not visited[nu][nv][nw]:
                    visited[nu][nv][nw] = True
                    nq.append((nu, nv, nw))

                move = min(cw, v - cv)
                nu, nv, nw = cu, cv + move, cw - move
                if not visited[nu][nv][nw]:
                    visited[nu][nv][nw] = True
                    nq.append((nu, nv, nw))
        q = nq

    answer.sort()
    return ' '.join(map(str, answer))
