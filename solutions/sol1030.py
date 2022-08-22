import sys

input = sys.stdin.readline


# 1030 프랙탈 평면
# 흰색의 1 * 1 정사각형 하나가 시간이 1 지날 때마다 n * n 개의 정사각형으로 쪼개지고
# 그중 가운데의 k * k 개의 정사각형이 검은색으로 칠해질 때
# s 초가 지난 후 정사각형의 모습중 r1행 c1열부터 r2행 c2열 까지의 모습을 출력하는 문제
def sol1030():
    s, n, k, r1, r2, c1, c2 = map(int, input().split())
    t = n ** s
    answer = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]

    def split_square(r, c, length, color):
        # 검은색이라면 범위를 검게 칠함
        if color:
            # 출력 범위 내에 속할 경우에만 칠함
            for i in range(max(r, r1), min(r + length, r2 + 1)):
                for j in range(max(c, c1), min(c + length, c2 + 1)):
                    answer[i - r1][j - c1] = 1

        # 크기 1 정사각형이라면 더이상 쪼개지 않음
        if length == 1:
            return

        # 단위 길이
        u = length // n

        # 가운데 k * k 칸을 제외한 양쪽 사이드 길이
        side = (n - k) // 2

        # n * n 칸에 대해 재귀호출
        # 그중 가운데 k * k 칸에 대해서는 color 값을 1로 하여 검게 칠함
        for i in range(n):
            for j in range(n):
                ncolor = 0
                # 가운데 k * k 일경우 ncolor를 1로 함
                if side <= i < n - side and side <= j < n - side:
                    ncolor = 1

                # 만약 출력범위를 포함하지 않는다면 재귀호출하지 않음
                nr, nc, nlength = r + i * u, c + j * u, u
                if nr + nlength <= r1 or nr > r2 or nc + nlength <= c1 or nc > c2:
                    continue

                split_square(nr, nc, nlength, ncolor)

    split_square(0, 0, t, 0)

    return '\n'.join([''.join(map(str, answer[i])) for i in range(len(answer))])
