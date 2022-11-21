import sys

input = sys.stdin.readline


# 2668 숫자고르기
# 1부터 n까지의 숫자는 각각 1~n사이의 어떤 숫자와 연결되어있다
# 1부터 n중 어느 숫자들을 골랐을 때, 숫자의 집합과 그 숫자들과 연결된 숫자들의 집합이 같은 경우 중
# 집합의 크기가 제일 큰 경우를 구하는 문제
def sol2668():
    n = int(input())
    g = [int(input()) - 1 for _ in range(n)]

    answer = [-1]

    visited = [-1] * n

    # 결국 각 숫자와 연결된 숫자를 계속해서 타고 들어갔을 때,
    # 발생하는 사이클에 속하는 숫자들의 집합을 구하는 문제이다
    def get_cluster_size(start, cid):
        nxt = g[start]
        path = [start]
        while visited[nxt] == -1:
            visited[nxt] = cid
            path.append(nxt)
            nxt = g[nxt]

        if visited[nxt] != cid:
            return

        while path[-1] != nxt:
            answer.append(path.pop() + 1)
        answer.append(nxt + 1)

    cluster_id = 0
    for i in range(n):
        if visited[i] == -1:
            visited[i] = cluster_id
            get_cluster_size(i, cluster_id)
            cluster_id += 1

    answer.sort()
    answer[0] = len(answer) - 1

    return '\n'.join(map(str, answer))
