import sys
from collections import defaultdict
from math import floor

input = sys.stdin.readline


# 20056 마법사 상어와 파이어볼
# n * n 공간에서 파이어볼이 규칙에 따라 이동, 병합, 분할될 때
# k번의 이동, 병합, 분할이 발생한 뒤 남아있는 파이어볼의 질량의 합을 구하는 문제
def sol20056():
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    n, m, k = map(int, input().split())
    space = defaultdict(list)
    for i in range(m):
        r, c, m, s, d = map(int, input().split())
        space[(r, c)].append([m, s, d])

    # k번의 이동명령
    for _ in range(k):
        # 파이어볼 이동
        move_space = defaultdict(list)
        for pos in space:
            r, c = pos
            for m, s, d in space[pos]:
                nr, nc = (r + directions[d][0] * s) % n, (c + directions[d][1] * s) % n
                if not nr:
                    nr = n
                if not nc:
                    nc = n
                move_space[(nr, nc)].append([m, s, d])

        # 파이어볼이 두 개 이상 있는 칸에 대한 연산
        nspace = defaultdict(list)
        for pos in move_space:
            cnt = len(move_space[pos])
            if cnt == 1:
                nspace[pos].append(move_space[pos].pop())
                continue

            # 파이어볼 병합
            m_total, s_total, d_total = 0, 0, 0
            for m, s, d in move_space[pos]:
                m_total += m
                s_total += s
                d_total += (d % 2)

            # 파이어볼 분할
            nm, ns = floor(m_total / 5), floor(s_total / cnt)

            # 질량이 0이된 파이어볼은 소멸
            if not nm:
                continue

            # 파이어볼을 규칙에 따라 네 개로 분할
            nd = [0, 2, 4, 6] if (not d_total or d_total == cnt) else [1, 3, 5, 7]
            for d in nd:
                nspace[pos].append([nm, ns, d])

        # 이동, 병합, 분할이 완료된 후의 상태에서 다음 이동으로 이행
        space = nspace

    # 남아있는 모든 파이어볼의 질량의 합
    answer = 0
    for fireballs in space.values():
        for m, s, d in fireballs:
            answer += m

    return answer
