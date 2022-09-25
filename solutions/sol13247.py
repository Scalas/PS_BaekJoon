import sys
from itertools import combinations

input = sys.stdin.readline


# 13247 토끼의 이동
# n (<= 17) 개의 칸이 나열된 게임판 위에는 흰색(W), 검은색(B), 빨간색(R) 중 하나의 색이 칠해져있다.
# r (<= n) 마리의 토끼들은 각각 게임판의 칸 중 하나의 위치를 시작 위치로 고르며 이 선택은 겹치지 않는다.
# 토끼들은 자신이 밟고있는 판의 위치와 색에 따라 다음에 이동할 칸이 정해진다.
# 1. 0 번째 칸의 토끼는 항상 1 번째 칸으로 이동한다.
# 2. 게임판의 크기가 size 라고 할 때, size - 1, size - 1 번째 칸의 토끼는 항상 왼쪽으로 이동한다.
# 3. 이동이 모두 끝나고 같은칸에 둘 이상 모여있는 토끼들은 모두 사라진다.
# 4. 그 후 게임판은 맨 끝부분이 한칸씩 사라진다.
# 5. 위 과정을 게임판의 크기가 2보다 큰 동안 반복한다.
# 이 규칙에 따르면 게임이 끝나고 게임판의 크기는 항상 2이며 토끼는 한칸에 하나씩만 살아남을 수 있기 때문에
# 마지막에 남는 토끼의 수는 항상 0, 1, 2 셋 중 하나이다.
# 게임판의 초기 상태와 토끼의 수(r)가 주어졌을 때, 마지막에 남을 토끼의 수의 기댓값 (0 ~ 2)을 구하는 문제
def sol13247():
    board = input().rstrip()
    n = len(board)
    r = int(input())

    # cur_idx 번째 칸의 토끼가 다음으로 이동해야할 칸을 구하는 함수
    def move(cur_idx, length):
        if cur_idx == 0:
            return 1
        if cur_idx >= length - 2:
            return cur_idx - 1
        if board[cur_idx] == 'W':
            return cur_idx - 1
        if board[cur_idx] == 'B':
            return cur_idx + 1
        if board[cur_idx] == 'R':
            return pre_positions[cur_idx] if pre_positions[cur_idx] != -1 else cur_idx - 1

    # 살아남은 토끼의 누적합과 토끼의 초기 배치 케이스 수
    answer = 0
    case_count = 0

    # 토끼를 배치가능한 모든 케이스 탐색 (최대 C(17, 8) = 24310)
    for init_positions in combinations(range(n), r):
        length = n
        # pre_positions[i] 는 i 번째 칸에 오기 전 위치
        pre_positions = [-1] * n

        # cur_positions[i] 는 i 번째 칸에 있는 토끼의 수
        cur_positions = [0] * n
        for pos in init_positions:
            cur_positions[pos] = 1

        # 게임은 n - 2 번 진행됨(게임판이 2칸 남을 때 까지)
        for _ in range(n - 2):
            # 토끼의 이동
            nxt_positions = [0] * (length - 1)
            for i in range(length):
                if not cur_positions[i]:
                    continue
                dest = move(i, length)
                nxt_positions[dest] += 1
                pre_positions[dest] = i

            # 같은 칸에 두 마리 이상 남은 토끼의 소멸
            for i in range(length - 1):
                if nxt_positions[i] > 1:
                    nxt_positions[i] = 0

            # 게임판의 크기 축소
            length -= 1
            cur_positions = nxt_positions

        # 살아남은 토끼의 수 누적, 케이스 수 증가
        survived = sum(cur_positions)
        answer += survived
        case_count += 1

    # 기댓값(모든 케이스에서 살아남은 토끼의 수의 누적합을 케이스 수로 나눈 값)을 반환
    return answer / case_count
