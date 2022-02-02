import sys

input = sys.stdin.readline


# 2655 가장높은탑쌓기
# 밑면이 정사각형인 직육면체 벽돌을 사용하여 가장 높은 탑을 쌓으려한다
# 벽돌은 자신보다 밑면이 넓고 무게가 무거운 벽돌 위에만 쌓을 수 있다고 할 때
# 가장 높은 탑을 이루는 벽돌의 갯수와 각 벽돌의 번호를 맨 위에서부터 차례대로 출력하는 문제
def sol2655():
    n = int(input())

    # 벽돌의 밑면넓이, 무게, 높이, 번호를 저장
    blocks = []
    for i in range(1, n+1):
        a, h, w = map(int, input().split())
        blocks.append((a, w, h, i))

    # 벽돌을 밑면넓이, 무게를 기준으로 내림차순 정렬
    blocks.sort(reverse=True)

    # dp[i] 는 i번째 벽돌이 맨 위에 있도록 만들 수 있는 최대높이
    # trace[i]는 i번째 벽돌을 맨 위로 하여 최대높이를 만들 때 두 번째 벽돌의 인덱스
    dp = [0] * n
    trace = [-1] * n
    dp[0] = blocks[0][2]
    trace[0] = -1
    for i in range(1, n):
        # i번째 벽돌의 무게와 높이
        w, h = blocks[i][1], blocks[i][2]

        # dp[i]의 초기값은 i번째 벽돌만 쌓았을때의 높이
        dp[i] = h

        # 이전에 이미 쌓여있던 벽돌 위에 i번째 벽돌을 쌓을 경우
        for j in range(i):
            # j번째 벽돌 위에 i번째 벽돌을 놓을 수 있다면
            # 그 때 만들 수 있는 최대높이로 dp와 trace 갱신
            if blocks[j][1] > w and dp[j] + h > dp[i]:
                dp[i] = dp[j] + h
                trace[i] = j

    # 최대 높이로 쌓았을 때 맨 위의 벽돌로부터 시작하여
    # 아래에 쌓인 벽돌을 역추적하고 갯수를 파악
    answer = [0]
    top_block = dp.index(max(dp))
    while top_block != -1:
        answer.append(blocks[top_block][3])
        top_block = trace[top_block]
        answer[0] += 1
    return '\n'.join(map(str, answer))
