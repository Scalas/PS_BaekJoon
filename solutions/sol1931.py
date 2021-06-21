import sys

input = sys.stdin.readline


# 1931 회의실 배정
# 회의의 시작시간과 종료시간이 주어졌을 때
# 회의 시간이 겹치지않게 선택할 수 있는 가장 많은 회의 수를 찾는 문제
# 최대한 많은 회의를 넣기 위해서는 종료시간이 빠른것을 우선적으로 선택할수록 좋다
# 다만 여기서는 한 회의의 종료와 동시에 다른 회의의 시작이 가능하기 때문에
# 시작 시간에 대해서도 정렬하지 않으면 (1, 1), (0, 1) 과 같은 케이스에서 예외가 발생한다
# 평범하게 (시작, 종료) 형태로 입력받아 람다함수로 정렬조건을 명시해도 되지만
# 실행시간을 단축하기 위해 처음부터 (종료, 시작)의 형태로 입력받아 정렬하였다
def sol1931():
    n = int(input())
    meeting = []
    for _ in range(n):
        s, e = map(int, input().split())
        meeting.append((e, s))
    meeting.sort()
    answer = 0
    time = 0
    for m in meeting:
        if m[1] >= time:
            answer += 1
            time = m[0]
    print(answer)

