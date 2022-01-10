import sys

input = sys.stdin.readline
direction = [(-1, 0), (-1, -1), (-1, 1), (0, -1)]
INF = 10 ** 9


# 4883 삼각 그래프
# n행 3열 그래프의 각 노드의 가중치가 주어지고
# 각 노드에서 오른쪽, 아래(왼쪽, 가운데 오른쪽)로만 이동 가능할 때
# 맨 위 가운데 노드에서 맨 아래 가운데 노드로 이동하기 위해 거쳐야하는 노드의
# 가중치의 합의 최솟값을 구하는 문제
def sol4883():
    answer = []
    case_num = 0
    while True:
        n = int(input())
        if not n:
            break
        case_num += 1
        graph = [list(map(int, input().split())) for _ in range(n)]
        graph[0][0] = INF
        graph[0][2] += graph[0][1]
        for i in range(1, n):
            for j in range(3):
                res = INF
                if j > 0:
                    res = min(res, graph[i-1][j-1])
                    res = min(res, graph[i][j-1])
                res = min(res, graph[i-1][j])
                if j < 2:
                    res = min(res, graph[i-1][j+1])
                graph[i][j] += res
        answer.append('%d. %d' % (case_num, graph[-1][1]))
    return '\n'.join(answer)
