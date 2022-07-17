import sys

input = sys.stdin.readline


# 2623 음악프로그램
# 1 ~ n 까지의 n명의 가수가 있고 m명의 pd들이 정한 가수들의 출연 순서가 있을 때
# 모든 순서를 만족하는 가수의 출연순서를 구하는 문제
def sol2623():
    n, m = map(int, input().split())

    # 가수들간의 순서관계를 그래프로 표현하고 각 가수의 진입차수를 계산
    g = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    for _ in range(m):
        _, *order = map(int, input().split())
        for i in range(len(order) - 1):
            g[order[i]].append(order[i + 1])
            degree[order[i + 1]] += 1

    # 진입차수가 0인 가수부터 시작하여 위상정렬
    q = [i for i in range(1, n + 1) if not degree[i]]
    answer = []
    while q:
        nq = []
        for cur in q:
            answer.append(cur)
            for nxt in g[cur]:
                degree[nxt] -= 1
                if not degree[nxt]:
                    nq.append(nxt)
        q = nq

    # 만약 모든 순서를 만족하여 n명의 가수를 모두 출연시킬 수 없을 경우 0 반환
    if len(answer) < n:
        return 0

    # 가수들의 순서를 한줄에 하나씩 출력하도록 반환
    return '\n'.join(map(str, answer))
