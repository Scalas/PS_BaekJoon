import sys

input = sys.stdin.readline


# 20055 컨베이어 벨트 위의 로봇
# 규칙에 따라 순차적으로 실행되는 작업이 몇단계에서 종료됐는지 구하는 문제
# 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
# 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면
#    가만히 있는다. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
# 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
# 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
def sol20055():
    n, k = map(int, input().split())
    belt = list(map(int, input().split()))
    robots = [0] * n

    zero_count = 0
    stage = 0
    # 과정 4 내구도가 0인 칸이 k개 미만일 동안 반복
    while zero_count < k:
        # 단계 1 증가
        stage += 1

        # 과정 1
        # 벨트 회전
        belt.insert(0, belt.pop())
        robots.insert(0, robots.pop())

        # 내리는 위치에 도달한 로봇 제거
        robots[n-1] = 0

        # 과정 2
        # 로봇 이동
        # 내리는 위치의 이전 칸부터 시작
        for idx in range(n-2, -1, -1):
            # 현 위치에 로봇이 없다면 continue
            if not robots[idx]:
                continue

            # 로봇이 이동할 위치
            nxt = idx + 1

            # 로봇이 이동할 위치에 다른 로봇이 없고 벨트의 내구도가 1 이상이라면 이동
            # 이동할 위치의 벨트의 내구도가 1 감소
            if not robots[nxt] and belt[nxt]:
                robots[nxt], robots[idx] = 1, 0
                belt[nxt] -= 1
                if not belt[nxt]:
                    zero_count += 1

        # 내리는 위치에 도달한 로봇 제거
        robots[n-1] = 0

        # 과정 3
        # 로봇 올리기
        # 올리는 위치에 로봇이 없고 내구도가 1 이상이라면 로봇을 올린다
        if not robots[0] and belt[0]:
            robots[0] = 1
            belt[0] -= 1
            if not belt[0]:
                zero_count += 1

    # 작업이 중단된 단계를 반환
    return stage
