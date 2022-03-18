import sys
from math import ceil

input = sys.stdin.readline


# 16434 드래곤 앤 던전
# 용사의 초기 공격력이 주어지고 던전의 방의 상태가 순서대로 다음과같이 주어진다.
# t: 방의 타입 - 1=몬스터 2=물약
# a: 1=몬스터의 공격력 2=물약의 공격력증가효과
# h: 1=몬스터의 체력 2=물약의 체력회복효과(최대체력 초과한 회복불가)
# 용사가 던전의 방을 순서대로 지나 마지막방의 용까지 물리치기 위한 최대 체력의 최솟값을 구하는 문제
def sol16434():
    n, atk = map(int, input().split())

    # 용사가 용을 물리치기 위해 필요한 최대체력의 최솟값
    answer = 0

    # 현재 용사가 입은 피해
    cur_damage = 0
    for _ in range(n):
        t, a, h = map(int, input().split())

        # 몬스터가 있는 경우
        if t == 1:
            # 용사가 받는 피해는 용사의 공격력으로 몬스터를 죽이는데
            # 필요한 턴수 - 1에 몬스터의 공격력을 곱한 수치
            cur_damage += (ceil(h / atk - 1) * a)
            answer = max(answer, cur_damage)

        # 물약이 있는 경우
        else:
            # 용사의 공격력 증가
            atk += a

            # 회복량은 h
            cur_damage = max(cur_damage - h, 0)

    # 용을 물리치려면 최소 용사가 입은 누적피해중 가장 큰 값 + 1만큼의 체력이 필요
    return answer + 1
