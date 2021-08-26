import sys

input = sys.stdin.read


# 11758 CCW
# 주어진 세 좌표를 순서대로 연결했을 때 선분의 방향을 구하는 문제
# 벡터의 외적공식을 활용하면 쉽게 해결 가능하다.
def sol11758():
    # 세 점의 좌표
    ax, ay, bx, by, cx, cy = map(int, input().split())

    # CCW 알고리즘 적용
    res = (ax * by + bx * cy + cx * ay) - (bx * ay + cx * by + ax * cy)

    # 결과값이 0이라면 일직선, 0보다 크다면 반시계방향, 작다면 시계방향
    return 0 if res == 0 else (1 if res > 0 else -1)
