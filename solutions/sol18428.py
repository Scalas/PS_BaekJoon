import sys
from itertools import combinations

input = sys.stdin.readline


# 18428 감시 피하기
# n * n 격자공간에 학생과 선생님이 있고 선생님은 상하좌우로
# 장애물을 만나기 전까지 모든 학생을 감시할 수 있다고 할 때
# 빈 공간(학생도 선생님도 없는 공간)에 장애물을 3개 배치하여
# 모든 학생이 감시당하지 않도록 할 수 있는지 여부를 구하는 문제
def sol18428():
    n = int(input())
    board = [input().split() for _ in range(n)]

    # 선생님들의 좌표, 빈 공간의 좌표
    teachers = []
    candidates = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'T':
                teachers.append((i, j))
            elif board[i][j] == 'X':
                candidates.append((i, j))

    # 모든 학생들이 감시당하지 않을 수 있는지 확인
    def simulate():
        for tr, tc in teachers:
            ctr, ctc = tr, tc
            while ctr > 0:
                ctr -= 1
                if board[ctr][ctc] == 'O':
                    break
                if board[ctr][ctc] == 'S':
                    return False
            ctr, ctc = tr, tc
            while ctr < n - 1:
                ctr += 1
                if board[ctr][ctc] == 'O':
                    break
                if board[ctr][ctc] == 'S':
                    return False
            ctr, ctc = tr, tc
            while ctc > 0:
                ctc -= 1
                if board[ctr][ctc] == 'O':
                    break
                if board[ctr][ctc] == 'S':
                    return False
            ctr, ctc = tr, tc
            while ctc < n - 1:
                ctc += 1
                if board[ctr][ctc] == 'O':
                    break
                if board[ctr][ctc] == 'S':
                    return False
        return True

    # 함정 3개 배치
    for traps in combinations(candidates, 3):
        for trapr, trapc in traps:
            board[trapr][trapc] = 'O'
        if simulate():
            return 'YES'
        for trapr, trapc in traps:
            board[trapr][trapc] = 'X'

    return 'NO'
