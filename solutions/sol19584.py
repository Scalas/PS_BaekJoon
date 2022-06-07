import sys

input = sys.stdin.readline


# 19584 난개발
# n개의 주요지점과 그 사이를 잇는 도로의 정보(도로가 잇는 두 지점과 도로의 통행량)가 주어지고
# x축과 평행하게 철로를 지었을 때 철로가 도로와 교차하거나 도로가 잇는 지점중 하나와 만날 경우 도로를 철거해야한다고 할 때
# 철로를 지어 철거시킬 수 있는 도로의 통행량의 합의 최댓값을 구하는 문제
def sol19584():
    n, m = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(n)]

    # 지점을 잇는 구간들의 두 y좌표중 낮은쪽을 진입구간, 높은쪽을 탈출구간으로 하여 삽입
    sections = []
    for _ in range(m):
        u, v, d = map(int, input().split())
        y1, y2 = nodes[u-1][1], nodes[v-1][1]
        if y1 > y2:
            y1, y2 = y2, y1
        sections.append((y1, d))
        sections.append((y2, -d))
    sections.sort()

    answer = 0
    pre_y = 0
    p_acc = 0
    m_acc = 0
    for y, d in sections:
        # 이전 좌표와 같은 좌표일 경우
        if y == pre_y:
            # 도로가 시작되는 구간이라면 p_acc 값에 합산
            # 도로가 끝나는 구간이라면 m_acc 값에 합산
            if d >= 0:
                p_acc += d
            else:
                m_acc += d

        # 이전 좌표와 다른 좌표일 경우
        else:
            # 이전 좌표까지 늘어난 통행량으로 answer 갱신
            answer = max(answer, p_acc)

            # 줄어든 통행량 반영
            p_acc += m_acc
            m_acc = 0

            # 이전 좌표 갱신
            pre_y = y

            # 도로가 시작되는 구간이라면 p_acc 값에 합산
            # 도로가 끝나는 구간이라면 m_acc 값에 합산
            if d >= 0:
                p_acc += d
            else:
                m_acc += d

    # 마지막으로 늘어난 구간으로 answer 갱신
    answer = max(answer, p_acc)

    return answer
