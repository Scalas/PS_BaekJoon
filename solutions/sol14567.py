import sys

input = sys.stdin.readline


# 14567 선수과목
# 1부터 n 까지의 과목의 선수관계가 주어졌을 때
# 각 과목을 이수하기 위해 필요한 최소 학기수를 구하는 문제
# 단, 한 학기에 들을 수 있는 과목 수에는 제한이 없으며
# 모든 과목은 매학기 개설된다.
def sol14567():
    n, m = map(int, input().split())

    # g[i] 는 i번 과목을 선수과목으로 가지는 과목의 리스트
    g = [[] for _ in range(n+1)]

    # i번 과목의 선수과목 수(진입차수)
    degree = [0] * (n+1)

    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        degree[v] += 1

    # 선수과목이 없는 과목
    q = [i for i in range(1, n+1) if not degree[i]]

    # 각 과목 이수에 필요한 최소학기 수
    answer = [0] * n

    # 현재 학기
    sem = 0

    # 이수할 수 있는 과목(선수과목이 없는 과목)이 남아있을 경우
    while q:
        # 한학기 진행
        sem += 1

        nq = []
        # 과목을 이수하여 이수완료한 학기를 저장하고
        # 해당 과목을 선수과목으로 가지는 과목의 선수과목 수를 감소
        # 선수과목 수가 0이된 과목은 다음학기에 이수 가능한 과목 리스트에 삽입
        for cur in q:
            answer[cur-1] = sem
            for nxt in g[cur]:
                degree[nxt] -= 1
                if not degree[nxt]:
                    nq.append(nxt)
        q = nq
    return ' '.join(map(str, answer))
