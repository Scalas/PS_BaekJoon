import sys

input = sys.stdin.readline


# 2590 색종이
# 모서리 길이가 1 ~ 6인 정사각형 색종이의 갯수가 각각 주어지고
# 이를 모두 6 * 6 종이에 겹치지 않게 붙여야할 때
# 필요한 6 * 6 종이의 최소 갯수를 구하는 문제
# 단, 하나의 색종이는 하나의 6 * 6 종이에만 붙일 수 있다.
def sol2590():
    p1, p2, p3, p4, p5, p6 = [int(input()) for _ in range(6)]

    # 6 크기의 종이는 한장을 온전히 차지
    answer = p6

    # 5 크기의 종이는 한장당 하나씩만 들어가고
    # 1 크기의 종이 11개를 추가로 수용 가능
    for _ in range(p5):
        answer += 1
        p1 = max(p1 - 11, 0)

    # 4 크기의 종이는 한장당 하나씩만 들어가고
    # 2 크기의 종이 5개 또는 1 크기의 종이 20개를 추가로 수용가능
    for _ in range(p4):
        answer += 1
        remain = 20
        p2_count = min(p2, 5)
        p2 -= p2_count
        remain -= p2_count * 4
        p1 = max(p1 - remain, 0)

    # 3 크기의 종이는 한장당 네개씩 들어갈 수 있음
    answer += p3 // 4
    p3 %= 4

    # 3 크기의 종이가 남아있을 경우
    # 남은 종이가 한개라면 2 크기의 종이를 5개
    # 남은 종이가 두개라면 2 크기의 종이를 3개
    # 남은 종이가 세개라면 2 크기의 종이를 1개 추가로 수용가능
    # 그리고 남은 칸수만큼 1 크기의 종이를 수용 가능
    if p3:
        answer += 1
        remain = 36 - 9 * p3
        p2_count = p2
        if p3 == 1:
            p2_count = min(p2_count, 5)
        elif p3 == 2:
            p2_count = min(p2_count, 3)
        elif p3 == 3:
            p2_count = min(p2_count, 1)
        p2 -= p2_count
        remain -= p2_count * 4
        p1 = max(p1 - remain, 0)

    # 2 크기의 종이는 한장당 9개까지 들어갈 수 있음
    answer += p2 // 9
    p2 %= 9

    # 2 크기의 종이를 수용하고 남은 칸수만큼 1 크기의 종이를 수용 가능
    if p2:
        answer += 1
        remain = 36 - 4 * p2
        p1 = max(p1 - remain, 0)

    # 1 크기의 종이는 한장당 36장 들어갈 수 있음
    answer += p1 // 36

    # 남은 1 크기의 종이가 있을 경우 1장이 더필요함
    if p1 % 36:
        answer += 1

    return answer
