import sys

input = sys.stdin.read


# 10157 자리 배정
# 좌측 하단에서 시작하여 순서대로 1 ~ n * m번 손님에게 방을 배정할 때
# k번 손님에게 배정된 방의 좌표를 구하는 문제
def sol10157():
    m, n, k = map(int, input().split())

    # 가능한 좌석수를 초과하는 경우
    if k > n * m:
        return 0

    # 초기좌표
    r, c = 0, 1

    # 번호
    num = k

    # 행, 열 초기 이동칸수
    row, col = n, m

    while True:
        # 위로
        col -= 1
        if row >= num:
            r += num
            break
        r += row
        num -= row

        # 오른쪽으로
        row -= 1
        if col >= num:
            c += num
            break
        c += col
        num -= col

        # 아래로
        col -= 1
        if row >= num:
            r -= num
            break
        r -= row
        num -= row

        # 왼쪽으로
        row -= 1
        if col >= num:
            c -= num
            break
        c -= col
        num -= col
    return ' '.join([str(c), str(r)])
