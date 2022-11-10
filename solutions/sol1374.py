import sys
from collections import defaultdict

input = sys.stdin.readline


# 1374 강의실
# n 개의 강의의 시작시간과 끝 시간이 주어졌을 때
# 강의들이 서로 겹치지 않도록 하기 위해 필요한 강의실의 최소 갯수를 구하는 문제
# 단, 어떤 강의가 끝남과 동시에 다른 강의가 시작할 경우 두 강의는 한 강의실에서 처리 가능하다.
def sol1374():
    n = int(input())
    lecture = defaultdict(int)
    check_points = set()

    # 각 시간별로 시작되는 강의 수와 끝나는 강의 수를 표시
    for _ in range(n):
        _, u, v = map(int, input().split())
        lecture[u] += 1
        lecture[v] -= 1
        check_points.add(u)
        check_points.add(v)

    # 시간대별로 진행중인 강의 갯수를 누적합 방식으로 구하여
    # 한 시간대에 진행중읜 강의 수의 최댓값이 필요한 강의실의 최소 갯수가 된다.
    answer = 0
    room = 0
    for point in sorted(check_points):
        room += lecture[point]
        answer = max(answer, room)

    return answer
