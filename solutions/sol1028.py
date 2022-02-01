import sys

input = sys.stdin.readline


# 1028 다이아몬드 광산
# 다이아몬드 광산의 크기 r, c 와 광산의 상태(0, 1로 이루어진 2차원 배열)가 주어질 때
# 광산의 다이아몬드중 가장 큰 것을 찾는 문제
# 다이아몬드의 크기는 1로 이루어진 정사각형의 경계선을 45도 회전시킨 형태를 가진다
# ex)
# 1 1 0
# 1 0 1
# 0 1 1
# 위와 같의 형태의 경우
#   1
# 1   1
#   1
# 이처럼 크기가 2인 다이아몬드가 최대크기의 다이아몬드가 된다.
def sol1028():
    r, c = map(int, input().split())

    # (r, c)에서의 좌하단 대각선 길이, 우하단 대각선 길이
    left = [[0] * (c+2) for _ in range(r+2)]
    right = [[0] * (c+2) for _ in range(r+2)]

    # 광산의 상태
    mine = [[0] * (c+1)] + [[0, *map(int, input().rstrip())] for _ in range(r)]

    # left, right 구하기
    for i in range(r, 0, -1):
        for j in range(1, c+1):
            if mine[i][j]:
                left[i][j] = left[i+1][j-1] + 1
                right[i][j] = right[i+1][j+1] + 1

    answer = 0
    # 각 위치를 맨위로 했을 때의 다이아몬드 최대크기
    for i in range(1, r+1):
        for j in range(1, c+1):
            # 0인 위치는 다이아몬드를 만들 수 없음
            if not mine[i][j]:
                continue

            # 맨 위일 때
            # 좌우 하단대각선중 짧은쪽이 가능한 최대크기
            max_len = min(left[i][j], right[i][j])

            # 만약 가능한 최대크기가 기존의 최대크기 이하라면 더이상 진행할 필요 없음
            if max_len <= answer:
                continue

            # 기존의 최대크기보다 클 가능성이 있다면 최대크기+1부터 탐색
            for l in range(answer+1, min(left[i][j], right[i][j])+1):
                # 다이아몬드를 이루는지 검증하기 위해
                # 길이가 l일 때 좌, 우 꼭짓점의 우하단, 좌하단 길이가 l 이상인지 확인
                # 다이아몬드를 이룬다면 answer를 갱신
                row = i + l - 1
                lj, rj = j - l + 1, j + l - 1
                if right[row][lj] >= l and left[row][rj] >= l:
                    answer = max(answer, l)
    return answer
