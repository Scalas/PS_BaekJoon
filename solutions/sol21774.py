import sys
from collections import defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline


# 21774 가희와 로그 파일
# <발생 일시>#<로그 레벨> 로 이루어진 n개의 로그파일이 주어지고
# <시작 일시>#<종료 일시>#<최소 로그 레벨> 로 이루어진 q개의 쿼리가 주어질 때
# 각 쿼리에 대해 시작 일시부터 종료 일시까지 로그 레벨이 최소 로그 레벨 이상인 로그의 총 발생 횟수를 구하는 문제
def sol21774():
    n, q = map(int, input().split())

    # 각 레벨별 로그를 딕셔너리(발생 일시 : 발생 횟수)로 관리
    log_count = [defaultdict(int) for _ in range(6)]
    for _ in range(n):
        time, level = input().split('#')
        level = int(level)-1
        for lv in range(6):
            if lv == level:
                log_count[lv][time] += 1
            else:
                log_count[lv][time] += 0

    # 인덱스 탐색을 위한 시간 리스트
    times = ['0000-00-00 00:00:00', *sorted(log_count[0].keys())]

    # 각 레벨별 시간에 따른 로그 발생 횟수
    counts = [[0] for _ in range(6)]
    for lv in range(6):
        for time in times[1:]:
            counts[lv].append(log_count[lv][time])
            counts[lv][-1] += counts[lv][-2]

    answers = []
    for _ in range(q):
        start, end, level = input().split('#')
        # 시작 시간에서 종료시간 사이의 구간합을 구하기 위한 시작과 끝 인덱스를 이분탐색으로 구함
        si, ei = bisect_left(times, start)-1, bisect_right(times, end)-1

        # 탐색할 로그의 최소 레벨
        level = int(level) - 1

        # 로그 레벨이 level 이상인 로그의 구간 내 발생 횟수를 구함
        answer = 0
        for lv in range(level, 6):
            answer += counts[lv][ei] - counts[lv][si]
        answers.append(answer)

    # 모든 쿼리의 결과 반환
    return '\n'.join(map(str, answers))
