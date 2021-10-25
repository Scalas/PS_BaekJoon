import sys

input = sys.stdin.readline


# 9466 텀 프로젝트
# 사이클에 속하지 않은 노드의 갯수를 찾아내는 문제
def sol9466():
    answer = []
    for _ in range(int(input())):
        n = int(input())
        select = [0, *map(int, input().split())]
        team = [False] * (n+1)
        cnt = 0
        for i in range(1, n+1):
            # 방문하지 않는 노드에 대해
            if not team[i]:
                # 해당 노드를 시작으로 연결된 노드가 아직 방문하지 않는 노드라면
                # 계속 방문해나가며 방문 리스트에 집어넣는다.
                cand = [i]
                team[i] = True
                cur = select[i]
                while not team[cur]:
                    team[cur] = True
                    cand.append(cur)
                    cur = select[cur]

                # 사이클을 찾은 경우 사이클에 해당하지 않는 노드의 갯수를 더한다
                try:
                    res = cand.index(cur)

                # 사이클을 찾지못한 경우 방문한 노드 전체의 갯수를 더한다
                except ValueError:
                    res = len(cand)
                cnt += res
        answer.append(cnt)
    return '\n'.join(map(str, answer))
